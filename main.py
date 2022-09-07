import re


class Person:
    __firstname = str()
    __lastname = str()
    __phone = str()

    def __init__(self, firstname: str, lastname: str, phone: str):
        self.set_firstname(firstname)
        self.set_lastname(lastname)
        self.set_phone(phone)

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_phone(self):
        return self.__phone

    def set_firstname(self, firstname: str):
        self.__firstname = firstname.capitalize()

    def set_lastname(self, lastname: str):
        self.__lastname = lastname.capitalize()

    def set_phone(self, phone: str):
        self.__phone = phone

    def __str__(self):
        return f'{self.__firstname} {self.__lastname} {self.__phone}'

    def to_file(self, filename: str):
        with open(filename, 'a') as file:
            file.write(self.__str__() + '\n')

    @staticmethod
    def from_file(filename: str):
        with open(filename, 'r') as file:
            res = file.readline().split()
            for line in file:
                return Person(res[0], res[1], res[2])


class Student(Person):
    __group = str()

    def __init__(self, firstname: str, lastname: str, phone: str, group: str):
        super().__init__(firstname, lastname, phone)
        self.set_group(group)

    def get_group(self):
        return self.__group

    def set_group(self, group: str):
        self.__group = group

    def __str__(self):
        return f'{super().__str__()} {self.__group}'

    @staticmethod
    def from_file(filename: str):
        with open(filename, 'r') as file:
            res = file.readline().split()
            if re.search(r'\d', res[3]):
                return Student(res[0], res[1], res[2], res[3])


class Teacher(Person):
    __subject = str()
    __teacher_list = list()

    def __init__(self, firstname: str, lastname: str, phone: str, subject: str):
        super().__init__(firstname, lastname, phone)
        self.set_subject(subject)

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject: str):
        self.__subject = subject

    def set_teacher_list(self, teacher_list: list):
        self.__teacher_list = teacher_list

    def __str__(self):
        return f'{super().__str__()} {self.__subject}'

    @staticmethod
    def from_file(filename: str):
        with open(filename, 'r') as file:
            res = file.readline().split()
            if re.search(r'\D+', res[3]):
                return Teacher(res[0], res[1], res[2], res[3])
            else:
                return file.readline()


li = []

li.append(Teacher('Olena', 'Polozova', '+380962356856', 'English'))
li.append(Student('Ivasyk', 'Bulkin', 'trinolyatrulyalya', 'Python11'))
li.append(Student('Grigoiy', 'Terkin', '+387415874165', 'Python21'))
li.append(Student('Anna', 'Chechetkina', '+04478451235', 'C++14'))
li.append(Student('Svetlana', 'Bulkina', 'trinolyatrulyalya2', 'Python11'))
li.append(Student('Anatloiy', 'Fedorov', '0991234756', 'C++17'))
li.append(Teacher('Fedor', 'Fedorov', '+380658392434', 'Math'))
li.append(Teacher('Oleksandr', 'Titarenko', '+380769456382', 'Physics'))


# for i in range(len(li)):
#     li[i].to_file('test.txt')
