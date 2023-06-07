import openai
from config.config import API_KEY
openai.api_key = API_KEY


def get_response(message):
    response = openai.Completion.create(
        model="davinci:ft-personal:model-with-csv-data-2023-06-07-21-27-59",
        prompt=message,
        temperature=0.5,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        # stop=["\n", "User: ", "AI: "]
    )
    answer = response.choices[0].text.strip()
    return answer
