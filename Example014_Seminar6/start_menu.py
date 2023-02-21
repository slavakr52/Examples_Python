from functions import *

def print_menu():
    print('Это телефонный справочник. Выберите действие, которое нужно совершить:\n'
        '1. Открыть файл\n'
        '2. Сохранить изменения\n'
        '3. Показать контакты\n'
        '4. Добавить контакт\n'
        '5. Изменить номер контакта\n'
        '6. Найти контакт\n'
        '7. Удалить контакт\n'
        '8. Выход')
    data = int(input('Введите номер необходимого действия: '))
    print()
    return data

def main_start(main_file = 'phone_book.txt'):
    opened_file = None
    while True:
        user_choice = print_menu()
        match user_choice:
            case 1:
                opened_file = open_phone_book(main_file)
            case 2:
                if opened_file == None:
                    warning()
                else: save_phone_book(opened_file)
            case 3:
                if opened_file == None:
                    warning()
                else: show_phone_book(opened_file)
            case 4:
                if opened_file == None:
                    warning()
                else: add_phone_book(opened_file)
            case 5:
                if opened_file == None:
                    warning()
                else: change_phone_book(opened_file)
            case 6:
                if opened_file == None:
                    warning()
                else: search_phone_book(opened_file)
            case 7:
                if opened_file == None:
                    warning()
                else: delete_phone_book(opened_file)
            case 8:
                exit = check()
                if exit:
                    print('Выход...')
                    break

