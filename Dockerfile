FROM python:latest

RUN mkdir /data
WORKDIR /data
ADD memtest.py /data/memtest.py
CMD ["python3", "memtest.py"]