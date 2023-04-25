import telebot
from telebot.types import Message
from task1 import circle

bot = telebot.TeleBot('6247252845:AAEIkzgPmySjLfcq_hdDMfIzCvcnajxmEc4')

@bot.message_handler(commands=['start'])
def start_handler(message: Message):
    bot.send_message(message.chat.id, "Привет я бот по вычислению площади фигур. Доступны команды /circle /triangle")

@bot.message_handler(regexp="Круг радиусом (\d+)")
def circle_handler(message: Message):
   radius = int(message.text.split()[-1])
   circle = circle(radius)
   area = circle.area()
   bot.send_message(message.chat.id, f'Площадь круга: {area}') 



if __name__ == '__main__':
    bot.polling(none_stop=True)