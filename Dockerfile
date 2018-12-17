FROM python:3.6

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN python3 -m pip install -r requirements.txt

COPY * /app

ENTRYPOINT [ "python" ]
CMD [ "manage.py" ]
