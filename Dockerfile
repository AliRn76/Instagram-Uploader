FROM python:3.8
ENV PYTHONUNBUFFERED 1

COPY start /usr/local/bin/
RUN chmod +x /usr/local/bin/start

RUN mkdir /instagram-uploader
WORKDIR /instagram-uploader
COPY . /instagram-uploader/

RUN pip install -U pip
RUN pip install -r requirements.txt
CMD ["start"]

