FROM python:3.6

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app


COPY * /app/

ENTRYPOINT [ "python3" ]
CMD [ "python3 manage.py" ]
