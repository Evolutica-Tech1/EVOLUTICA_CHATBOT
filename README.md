# EVOLUTICA_CHATBOT

## Docker Container

To deploy flask application run the following docker commands

```bash
# Build the container
docker build -t evolutica-chatbot .
# Run app
docker run -p 8080:8080 evolutica-chatbot
# Access to container details (executed and stopped containers)
docker ps -a
# Access to terminal and navegate into files
docker exec -it <container id> /bin/bash
docker ls -ll
# Stop container
docker stop evolutica-chatbot
```
