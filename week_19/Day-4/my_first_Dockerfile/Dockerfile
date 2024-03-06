FROM python:3.9

EXPOSE 5000
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

WORKDIR /my_first_Dockerfile

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run"]
