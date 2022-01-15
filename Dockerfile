FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt update && \
    apt upgrade && \
    apt install ffmpeg libsm6 libxext6  -y

RUN mkdir /instagram-uploader
WORKDIR /instagram-uploader
COPY . /instagram-uploader/

RUN pip install -U pip
RUN pip install -r requirements.txt
CMD ["python", "main.py"]

