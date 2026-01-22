FROM python:3.13-trixie

WORKDIR /app

COPY . .

CMD [ "python3", "main.py"]
