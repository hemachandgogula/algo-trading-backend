from app.core.celery_app import celery_app


@celery_app.task
def sample_task(name: str) -> str:
    return f"Hello, {name}!"
