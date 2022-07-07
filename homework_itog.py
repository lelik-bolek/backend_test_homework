from dataclasses import asdict, dataclass
from typing import Dict, Type

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


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    message: str = ('Тип тренировки: {}; '
                    'Длительность: {:.3f} ч.; '
                    'Дистанция: {:.3f} км; '
                    'Ср. скорость: {:.3f} км/ч; '
                    'Потрачено ккал: {:.3f}.')

    def get_message(self) -> str:
        return self.message.format(*asdict(self).values())
    # Можно было передать, как  **asdict(self), при этом заменить
    # позиционный способ форматирования в строке на именованный, как в словаре.


class Training:
    """Базовый класс тренировки."""

    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    MIN: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        return (self.action * self.LEN_STEP) / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError('Определите def get_spent_calories в'
                                  f'{self.__class__.__name__}.')
    # Есть еще написание имени класса чуть по короче type(self).name

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        return InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories()
                           )


class Running(Training):
    """Тренировка: бег."""

    run_coeff_1: int = 18
    run_coeff_2: int = 20
    # Коэффициенты лучше писать заглавными буквами.

    def get_spent_calories(self) -> float:
        """Переопределяет метод расчета колорий, для Running."""

        return (self.run_coeff_1 * self.get_mean_speed()
                - self.run_coeff_2) * self.weight / self.M_IN_KM * (
                    self.duration * self.MIN)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    sw_coeff_1: float = 0.035
    sw_coeff_2: float = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Переопределяет метод расчета колорий для SportsWalking."""

        return (self.sw_coeff_1 * self.weight + (
                self.get_mean_speed()**2 // self.height
                ) * self.sw_coeff_2 * self.weight) * (
                    self.duration * self.MIN)


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38
    swim_coeff_1: float = 1.1
    swim_coeff_2: int = 2

    def __init__(self, action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Переопределить метод расчета средней скорости для Swimming."""

        return ((self.length_pool * self.count_pool)
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Переопределить метод расчета калорий для Swimming."""

        return ((self.get_mean_speed() + self.swim_coeff_1)
                * self.swim_coeff_2 * self.weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""

    # Название переменной не должно содержать название типа.
    dict_gadget: Dict[str, Type[Training]] = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    try:
        if workout_type in dict_gadget:
            return dict_gadget[workout_type](*data)
    except ValueError as ve:
        print('ValueError', ve)


def main(training: Training) -> None:
    """Главная функция."""

    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
