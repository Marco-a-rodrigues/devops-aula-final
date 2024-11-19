FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./devops-aula-final /code/devops-aula-final

CMD ["fastapi", "run", "devops-aula-final/main.py", "--port", "80"]