from flask import Flask

app = Flask(__name__)

# Cambia aquí tu nombre y secreto
nombre = "José"
secreto = "1234"

@app.route('/')
def home():
    return f"hello {nombre}, tu secreto es: {secreto}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
