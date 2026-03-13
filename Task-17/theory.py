with open('путь до файла') as file:
    # Считывает весь файл. Возвращает str
    data = file.read()
    # Считывает одну строку до символа \n. Возвращает str
    data = file.readline()
    # Считывает все строки. Возвращает list[str]
    data = file.readlines()