from flask import Flask

app = Flask(__name__)

nombre = "Jesús"
secreto = "xyz123"

@app.route('/')
def home():
    return f"hello {nombre}, tu secreto es: {secreto}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

