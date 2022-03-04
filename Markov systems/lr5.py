import numpy as np
import matplotlib.pyplot as plt


A = np.array(
    [
        [-9, 3, 0, 1, 2],
        [7, -7, 8, 6, 0],
        [2, 0, -14, 0, 9],
        [0, 0, 4, -7, 5],
        [0, 4, 2, 0, -16],
    ]
)
H = 0.01


def main():
    euler_method()
    A[4] = 1
    B = np.array([0, 0, 0, 0, 1])
    solution = np.linalg.solve(A, B)
    print("Предельные вероятности системы:")
    print(solution)


def euler_method():
    E = np.eye(len(A))
    h = H
    k = 50
    P = [np.array([1, 0, 0, 0, 0])]
    t = [0]
    for i in range(k):
        P.append(np.dot((E + h * A), P[i]))
        t.append(t[i] + i * h)
    P = np.array(P)
    plt.plot(t, P[:, 0], t, P[:, 1], t, P[:, 2], t, P[:, 3], t, P[:, 4])
    plt.legend(["p1", "p2", "p3", "p4", "p5"])
    plt.show()


if __name__ == "__main__":
    main()
