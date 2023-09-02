FROM python:3.11.4

WORKDIR /app

COPY . .

RUN pip3 install fastapi uvicorn

CMD uvicorn main:app --host 0.0.0.0 --reload