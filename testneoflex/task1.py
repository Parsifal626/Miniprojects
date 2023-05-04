"""
Извлеките доменное имя из URL-адреса
Необходимо написать функцию, которая при задании URL адреса в виде строки анализирует
только доменное имя и возвращает его в виде строки.
Пример вывода функции:
url = "http://github.com/carbonfive/raygun" -> domain name = "github"
url = "http://www.zombie-bites.com" -> domain name = "zombie-bites"
url = "https://www.cnet.com" -> domain name = cnet
"""


# Определяем функцию get_domain_name
def get_domain_name():
    # Получаем URL-адрес от пользователя
    url = input("Введите URL-адрес: ")
    # Устанавливаем протокол для определения начала доменного имени
    protocol = "://"
    # Определяем начало доменного имени
    domain_start = url.find(protocol) + len(protocol)
    # Определяем конец доменного имени
    domain_end = url.find("/", domain_start)
    # Если конец доменного имени не найден, устанавливаем его в конец URL-адреса
    if domain_end == -1:
        domain_end = len(url)
    # Извлекаем доменное имя
    domain_name = url[domain_start:domain_end].split(".")[-2]
    # Возвращаем доменное имя
    return domain_name

if "__main__" == __name__:

    print(get_domain_name())