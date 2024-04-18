from flask import Flask, json, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return "Olá"


@app.route("/api/contatos", methods=['GET'])
def contatos():
    with open("./data/data.json", "r") as file:
        dataContatos = json.load(file)
        return jsonify(dataContatos)


if __name__ == '__main__':
    app.run(debug=True)