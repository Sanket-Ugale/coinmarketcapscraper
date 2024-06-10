import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coinmarketcapscrape.settings')

app = Celery('coinmarketcapscrape')
app.conf.enable_utc=False
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update(timezone='Asia/Kolkata')
app.autodiscover_tasks()
# celery beat settings
app.conf.beat_scheduler={}
@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
