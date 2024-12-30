FROM python:3.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
WORKDIR /Ultra-Forward-Bot
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Run patch script
COPY patch_pyrogram.py /app/patch_pyrogram.py
RUN python /app/patch_pyrogram.py

EXPOSE 8080

CMD ["/bin/bash", "/start.sh"]
