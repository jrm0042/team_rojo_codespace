from flask import Flask

app = Flask(__name__)

nombre = "Javier"
secreto = "abcd"

@app.route('/')
def home():
    return f"hello {nombre}, tu secreto es: {secreto}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
