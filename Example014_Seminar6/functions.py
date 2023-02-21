

def open_phone_book(file):
    with open(file, 'r', encoding = 'utf-8') as data:
        phone_book = data.readlines()
        print(f'Открыт файл {file}\n')
        return phone_book
    
def save_phone_book(file):
    with open('phone_book.txt', 'w', encoding = 'utf-8') as data:
        for i in file:
            data.write(i)
        print('Изменения сохранены\n')
        
def show_phone_book(file):
    print('========= Контакты =========')
    for i in file:
        print(' '.join(i.split(';')))
    print('============================')

def add_phone_book(file):
        user_info = input('Введите данные нового контакта (имя, номер, комментарий): ')
        user_info = ';'.join(user_info.split(' '))
        file.append('\n' + user_info)
        print('\nКонтакт добавлен. Не забудьте сохранить изменения\n')

def change_phone_book(file):
    user_info = input('Введите номер контакта, которого вы хотите изменить: ')
    for i in range(len(file)):
        if user_info in file[i]:
            print('\nНайден контакт:')
            print(' '.join(file[i].split(';')))
            new_user_info = input('\nВведите новый номер контакта: ')
            file[i] = file[i].replace(user_info, new_user_info)
            print('\nНомер изменён. Не забудьте сохранить изменения\n')

def search_phone_book(file):
    user_info = input('Введите номер контакта, по которому будем искать: ')
    for i in range(len(file)):
        if user_info in file[i]:
            print('\nНайден контакт:')
            print(' '.join(file[i].split(';')))
            print()

def delete_phone_book(file):
    user_info = input('Введите номер контакта, которого вы хотите удалить: ')
    for i in range(len(file)):
        if user_info in file[i]:
            print('\nНайден контакт:')
            print(' '.join(file[i].split(';')))
            check = input('\nВы действительно хотите удалить данный контакт? Если да, введите 1, если нет - нажмите Enter: \n')
            if check:
                file.pop(i)
                print('\nКонтакт удалён. Не забудьте сохранить изменения\n')
            break




def warning():
    print('Файл не открыт!\n')

def check():
    result = input('Вы действительно хотите выйти? Все несохранённые изменения будут утеряны\n'
                            'Если да, введите 1, если нет - нажмите Enter: \n')
    return result


    

            

