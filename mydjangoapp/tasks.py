from celery import shared_task

@shared_task(bind=True, queue='CELERY-SILVER-PRIORITY-2')
def test_func(self,*args,**kwargs):
    for i in range(10):
        print(i)

    return "Done"