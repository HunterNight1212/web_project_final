from django import template
import datetime
register = template.Library()

@register.filter()
def censored(value):
    result = ''
    try:
        for word in value.split():
            if word[0].isupper():
                word = word[0] + '*' * (len(word) - 1)
            result += word + ' '
    except ValueError:
        print('не применяется к нестроковым значениям')
    else:

        return result.strip()

# @register.filter()
# def time_in(value):
#     now_utc = datetime.datetime.now(datetime.timezone.utc)
#
