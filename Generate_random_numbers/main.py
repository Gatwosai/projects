import numpy as np
import matplotlib.pyplot as plt


COUNT_RANDOM_NUMBERS = 60
RANDOM1 = 0.1299824
RANDOM2 = 0.1742435
N = 61


def main():
    random_numbers = generate_random_numbers(
        RANDOM1, RANDOM2, COUNT_RANDOM_NUMBERS)
    expected_value, dispersion, standard_deviation = \
        (standart_parameters(random_numbers))
    print(random_numbers)
    print(expected_value)
    print(dispersion)
    print(standard_deviation)
    # FIXME
    random_numbers = generate_random_numbers(RANDOM1, RANDOM2, N)
    # FIXME
    show_frequency_test()
    khi_square_exp = khi_square(random_numbers, 5)
    # FIXME
    khi_square_t = khi_square_theory()
    # FIXME
    print_khi_square(khi_square_exp)
    # FIXME maybe
    frequency_check(random_numbers)

def frequency_check(random_numbers):
    numbers = ''
    for i in range(N):
        numbers += str(random_numbers[i])[2:]
    counters = [0 for _ in range(10)]
    for i in range(10):
        for number in numbers:
            if number == str(i):
                counters[i] += 1
    p_i = 1 / 10
    khi_exp = sum([n ** 2 / p_i - N for n in counters]) / N
    print(khi_exp)

def print_khi_square(khi_exp):
    print(khi_exp)

def khi_square_theory():
    nu = N - 1
    x_p = [-2.33, -1.64, -0.674, 0.00, 0.674, 1.64, 2.33]
    #p = "p = 1%", "p = 5%", "p = 25%", "p = 50%", "p = 75%", "p = 95%", "p = 99%"

def khi_square(random_numbers, k):
    step = 1 / k
    random_numbers = sorted(random_numbers)
    counters = [0 for _ in range(k)]
    interval_boundary = step
    j = 0
    for i in range(k):
        while j < N:
            if random_numbers[j] < interval_boundary:
                counters[i] += 1
                j += 1
            else:
                interval_boundary += step
                break
    p_i = 1 / k
    khi_exp = sum([n ** 2 / p_i - N for n in counters]) / N
    return khi_exp

def show_frequency_test():
    pass

def standart_parameters(random_numbers):
    """Calculate and return m_r, D_r, gamma_r."""
    n = len(random_numbers)
    expected_value = sum(random_numbers) / n
    dispersion = sum([(x - expected_value) ** 2 for x in random_numbers]) / n
    standard_deviation = dispersion ** 0.5
    return expected_value, dispersion, standard_deviation

def generate_random_numbers(random1, random2, count):
    """Generates a random number by the method of median products."""
    random_numbers = []
    for _ in range(count):
        tmp = random1
        random1 *= random2
        random2 = tmp
        mean = format(random1, '.10f')
        random1 = float('0.' + mean[len(mean) // 2 - 2:len(mean) // 2 + 2])
        random_numbers.append(random1)
    return random_numbers

if __name__ == '__main__':
    main()
