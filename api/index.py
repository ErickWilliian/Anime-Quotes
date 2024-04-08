from flask import Flask,make_response,jsonify
import psycopg2
import os
from dotenv import load_dotenv,dotenv_values
from flask_cors import CORS


load_dotenv()

app = Flask(__name__)

CORS(app)

db = os.getenv("POSTGRES_DATABASE")
host = os.getenv("POSTGRES_URL")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")

conexao = psycopg2.connect(database=db, host=host, user=user, password=password)
cursor = conexao.cursor()


@app.route('/personagens',methods=['GET'])
def get_personagens():
    cursor.execute("SELECT * FROM personagens")
    rows = cursor.fetchall()
    personagens = []
    for row in rows:
        personagem = {
            'id': row[0],
            'name': row[1],
            'anime': row[2]
        }
        personagens.append(personagem)

    data = {'data': personagens}
    return make_response(
        jsonify(data)
    )


if __name__ == "__main__":
    app.run(debug=True)
