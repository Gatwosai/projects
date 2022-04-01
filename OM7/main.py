import random
from scipy.integrate import quad
import math

_LAMBDA = 6


def gen_random_post():
    """Генератор случайного числа по нормальному закону."""
    sum = 0.0
    for i in range(6):
        sum += random.random()
    sigma = 1 / 2**0.5
    m = 3
    x = sigma * 2**0.5 * (sum - 3) + m
    return x


def f_post(x):
    """Функция плотности распределения по нормальному закону."""
    sigma = 1 / 2**0.5
    m = 3
    y = (
        1
        / (sigma * (2 * math.pi) ** 0.5)
        * math.e ** (-((x - m) ** 2) / (2 * sigma**2))
    )
    return y


def f_post_obr(x):
    """
    Функция, обратная функции плотности распределения по нормальному закону.
    """
    sigma = 1 / 2**0.5
    m = 3
    y = math.e**(-(-m + x)**2 / 2 * sigma**2) / ((2 * math.pi)**0.5 * sigma)
    return y


def F_post(t):
    """Интервал между запросами T."""
    T, err = quad(f_post, 0, t)  # интеграл от 0 до t
    return T


def F_post_obr(t):
    """Функция, обратная F_пост. Вычисляет дельта t."""
    dt, err = quad(f_post_obr, 0, t)
    return dt


def gen_random_ob():
    """Случайная величина времени обработки по экспоненциальному закону."""
    return -1 / _LAMBDA * math.log(random.random())


def f_ob(x):
    """Функция плотности распределения обработки."""
    return _LAMBDA * math.e ** (-_LAMBDA * x)


def f_ob_obr(x):
    """Функция, обратная функции плотности распределения обработки."""
    return (-1 / _LAMBDA) * math.log(x / _LAMBDA)


def F_ob(t):
    """Сколько времени занят канал."""
    tau, err = quad(f_ob, 0, t)  # интеграл от 0 до t
    return tau


def F_ob_obr(t):
    """Функция, обратная F_об. Вычисляет тау."""
    tau, err = quad(f_post_obr, 0, t)
    return tau


def SMO():
    T = F_post(gen_random_post())

    dt = F_post_obr(gen_random_ob())


def main():
    y = f_ob(2)
    x = f_ob_obr(y)
    print(y, x)


if __name__ == "__main__":
    main()
