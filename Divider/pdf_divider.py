import os
from tkinter import Tk, filedialog
from PyPDF2 import PdfReader, PdfWriter

# Создаем графический интерфейс для выбора файла
root = Tk()
root.withdraw()
input_pdf_path = filedialog.askopenfilename()

# Создаем объект PdfFileReader, который считывает содержимое PDF-файла
pdf_reader = PdfReader(input_pdf_path)

# Получаем количество страниц в PDF-файле
num_pages = len(pdf_reader.pages)

# Создаем объект PdfFileWriter, который будет записывать отдельные страницы в файлы
pdf_writer = PdfWriter()

# Проходимся по каждой странице в PDF-файле
for page_num in range(num_pages):
    # Получаем объект страницы по ее номеру
    page = pdf_reader.pages[page_num]

    # Добавляем страницу в объект PdfFileWriter
    pdf_writer.add_page(page)

    # Определяем путь к файлу, куда будем сохранять текущую страницу
    output_file_path = os.path.splitext(input_pdf_path)[0] + '_page{}.pdf'.format(page_num+1)

    # Создаем файл и записываем в него текущую страницу
    with open(output_file_path, 'wb') as output_file:
        pdf_writer.write(output_file)

    # Очищаем объект PdfFileWriter для записи следующей страницы
    pdf_writer = PdfWriter()

# Выводим количество полученных страниц
print('Количество полученных страниц: {}'.format(num_pages))

# Завершаем программу
input('Нажмите Enter, чтобы закрыть программу...')
