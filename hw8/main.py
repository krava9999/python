# Открываем файл относительно нашего main файла проекта в папке books.
# Заменить на путь
import act
while (True):
    action = input(
        'Введите необходимое действие:'
        '\n1. Add - Добавить запись'
        '\n2. Show - показать справочик'
        '\n3. find - Поиск записей'
        '\n4. Save - Сохранить Файл в папку save'
        '\n5. Del - Удалить строку по критерию'
        '\n6. Edit - Изменить строку по критерию'
        '\n0. 0 - Завершить программу\n-> ').upper()
    if action == '0':
        break
    elif action == 'ADD':
        act.addNewUser()
    elif action == 'SHOW':
        act.show()
    elif action == 'FIND':
        act.find()
    elif action == 'SAVE':
        act.saveFile()
    elif action == 'DEL':
        act.deleteString()
    elif action == 'EDIT':
        act.editString()
