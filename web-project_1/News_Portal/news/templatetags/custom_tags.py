from django import template
import datetime

register = template.Library()

now_uts = datetime.datetime.now(datetime.timezone.utc)

register.simple_tag()
def time(format= '%b, %d, %Y'):
    return now_uts.strftime(format)