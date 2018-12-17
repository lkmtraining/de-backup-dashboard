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

RUN pipenv install --system --deploy

COPY ./requirements.txt /app/requirements.txt

RUN python3 -m pip install -r requirements.txt

WORKDIR /app

COPY * /app/

CMD ["python3", "./manage.py" ]
