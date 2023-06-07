import openai
from config.config import API_KEY
openai.api_key = API_KEY
conversation = ""
i = 1

while (i != 0):
    question = input("User: ")
    conversation += "\nUser: " + question + "\nAI: "
    response = openai.Completion.create(
        #model="text-davinci-003",
        model="davinci:ft-personal:model-with-csv-data-v1-0-2023-06-07-22-15-31",
        prompt=conversation,
        temperature=0.1, #0.5
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.8, #0.5
        presence_penalty=0.1, #0.0
        stop=["\n", "User: ", "AI: "]
    )
    answer = response.choices[0].text.strip()
    # print(answer)
    conversation += answer
    print("AI: " + answer + "\n")
