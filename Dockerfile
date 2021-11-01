FROM python:3

WORKDIR /usr/src/app

COPY ./app ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "gunicorn","--bind", "0.0.0.0:8080", "web:app" ]