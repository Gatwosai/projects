import random
import math
_LAMBDA = 6


def main():
    print(gen_random())


def density_distr():
    return []


def gen_random():
    return -1 / _LAMBDA * math.log(random.random())


if __name__ == "__main__":
    main()
