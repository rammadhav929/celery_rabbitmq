command to run rabbitmq(using docker):- docker run -d -p 5672:5672 rabbitmq

starts celery worker(👉 This starts the worker that will execute your task):- 

celery -A backend worker --loglevel=info
celery -A backend worker --loglevel=info --pool=solo