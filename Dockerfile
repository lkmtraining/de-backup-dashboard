FROM python:3.6

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY * /app

ENTRYPOINT [ "python" ]
CMD [ "manage.py" ]
