FROM python:3.9-buster

RUN mkdir shs
COPY . /shs/

RUN pip install -r /shs/requirements.txt

EXPOSE 8080/tcp

CMD ["python", "/shs/main.py"]
