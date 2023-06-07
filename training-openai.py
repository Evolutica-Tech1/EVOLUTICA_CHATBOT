import openai
from config.config import API_KEY
openai.api_key = API_KEY
openai.File.create(
  file=open("train_data_prepared.jsonl", "rb"),
  purpose='fine-tune'
)
openai.File.list()