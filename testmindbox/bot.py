import telebot
from telebot.types import Message
from task import Circle


bot = telebot.TeleBot('6247252845:AAEIkzgPmySjLfcq_hdDMfIzCvcnajxmEc4')

@bot.message_handler(commands=['start'])
def start_handler(message: Message):
    bot.send_message(message.chat.id, "Привет я бот по вычислению площади фигур. Доступны команды /circle /triangle. 1. Щелкни по нужной фигуре и напиши 'Круг радиусом <цифра>' ")

@bot.message_handler(regexp="Круг радиусом (\d+)")
def circle_handler(message: Message):
   radius = int(message.text.split()[-1])
   circle = Circle(radius)
   area = circle.area()
   bot.send_message(message.chat.id, f'Площадь круга: {area}') 

@bot.message_handler(regexp='Треугольник со сторонами (\d+) (\d+) (\d+)')
def triangle_handler(message: Message):
    a, b, c = map(int, message.text.split()[-3:])
    triangle = Triangle(a, b, c)
    area = triangle.area()
    if triangle.is_right():
        bot.send_message(message.chat.id, f'Площадь треугольника: {area}\nТреугольник прямоугольный.')
    else:
        bot.send_message(message.chat.id, f'Площадь треугольника: {area}\nТреугольник не прямоугольный.')


@bot.exception_handler(Exception)
def error_handler(e):
    print(e)

if __name__ == '__main__':
    bot.polling(none_stop=True)