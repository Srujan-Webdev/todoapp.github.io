from django.http import request
from .views import sendmail

def my_cron_job():
    sendmail()
