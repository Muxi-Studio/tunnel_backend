#base image
FROM python:2.7
MAINTAINER muxistudio <muxistudio@qq.com>

ENV DEPLOY_PATH /tunnel_backend
RUN mkdir -p $DEPLOY_PATH
WORKDIR /tunnel_backend

ADD requirements.txt requirements.txt
RUN pip install --index-url http://pypi.doubanio.com/simple/ -r requirements.txt --trusted-host=pypi.doubanio.com

ADD . .
