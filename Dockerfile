FROM python

WORKDIR /chatbot-api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn --bind 0.0.0.0:8000 app:app

# CMD [ "python", "./app.py" ]