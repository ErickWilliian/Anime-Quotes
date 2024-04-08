
# Aqui é a importação para a conexão de python com o postgree
import psycopg2

import os
from dotenv import load_dotenv,dotenv_values

load_dotenv()

# Aqui estabelece a conexão com o banco de dados
db = os.getenv("POSTGRES_DATABASE")
host = os.getenv("POSTGRES_URL")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")

conexao = psycopg2.connect(database=db, host=host, user=user, password=password)

# Aqui você inicia um cursor que vai fazer os comandos no postgree
cursor = conexao.cursor()

# E aqui ele inicia um comando de executar uma ação
# cursor.execute("INSERT INTO personagens (nome,anime) VALUES ('Byakuya','bleach')")

cursor.execute("SELECT * FROM personagens WHERE nome = 'Ichigo'")

# Obtendo o primeiro resultado
linha = cursor.fetchone()
print(linha)
# O commit funciona para confirmar as alterações
# Sem isso ele não confirma e os dados não são salvos no banco de dados
conexao.commit()


cursor.close()
conexao.close()
