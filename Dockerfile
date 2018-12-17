FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y software-properties-common vim
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN apt-get install -y git

# update pip
RUN python3.6 -m pip install pip --upgrade

RUN pip install pipenv

COPY ./requirements.txt /app/requirements.txt

RUN python3 -m pip install -r /app/requirements.txt

WORKDIR /app

COPY * /app/

#CMD ["python3", "/app/manage.py runserver 0:80" ]
#CMD ["/app/manage.py", "runserver 0:80"]

EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python3", "/app/manage.py"]
CMD ["runserver", "0.0.0.0:80"]
