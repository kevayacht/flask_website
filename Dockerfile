FROM python:3.6
MAINTAINER Kevin Smith <kevinsmith.kis@gmail.com>

ENV PYTHONUNBUFFERED 1
ENV TZ='Africa/Johannesburg'
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir /config
ADD requirements.txt /config/
RUN pip install -r /config/requirements.txt

RUN mkdir /src;
WORKDIR /src