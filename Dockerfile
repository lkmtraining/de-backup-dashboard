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

RUN \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5 && \
  echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" >  /etc/apt/sources.list.d/mongodb-org-3.6.list && \
  apt update && \
  apt install -y mongodb-org 
 

# Define mountable directories.
VOLUME ["/data/db"]

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["mongod"]

# Expose ports.
#   - 27017: process
#   - 28017: http
EXPOSE 27017
EXPOSE 28017

EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python3", "/app/manage.py"]
CMD ["runserver", "0.0.0.0:80"]
