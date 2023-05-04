def generate_hashtag(s):
    # Проверяем, что входная строка не пустая
    if not s:
        return False
    # Разбиваем строку на слова, убираем пробелы по бокам и приводим первую букву каждого слова к верхнему регистру
    words = s.strip().split()
    if not words:
        return False
    hashtag = '#' + ''.join(word.capitalize() for word in words)
    # Проверяем, что длина хэштега не превышает 140 символов
    if len(hashtag) > 140:
        return False
    return hashtag

if __name__ == '__main__':
    user_input = input('Введите фразу для генерации хэштега: ')
    hashtag = generate_hashtag(user_input)
    if hashtag:
        print('Сгенерированный хэштег:', hashtag)
    else:
        print('Не удалось сгенерировать хэштег')
