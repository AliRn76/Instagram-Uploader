FROM python:3.10
ENV PYTHONUNBUFFERED 1

COPY start /usr/local/bin/
RUN chmod +x /usr/local/bin/start

RUN mkdir /app
WORKDIR /app
COPY . /app/

RUN pip install -U pip
RUN pip install -r requirements.txt
CMD ["start"]

