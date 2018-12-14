FROM python:2

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "manage.py" ]
