FROM python:3.9.6-slim

WORKDIR /code
COPY . /code/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN apt-get install -y gcc libpq-dev libssl-dev 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "-w", "2", "-b", ":8080", "movc.wsgi"]