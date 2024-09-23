from flask import Flask, render_template
import os

app = Flask(__name__)

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
    # Dados fictícios para as ligas (temporariamente, até o banco de dados ser configurado)
    master_players = [
        {'name': 'MasterPlayer1', 'points': 5000},
        {'name': 'MasterPlayer2', 'points': 4900},
    ]
    
    diamond_players = [
        {'name': 'DiamondPlayer1', 'points': 4700},
        {'name': 'DiamondPlayer2', 'points': 4600},
    ]
    
    gold_players = [
        {'name': 'GoldPlayer1', 'points': 4400},
        {'name': 'GoldPlayer2', 'points': 4300},
    ]

    # Passar os dados fictícios para o template ranking.html
    return render_template("ranking.html", master_players=master_players, diamond_players=diamond_players, gold_players=gold_players)

if __name__ == "__main__":
    # Configurações para rodar no Railway
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

