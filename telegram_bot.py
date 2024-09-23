import telebot
import os

# Substitua com o seu token de API fornecido pelo BotFather
TOKEN = "7894649662:AAHf8nPH2UWQmyxdPbHAYc-wP9GFiCzV_z0"

# Inicializa o bot com o token
bot = telebot.TeleBot(TOKEN)

# Comando /start para quando o usuário iniciar o bot
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id  # ID único do Telegram do jogador
    username = message.from_user.username  # Nome de usuário do Telegram
    
    # Resposta de boas-vindas
    bot.send_message(message.chat.id, f"Olá, {username}! Bem-vindo ao jogo.")
    
    # Aqui você pode salvar o ID e nome de usuário no banco de dados ou exibir no console
    print(f"Jogador {username} (ID: {user_id}) entrou no jogo.")

# Definir o Webhook
WEBHOOK_URL = f"https://telegramminigameapp-production.up.railway.app/{TOKEN}/"
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)

