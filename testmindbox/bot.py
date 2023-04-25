import telebot
from telebot.types import Message

bot = telebot.TeleBot('6247252845:AAEIkzgPmySjLfcq_hdDMfIzCvcnajxmEc4')

@bot.message_handler(commands=['start'])
def start_handler(message: Message):
    bot.send_message(message.chat.id, "Привет я бот по вычислению площади фигур. Доступны команды /circle /triangle")

@bot.message_handler(regexp="Круг радиусом (\d+)")
def circle_handler(message: Message):
   radius = int(message.txt.split()[-1])
   circle = Circle(radius)
   area = circle.area()
   bot.send_message(message.chat.id, f'Площадь круга: {area}') 

@bot.exception_handler(Exception)
def error_handler(e):
    print(e)

if __name__ == '__main__':
    bot.polling(none_stop=True)