FROM python:3.6

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY * /app

ENTRYPOINT [ "python" ]
CMD [ "manage.py" ]
