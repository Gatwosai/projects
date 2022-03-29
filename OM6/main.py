"""
Станция автосервиса использует систему двухканальной очереди (два канала
обслуживания (два автомеханика) и очередь из двух машин). Прибытие машин распределено
по закону Пуассона со средней скоростью прибытия 6 машин в час. Время обслуживания
распределено экспоненциально со средней скоростью обслуживания 1,2 машины в час для
каждого из каналов. Если вновь прибывшая машина застает ситуацию, что все каналы
заняты, и в очереди нет мест, то она покидает станцию автосервиса. Число мест в очереди 5.
1. Какова вероятность того, что в системе нет машин?
2. Каково среднее число машин в очереди?
3. Каково среднее время ожидания обслуживания?
4. Каково среднее время пребывания в системе?
5. Какова вероятность того, что вновь прибывшей машине придется ждать?
Считая, что клиент в среднем приносит станции автосервиса 8000 руб., а зарплата
автомеханика в месяц (22 рабочих дня, в день 8 часов) 75000 руб., определить выгодно для
станции автосервиса нанять еще одного или двух автомехаников. Предполагается, что
стоимость издержек станции автосервиса не считая зарплат в месяц составляет 250000 руб.,
60% от выручки за месяц остается у владельца станции автосервиса.
"""


def geom_prog(n, m, ro):
    """Геометрическая прогрессия со знаменателем (ro / n). Расчет p0."""
    sum = 1
    for i in range(1, n + 1):
        sum += ro**i / fact(i)
    sum += ro**n / fact(n) * ((ro / n - (ro / n) ** (m + 1)) / (1 - ro / n))
    return sum**-1


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


def car_service(n, m, _lambda, mu):
    """Расчет значений по заданию."""
    t_ob = 1 / mu
    ro = _lambda / mu
    gamma = ro / n
    p0 = geom_prog(n, m, ro)
    p_otk = ro ** (n + m) / (n**m * fact(n)) * p0
    q = 1 - p_otk
    A = _lambda * q
    r = ((ro ** (n + 1) * p0) / (n * fact(n))) * (
        (1 - (m + 1) * gamma**m + m * gamma ** (m + 1)) / (1 - gamma) ** 2
    )
    t_ob_sr = q * t_ob
    t_oj = r / _lambda
    t_sist = t_oj + q * t_ob
    p = 1 - (p0 + ro * p0)
    return ro, gamma, p0, p_otk, q, A, r, t_ob_sr, t_sist, p


def profit(n):
    """Расчет прибыли. Зависит от количества автомехаников n"""
    ro, gamma, p0, p_otk, q, A, r, t_ob_sr, t_sist, p = car_service(
        n, m, _lambda, mu)
    income = 8000 * A * 8 * 22  # 8000 за машину, А - машин в час, 8 часов 22 дня
    income = income * 0.6  # 60% остается владельцу
    costs = 75000 * n + 250000  # 75к зарплаты, 250000 на авточасти
    _profit = income - costs
    print(
        "Прибыль для владельца, если иметь %d автомехаников: %d рублей" % (
            n, _profit)
    )
    return _profit


n = 2
m = 5
_lambda = 6
mu = 1.2
ro, gamma, p0, p_otk, q, A, r, t_ob_sr, t_sist, p = car_service(
    n, m, _lambda, mu)

print(
    "Входные данные: n=%d, m=%d, λ=%d, μ=%.1f, ρ=%.1f, γ=%.1f"
    % (n, m, _lambda, mu, ro, gamma)
)
print("Вероятность что все каналы свободны = ", round(p0 * 100, 5), "%", sep="")
print("Вероятность отказа = ", round(p_otk * 100, 2), "%", sep="")
print("Относительная пропускная способность = ", round(q * 100, 2), "%", sep="")
print("Абсолютная пропускная способность = ",
      round(A, 3), " машины в час", sep="")
print(
    "Какова вероятность того, что в системе нет машин?\n",
    round(p0 * 100, 5),
    "%",
    sep="",
)
print("Каково среднее число машин в очереди?\n", round(r, 3), sep="")
print(
    "Каково среднее время ожидания обслуживания?\n",
    round(t_ob_sr * 60, 2),
    " минут",
    sep="",
)
print(
    "Каково среднее время пребывания в системе?\n",
    round(t_sist * 60, 2),
    " минут",
    sep="",
)
print(
    "Какова вероятность того, что вновь прибывшей машине придется ждать?\n",
    round(p * 100, 2),
    "%",
    sep="",
)

p1 = profit(2)
p2 = profit(3)
p3 = profit(4)
if p1 < p2:
    print("Вывод: выгодно нанять еще автомехаников")
