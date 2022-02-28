import numpy as np
import matplotlib.pyplot as plt


COUNT_RANDOM_NUMBERS = 60


def main():
    random1 = 0.1299824
    random2 = 0.1742435
    random_numbers = generate_random_numbers(random1, random2, COUNT_RANDOM_NUMBERS)
    expected_value, dispersion, standard_deviation = \
        (standart_parameters(random_numbers))
    print(random_numbers)
    print(expected_value)
    print(dispersion)
    print(standard_deviation)
    #plt.plot()
    #plt.show()
    khi_square(5)

def khi_square(k):
    step = 1 / k
    N = 31
    random_numbers = generate_random_numbers(
        0.1299824, 0.1742435, N)
    random_numbers = sorted(random_numbers)
    list_for_count = [[] for _ in range(k)]
    interval_boundary = step
    j = 0
    for i in range(k):
        while j < N:
            if random_numbers[j] < interval_boundary:
                list_for_count[i].append(random_numbers[j])
                j += 1
            else:
                interval_boundary += step
                break
    counters = [len(l) for l in list_for_count]
    p_i = 1 / k
    khi_exp = (sum([n ** 2 / p_i - N for n in counters]) / N)
    print(khi_exp)


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

def standart_parameters(random_numbers):
    """Calculate and return m_r, D_r, gamma_r."""
    n = len(random_numbers)
    expected_value = sum(random_numbers) / n
    dispersion = sum([(x - expected_value) ** 2 for x in random_numbers]) / n
    standard_deviation = dispersion ** 0.5
    return expected_value, dispersion, standard_deviation

if __name__ == '__main__':
    main()
