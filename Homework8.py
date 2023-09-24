import json

class Phonebook:
    def __init__(self, storage_file):
        self.phonebook = []
        self.storage_file = storage_file

    def load_phonebook(self):
        try:
            with open(self.storage_file, 'r') as f:
                self.phonebook = json.load(f)
        except FileNotFoundError:
            # Если файл не найден, создаем пустую записную книжку
            self.phonebook = []

    def save_phonebook(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.phonebook, f)

    def add_contact(self, name, number):
        contact = {'name': name, 'number': number}
        self.phonebook.append(contact)
        self.save_phonebook()
        print(f'Контакт {name} успешно добавлен в справочник.')

    def remove_contact(self, name):
        for contact in self.phonebook:
            if contact['name'] == name:
                self.phonebook.remove(contact)
                self.save_phonebook()
                print(f'Контакт {name} успешно удален из справочника.')
                return
        print(f'Контакт {name} не найден в справочнике.')

    def search_contact(self, name):
        found_contacts = [contact for contact in self.phonebook if contact['name'] == name]
        if len(found_contacts) > 0:
            for contact in found_contacts:
                print(f'Имя: {contact["name"]}, Номер: {contact["number"]}')
        else:
            print(f'Контакт {name} не найден в справочнике.')

    def list_contacts(self):
        if len(self.phonebook) == 0:
            print('Справочник пуст.')
        else:
            for contact in self.phonebook:
                print(f'Имя: {contact["name"]}, Номер: {contact["number"]}')

    def import_contacts(self, file_path):
        try:
            with open(file_path, 'r') as f:
                contacts = json.load(f)
                if isinstance(contacts, list):
                    self.phonebook.extend(contacts)
                    self.save_phonebook()
                    print(f'Контакты из файла {file_path} успешно импортированы в справочник.')
                else:
                    print(f'Некорректный формат файла {file_path}. Ожидался список контактов.')
        except FileNotFoundError:
            print(f'Файл {file_path} не найден.')


def main():
    storage_file = 'phonebook.json'
    phonebook = Phonebook(storage_file)
    phonebook.load_phonebook()

    while True:
        print('\nМеню:')
        print('1. Просмотреть контакты')
        print('2. Добавить контакт')
        print('3. Удалить контакт')
        print('4. Импортировать контакты из файла')
        print('5. Поиск контакта')
        print('6. Выйти')

        choice = input('Выберите действие (1-6): ')

        if choice == '1':
            phonebook.list_contacts()
        elif choice == '2':
            name = input('Введите имя: ')
            number = input('Введите номер телефона: ')
            phonebook.add_contact(name, number)
        elif choice == '3':
            name = input('Введите имя контакта, который нужно удалить: ')
            phonebook.remove_contact(name)
        elif choice == '4':
            file_path = input('Введите путь к файлу для импорта контактов: ')
            phonebook.import_contacts(file_path)
        elif choice == '5':
            name = input('Введите имя контакта, которого нужно найти: ')
            phonebook.search_contact(name)
        elif choice == '6':
            break
        else:
            print('Некорректный выбор. Попробуйте еще раз.')

    print('Завершение программы.')


if __name__ == '__main__':
    main()