command to run rabbitmq(using docker):- 
🔹 Step 1 — Stop current RabbitMQ container
docker ps

Copy container ID, then:

docker stop <container_id>
docker rm <container_id>
🔹 Step 2 — Run compatible RabbitMQ version
docker run -d -p 5672:5672 rabbitmq:3.11-management


starts celery worker(👉 This starts the worker that will execute your task):- 

celery -A backend worker --loglevel=info this is for linux
celery -A backend worker --loglevel=info --pool=solo this for windows