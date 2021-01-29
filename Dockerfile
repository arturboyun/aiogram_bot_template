FROM python:3.9

WORKDIR /bot

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "main.py"]
