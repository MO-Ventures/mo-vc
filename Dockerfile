FROM python:3.9
WORKDIR /movc
COPY requirements.txt /movc/
RUN pip install -r requirements.txt
COPY . /movc/