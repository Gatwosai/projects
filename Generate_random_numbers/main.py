import matplotlib.pyplot as plt


RANDOM1 = 0.6299
RANDOM2 = 0.8742
COUNT_NUMBERS = 201


def main():
    random_numbers = generate_random_numbers(RANDOM1, RANDOM2, COUNT_NUMBERS)
    m, D, sigma = standart_parameters(random_numbers)
    print("Случайные числа:", str(random_numbers[:10])[1:-1], "...")
    print("Математическое ожидание =", m)
    print("Дисперсия =", D)
    print("Среднеквадратичное отклонение =", sigma)
    show_frequency_test(random_numbers, m, sigma)
    uniformity_check(random_numbers, 5)
    # FIXME add output
    frequency_check(random_numbers)
    # FIXME add output
    series_check(random_numbers, 5)


def generate_random_numbers(random1, random2, count):
    """Generates a random number by the method of median products."""
    random_numbers = []
    for _ in range(count):
        tmp = random1
        random1 *= random2
        random2 = tmp
        mean = format(random1, ".8f")
        random1 = float("0." + mean[4:-2])
        random_numbers.append(random1)
    return random_numbers


def standart_parameters(random_numbers):
    """Calculate and return m_r, D_r, sigma_r."""
    n = len(random_numbers)
    expected_value = sum(random_numbers) / n
    dispersion = sum([(x - expected_value) ** 2 for x in random_numbers]) / n
    standard_deviation = dispersion**0.5
    return expected_value, dispersion, standard_deviation


def show_frequency_test(random_numbers, m, sigma):
    numbers = sorted(random_numbers)
    x1 = [n for n in numbers if n < m - sigma]
    x2 = [n for n in numbers if n > m - sigma and n < m + sigma]
    x3 = [n for n in numbers if n > m + sigma]
    freq1 = len(x1)
    freq2 = len(x2)
    freq3 = len(x3)
    plt.xticks([0, m - sigma, m, m + sigma, 1])
    plt.fill_between(x1, freq1, color="yellow")
    plt.fill_between(x2, freq2)
    plt.fill_between(x3, freq3, color="yellow")
    persent1 = len(x1) / (len(x1) + len(x2) + len(x3)) * 100
    persent2 = len(x2) / (len(x1) + len(x2) + len(x3)) * 100
    persent3 = len(x3) / (len(x1) + len(x2) + len(x3)) * 100
    plt.text(0.1, 5, str(round(persent1, 2)) + "%")
    plt.text(m, 10, str(round(persent2, 2)) + "%")
    plt.text(0.9, 5, str(round(persent3, 2)) + "%")
    plt.show()


def uniformity_check(random_numbers, k):
    N = len(random_numbers)
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
    khi_exp = sum([n**2 / p_i - N for n in counters]) / N
    conclusion_khi_square(N, khi_exp, "случайности равномерного генератора")


def calc_theory(N):
    nu = N - 1
    x_p_list = [-2.33, -1.64, -0.674, 0.00, 0.674, 1.64, 2.33]
    khi_list = []
    for x_p in x_p_list:
        khi0 = nu + ((2 * nu) ** 0.5) * x_p + 2 / 3 * (x_p**2) - 2 / 3
        khi_list.append(khi0)
    return khi_list


def conclusion_khi_square(N, khi_square_exp, hypothesis):
    theory_list = calc_theory(N)
    theory_list = [round(t, 2) for t in theory_list]
    p = ["1%", "5%", "25%", "50%", "75%", "95%", "99%"]
    print(str(p)[1:-1].replace("'", ""))
    print(str(theory_list)[1:-1])
    choose = 0
    if khi_square_exp < theory_list[0]:
        choose = 0
    for i in range(len(theory_list)):
        if khi_square_exp > theory_list[i]:
            choose = p[i]
    if khi_square_exp > theory_list[-1]:
        choose = 1
    match(str(type(choose))):
        case "<class 'int'>":
            print("Гипотеза о", hypothesis, "не выполняется")
        case "<class 'str'>":
            print(
                "Гипотеза о",
                hypothesis,
                "выполняется с вероятностью",
                choose,
            )


def frequency_check(random_numbers):
    N = len(random_numbers)
    numbers = ""
    for i in range(N):
        numbers += str(random_numbers[i])[2:]
    counters = [0 for _ in range(10)]
    for i in range(10):
        for j in range(N):
            if numbers[j] == str(i):
                counters[i] += 1
    p_i = 1 / 10
    khi_exp = sum([n**2 / p_i - N for n in counters]) / N
    conclusion_khi_square(N, khi_exp, "статистической независимости частот")


def series_check(random_numbers, max_series):
    N = len(random_numbers)
    numbers = ""
    for i in range(N):
        numbers += str(random_numbers[i])[2:]
    counters = [0 for _ in range(max_series)]
    series = 0
    tmp = numbers[i]
    for i in range(1, N):
        if tmp == numbers[i]:
            series += 1
        elif series > max_series:
            tmp = numbers[i]
            series = 0
        else:
            counters[series] += 1
            tmp = numbers[i]
            series = 0
    N = sum(counters)
    p_L = [0 for _ in range(max_series)]
    for i in range(max_series):
        chance = 0.9 * 0.1**i
        p_L[i] = chance
    khi_exp = sum([n**2 / p_i - N for n, p_i in zip(counters, p_L)]) / N
    conclusion_khi_square(N, khi_exp, "статистической независимости серий")


if __name__ == "__main__":
    main()
