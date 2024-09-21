<<<<<<< HEAD
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

# Função para criar o banco de dados e a tabela (execute uma vez para criar o banco)
def init_db():
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS players (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        points INTEGER NOT NULL,
                        category TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

# Função para adicionar dados fictícios (execute uma vez para preencher o banco)
def insert_dummy_data():
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    # Exemplo de dados
    players = [
        ('MasterPlayer1', 5000, 'master'),
        ('MasterPlayer2', 4900, 'master'),
        ('DiamondPlayer1', 4700, 'diamond'),
        ('DiamondPlayer2', 4600, 'diamond'),
        ('GoldPlayer1', 4400, 'gold'),
        ('GoldPlayer2', 4300, 'gold')
    ]
    cursor.executemany('INSERT INTO players (name, points, category) VALUES (?, ?, ?)', players)
    conn.commit()
    conn.close()

# Home page
@app.route("/")
def home():
    return render_template("home.html")

# Tasks page
@app.route("/tasks")
def tasks():
    return render_template("tasks.html")

# Friends page
@app.route("/friends")
def friends():
    return render_template("friends.html")

# Ranking page
@app.route("/ranking")
def ranking():
    # Conectar ao banco de dados e buscar os jogadores por categoria
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()

    # Obter os jogadores da categoria Master
    cursor.execute("SELECT name, points FROM players WHERE category = 'master' ORDER BY points DESC LIMIT 100")
    master_players = cursor.fetchall()

    # Obter os jogadores da categoria Diamond
    cursor.execute("SELECT name, points FROM players WHERE category = 'diamond' ORDER BY points DESC LIMIT 100")
    diamond_players = cursor.fetchall()

    # Obter os jogadores da categoria Gold
    cursor.execute("SELECT name, points FROM players WHERE category = 'gold' ORDER BY points DESC LIMIT 100")
    gold_players = cursor.fetchall()

    conn.close()

    # Passar os dados para o template ranking.html
    return render_template("ranking.html", master_players=master_players, diamond_players=diamond_players, gold_players=gold_players)

if __name__ == "__main__":
    # Inicializa o banco de dados e insere dados fictícios (apenas execute uma vez para criar e preencher o banco)
    init_db()
    insert_dummy_data()
    app.run(debug=True)
=======
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

# Função para criar o banco de dados e a tabela (execute uma vez para criar o banco)
def init_db():
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS players (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        points INTEGER NOT NULL,
                        category TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

# Função para adicionar dados fictícios (execute uma vez para preencher o banco)
def insert_dummy_data():
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    # Exemplo de dados
    players = [
        ('MasterPlayer1', 5000, 'master'),
        ('MasterPlayer2', 4900, 'master'),
        ('DiamondPlayer1', 4700, 'diamond'),
        ('DiamondPlayer2', 4600, 'diamond'),
        ('GoldPlayer1', 4400, 'gold'),
        ('GoldPlayer2', 4300, 'gold')
    ]
    cursor.executemany('INSERT INTO players (name, points, category) VALUES (?, ?, ?)', players)
    conn.commit()
    conn.close()

# Home page
@app.route("/")
def home():
    return render_template("home.html")

# Tasks page
@app.route("/tasks")
def tasks():
    return render_template("tasks.html")

# Friends page
@app.route("/friends")
def friends():
    return render_template("friends.html")

# Ranking page
@app.route("/ranking")
def ranking():
    # Conectar ao banco de dados e buscar os jogadores por categoria
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()

    # Obter os jogadores da categoria Master
    cursor.execute("SELECT name, points FROM players WHERE category = 'master' ORDER BY points DESC LIMIT 100")
    master_players = cursor.fetchall()

    # Obter os jogadores da categoria Diamond
    cursor.execute("SELECT name, points FROM players WHERE category = 'diamond' ORDER BY points DESC LIMIT 100")
    diamond_players = cursor.fetchall()

    # Obter os jogadores da categoria Gold
    cursor.execute("SELECT name, points FROM players WHERE category = 'gold' ORDER BY points DESC LIMIT 100")
    gold_players = cursor.fetchall()

    conn.close()

    # Passar os dados para o template ranking.html
    return render_template("ranking.html", master_players=master_players, diamond_players=diamond_players, gold_players=gold_players)

if __name__ == "__main__":
    # Inicializa o banco de dados e insere dados fictícios (apenas execute uma vez para criar e preencher o banco)
    init_db()
    insert_dummy_data()
    app.run(debug=True)
>>>>>>> master
