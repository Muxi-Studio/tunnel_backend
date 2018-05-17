#base image
FROM python:2.7
MAINTAINER muxistudio <muxistudio@qq.com>

WORKDIR /TS
ADD . /TS
RUN pip install --upgrade pip
RUN pip install --index-url http://pypi.doubanio.com/simple/ -r requirements.txt --trusted-host=pypi.doubanio.com
ADD . . 


EXPOSE 3330

CMD ["python", "mproject_tunnel/manage.py", "createdb"] \
&& ["gunicorn", "-b", "0.0.0.0.3330", "app:app"]