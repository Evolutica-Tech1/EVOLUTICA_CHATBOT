# EVOLUTICA CHATBOT

## Docker Container

To deploy fastapi application run the following docker commands

```bash
# Build the container
docker build -t evolutica-chatbot .
# Run app
docker run -p 8000:8000 evolutica-chatbot
# Access to container details (executed and stopped containers)
docker ps -a
# Access to terminal and navegate into files
docker exec -it <container id> /bin/bash
docker ls -ll
# Stop container
docker stop evolutica-chatbot
```

This file is used to deploy the application in a cloud service

## Deploy in a cloud service

Dockerfile is used to deploy the entire application in web server to make the chatbot available to be consumed. Most of the hosting services allow to create a service like Railway, it recognizes Dockerfile and build up the application.

> While Building up the app its necessary to set up the environment variable `OPENAI_API_KEY`

## OpenAI Fine-Tunes

Steps:

1. Create a `training-data.jsonl`file with the following format:

```json
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
```

2. Run the following command:

```bash
openai tools fine_tunes.prepare_data -f training-data.jsonl
```

3. After that the openai will check if the jsonl promt-completion format are ok. In case it needs corrections, openai will ask to make changes and will export a second `.jsonl` with the name `training-data-prepared.jsonl` that will be ready to train in the next step
4. Connect to openai with API_KEY:

```python
import openai
from config.config import API_KEY
openai.api_key = API_KEY
```

5. Upload training file to your own openai account:

```python
openai.File.create(
  file=open("train-data-prepared.jsonl", "rb"),
  purpose='fine-tune'
)
```

6. Verify that the file was uploaded correctly and copy file-id:

```python
openai.File.list()
```

7. Train the model with FineTuned (chose an specific base model as a background):

```python
openai.FineTune.create(training_file="file-9DSXc7AWwU4oGpaVqeVDBdSR", model="davinci")
```

8. Run the next code to verify your openai models available and copy the name of your fine-tuned-model (the last model in the list):

```python
openai.Model.list()
```

9. Copy the id of the response and paste con the Completion method:

```python
openai.Completion.create(
        model="id-of-personal-trained-model",
        prompt="your prompt",
        temperature=0.5,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        #stop=["\n", "User: ", "AI: "]
    )
```
