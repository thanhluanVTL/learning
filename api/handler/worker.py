import os
from celery import Celery
from utils.utils import getenv


celery = Celery(__name__)
# celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
# celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")
celery.conf.broker_url = getenv("CELERY_BROKER_URL")
celery.conf.result_backend = getenv("CELERY_RESULT_BACKEND")