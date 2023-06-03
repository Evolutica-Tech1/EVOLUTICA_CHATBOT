import openai
from config import API_KEY
openai.api_key = API_KEY


def get_response(message):
    response = openai.Completion.create(
        model="text-davinci-003",
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


""" question = input("User: ")
conversation += "\nUser: " + question + "\nAI: "
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=conversation,
    temperature=0.5,
    max_tokens=100,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    stop=["\n", "User: ", "AI: "]
)
answer = response.choices[0].text.strip()
# print(answer)
conversation += answer
print("AI: " + answer + "\n") """
