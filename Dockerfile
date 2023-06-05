FROM tiangolo/uvicorn-gunicorn:python3.11

WORKDIR /chatbot-api

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD uvicorn app:app --host=0.0.0.0 --port=${PORT:-8000}