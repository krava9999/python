import shutil
path_file = 'textFiles/books.txt'
# Функция показывает справочник


def show():
    with open(path_file, 'r', encoding='utf-8') as file:
        print(file.read())

# Функция добавление записи


def addNewUser():
    newString = input(
        'Введите данные формата: Фамилия Имя Отчество Телефон\n--> ')
    with open(path_file, 'a') as file:
        file.write(f'\n{newString}')

# Функция поиска строк по критерию


def find():
    searchString = input('Введите критерий который ищем: ')
    with open(path_file, 'r', encoding='utf-8') as file:
        for line in file:
            if searchString in line:
                print(line)


def saveFile():
    shutil.copy2(path_file, 'saves')


def deleteString():
    newLines = []
    searchDeleteString = input('Введите критерий который ищем: ')
    with open(path_file, 'r', encoding='utf-8') as file:
        for line in file:
            print(newLines)
            if searchDeleteString not in line:
                newLines.append(line)
                print(newLines)
    with open(path_file, 'w', encoding='utf-8') as file:
        for i in range(len(newLines)):
            file.write(f'{newLines[i]}')


def editString():
    newLines = []
    searchDeleteString = input('Введите критерий который ищем: ')
    with open(path_file, 'r', encoding='utf-8') as file:
        for line in file:
            if searchDeleteString not in line:
                newLines.append(line)
            else:
                newString = input(
                    'Введите данные формата: Фамилия Имя Отчество Телефон\n--> ')
                newLines.append(newString)
    with open(path_file, 'w', encoding='utf-8') as file:
        for i in range(len(newLines)):
            file.write(f'{newLines[i]}\n')
