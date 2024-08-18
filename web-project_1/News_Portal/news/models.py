from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reit = models.IntegerField(default=0)

    def update_rating(self):
        posts_rating = 0
        comments_rating = 0
        posts_comments_rating = 0
        posts = Post.objects.filter(author=self)
        for p in posts:
            posts_rating += p.reit
        comments = Comment.objects.filter(user=self.user)
        for c in comments:
            comments_rating += c.reit
        posts_comments = Comment.objects.filter(post__author=self)
        for pc in posts_comments:
            posts_comments_rating += pc.reit

        self.reit = posts_rating * 3 + comments_rating + posts_comments_rating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name.title()}'


state = 'ST'
news = 'NE'
positions = [
    (state, 'статья'),
    (news, 'новости')
]


class Post(models.Model):
    objects = None
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    state_news = models.CharField(max_length=2, choices=positions, default=news)
    time_in = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    hat = models.CharField(max_length=255)
    text = models.TextField(default='')
    reit = models.IntegerField(default=0)
    preview = models.CharField(max_length=124)

    def like(self):
        self.reit += 1
        self.save()

    def dislike(self):
        self.reit -= 1
        self.save()

    def previews(self):
        self.preview = self.text[:125] + '...'
        self.save()

    def __str__(self):
        return f'{self.author.user}: {self.preview} ({self.reit})'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    objects = None
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    time_in = models.DateTimeField(auto_now_add=True)
    reit = models.IntegerField(default=0)

    def like(self):
        self.reit += 1
        self.save()

    def dislike(self):
        self.reit -= 1
        self.save()



# команды shell в папке comands.py

