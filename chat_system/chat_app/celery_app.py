from celery import Celery
from channels_presence.models import Room


app = Celery('tasks', broker='redis://localhost:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, prune.s(), name="Prune users", expires=10)

@app.task
def prune():
    Room.objects.prune_presences()