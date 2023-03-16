FROM python:3.11.2-alpine3.16

WORKDIR /app 

COPY requirements.txt /app/

RUN pip3 install --no-cache-dir -r requirements.txt 

COPY . /app/

CMD ["sh","start.sh"]