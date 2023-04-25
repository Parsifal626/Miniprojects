from telegram.ext import Updater, CommandHandler
import logging
import math


# Конфигурация логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Определение функций для вычисления площади круга и треугольника
def circle_area(radius):
    """
    Вычисляет площадь круга по его радиусу.
    """
    return math.pi * radius**2

def triangle_area(a, b, c):
    """
    Вычисляет площадь треугольника по трем его сторонам, используя формулу Герона.
    """
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Обработчики команд бота
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Привет! Я бот для вычисления площади круга и треугольника. Для вычисления площади круга используйте команду /circle, а для вычисления площади треугольника используйте команду /triangle.')

def circle(update, context):
    try:
        radius = float(context.args[0])
        if radius <= 0:
            raise ValueError
        area = circle_area(radius)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Площадь круга с радиусом {radius} равна {area:.2f}.')
    except (ValueError, IndexError):
        context.bot.send_message(chat_id=update.effective_chat.id, text='Некорректный радиус круга.')

def triangle(update, context):
    try:
        a = float(context.args[0])
        b = float(context.args[1])
        c = float(context.args[2])
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError
        area = triangle_area(a, b, c)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Площадь треугольника со сторонами {a}, {b}, {c} равна {area:.2f}.')
    except (ValueError, IndexError):
        context.bot.send_message(chat_id=update.effective_chat.id, text='Некорректные стороны треугольника.')

# Создание объекта Updater и добавление обработчиков команд бота
def main():
    updater = Updater(token='6247252845:AAEIkzgPmySjLfcq_hdDMfIzCvcnajxmEc4', use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('circle', circle))
    dispatcher.add_handler(CommandHandler('triangle', triangle))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == 'main':
    main()