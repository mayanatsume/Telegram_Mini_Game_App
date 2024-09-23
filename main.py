from flask import Flask, render_template, request
import os
import telebot

app = Flask(__name__)

# Substitua com o seu token de API fornecido pelo BotFather
TOKEN = "7894649662:AAHf8nPH2UWQmyxdPbHAYc-wP9GFiCzV_z0"
bot = telebot.TeleBot(TOKEN)

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

# Rota para o webhook do Telegram
@app.route(f'/{TOKEN}/', methods=['POST'])
def webhook():
    json_str = request.get_data(as_text=True)
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "ok", 200

# Definir o Webhook do Telegram no Flask
WEBHOOK_URL = f"https://telegramminigameapp-production.up.railway.app/{TOKEN}/"
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)

if __name__ == "__main__":
    # Configurações para rodar no Railway
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)


