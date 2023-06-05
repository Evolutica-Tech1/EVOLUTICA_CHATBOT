from fastapi import FastAPI, Request, HTTPException
from fastapi.encoders import jsonable_encoder
from json import JSONDecodeError
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from chat import get_response

# FastAPI App Instance
app = FastAPI(
                title='Chatbot-evolutica',
                description='Construcción de API para Chatbot',
                version = '1.0.0'
              )

""" "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000", """
""" origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) """

# Index: Pagina de inicio
@app.get("/", response_class=HTMLResponse)
async def index():
    return """ 
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Chatbot Evolutica</title>
            </head>
            <body>
                <h1>Versión 1.0.0 - FastAPI Chatbot Evolutica- Nicolas Lazarte</h1>
            </body>
            </html>
"""

@app.post("/predict")
async def predict(request : Request):
    try:
        data = await request.json()
        text = data.get("message")
        if text is None:
            raise HTTPException(status_code=400, detail="Invalid JSON payload: 'message' field is missing")
        response = get_response(text)
        message = {"answer": response}
    except JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON payload")
    return jsonable_encoder(message)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
