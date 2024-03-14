from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def is_valid(self):
        return len(self.value) == 10


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)

        if phone.is_valid() and not self.find_phone(phone_number):
            self.phones.append(phone)

    def remove_phone(self, phone_number):
        self.phones = [item for item in self.phones if item.value != phone_number]

    def edit_phone(self, old_number, new_number):
        found_phone = self.find_phone(old_number)

        if found_phone:
            found_phone.value = new_number

    def find_phone(self, phone_number):
        return next(item for item in self.phones if item.value == phone_number)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record():
        pass

    def find():
        pass

    def delete():
        pass
