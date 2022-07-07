# 9 причин использовать dataclasses в Python
# https://habr.com/ru/company/otus/blog/650257/
# оф библиотека dataclasses https://docs.python.org/3/library/dataclasses.html

# Исключение raise NotImplementedError должно подниматься методами
# пользовательских базовых классов
# как индикатор того, что наследникам требуется переопределить такие методы

# https://pythonz.net/references/named/notimplementederror/

# self.__class__.__name__, - https://russianblogs.com/article/32772219698/

# Именование в Python — как выбирать имена и почему это важно
# https://pythonchik.ru/osnovy/imenovanie-v-python

# 9 причин использовать dataclasses в Python
# 1 – Меньше кода для определения класса
class Person():
    def __init__(self, first_name, last_name, age, job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job

# Вот так выглядит предыдущий код с использованием dataclasses:


from dataclasses import dataclass


@dataclass
class Person1:
    first_name: str
    last_name: str
    age: int
    job: str

# В синтаксисе нужно обратить внимание на несколько моментов:
# - Получилось меньше шаблонного кода: мы определяем каждый атрибут один раз и не повторяемся.
# - Мы используем аннотацию типов для каждого атрибута.
# Хотя она и не позволяет проверять типы принудительно,
# но помогает вашему текстовому редактору обеспечивать лучшую компоновку,
# если вы используете средство проверки типов, как mypy, например.

# 2 – Поддержка значений по умолчанию


@dataclass
class Person2:
    first_name: str = "Ahmed"
    last_name: str = "Besbes"
    age: int = 30
    job: str = "Data Scientist"


ahmed = Person2()
print(ahmed)
# Помните о том, что поля без значений по умолчанию не могут стоять
# после полей со значениями по умолчанию.

# 3 – Кастомное представление объектов
# Благодаря методу repr Представление можно переопределить
# для вывода любого кастомного сообщения, которое вам может понадобиться.


@dataclass
class Person3:
    first_name: str = "Ahmed"
    last_name: str = "Besbes"
    age: int = 30
    job: str = "Data Scientist"

    def __repr__(self):
        return f"{self.first_name} {self.last_name} ({self.age})"


ahmed3 = Person3()
print(ahmed3)

# 4 – Упрощенная конвертация в кортеж или словарь
# Экземпляры можно легко сериализовать в словари или кортежи.
# Механика оказывается полезной, когда ваш код взаимодействует
# с другими программами, которые ожидают именно эти типы.

from dataclasses import asdict, dataclass

ahmed4 = Person2()

print("{}'s {} age is: {} and {}".format(*asdict(ahmed4).values()))
# {'first_name': 'Ahmed',
# 'last_name': 'Besbes',
# 'age': 30,
# 'job': 'Data Scientist'}
