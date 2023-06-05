from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response

# conda install flask-cors para habilitar los cors y poder interactuar en forma separada con el frontend

app = Flask(__name__)
CORS(app)

""" 
SI UTILIZO LOS CORS PUEDO CORRER EL FRONTEND EN FORMA SEPARADA 
Y EN ESE CASO ELIMINO LA FUNCION index_get() y solo dejo el post
"""


""" @app.get("/")
def index_get():
    return render_template('index.html') """


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # Check if everithing is ok

    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
