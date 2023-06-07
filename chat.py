import openai
from config.config import API_KEY
openai.api_key = API_KEY


def get_response(message):
    response = openai.Completion.create(
        model="davinci:ft-personal:model-with-csv-data-v1-0-2023-06-07-22-15-31",
        prompt=message,
        temperature=0.2,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.8,
        presence_penalty=0.0,
        # stop=["\n", "User: ", "AI: "]
    )
    answer = response.choices[0].text.strip()
    return answer
