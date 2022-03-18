import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

PATH_OF_FILE = "/home/gasai/Документы/учеба/ИИ/projects/lr4/naruto.jpg"
K = 10


def main():
    global K
    while True:
        input_k = input("Ввод количества цветов: ")
        if input_k.isdigit() is True:
            if int(input_k) > 0:
                break
        print("Неверный ввод, ожидалось число большее 0")
    K = int(input_k)
    show_images()


def show_images():
    """Shows uploaded and converted image."""
    with cbook.get_sample_data(PATH_OF_FILE) as image_file:
        image = plt.imread(image_file)
    plt.figure(1)
    plt.title("Начальное изображение")
    plt.imshow(image)
    plt.figure(2)
    plt.title("Преобразованное изображение")
    plt.imshow(k_means_for_image(image))
    plt.show()


def pixel_bright(pix1, pix2):
    """Evaluates the proximity of pixel brightness.

    f_i = 30 * (Ri-R0)**2 + 59 * (Gi-G0)**2 + 11 * (Bi-B0)**2
    30, 59, 11 -- sensitivity of the human eye to
    red, green and blue colors.

    """
    R1, G1, B1 = int(pix1[0]), int(pix1[1]), int(pix1[2])
    R2, G2, B2 = int(pix2[0]), int(pix2[1]), int(pix2[2])
    return 30 * (R1 - R2) ** 2 + 59 * (G1 - G2) ** 2 + 11 * (B1 - B2) ** 2


def estimate_center(cluster):
    """Find and return mean RGB value in cluster."""
    R, G, B = 0, 0, 0
    len_cluster = len(cluster) if len(cluster) > 0 else 1
    for pixel in cluster:
        R += pixel[0]
        G += pixel[1]
        B += pixel[2]
    R = round(R / len_cluster)
    G = round(G / len_cluster)
    B = round(B / len_cluster)
    return [R, G, B]


def k_means_for_image(image):
    """Method k-means for pixels."""
    # 1 point
    samples_x = random.sample(range(0, image.shape[0]), K)
    samples_y = random.sample(range(0, image.shape[0]), K)
    centers = [image[x][y] for x, y in zip(samples_x, samples_y)]
    clusters = [[]] * K
    new_image = image[:]
    i = 0
    while i < 20:
        i += 1
        clusters0 = clusters[:]
        clusters = [[] for _ in range(K)]
        # 2 point
        for i in range(len(image)):
            for j in range(len(image[i])):
                proximity = [pixel_bright(image[i][j], c) for c in centers]
                clusters[np.argmin(proximity)].append(image[i][j])
                new_image[i][j] = centers[np.argmin(proximity)]
        # 3 point
        for i in range(K):
            centers[i] = estimate_center(clusters[i])
        # 4 point
        check = True
        for i in range(len(clusters)):
            for j in range(len(clusters[i])):
                if len(clusters0[i]) != len(clusters[i]):
                    check = False
                    break
                for k in range(len(clusters[i][j])):
                    if clusters[i][j][k] != clusters0[i][j][k]:
                        check = False
                        break
        if check:
            break
    return new_image


if __name__ == "__main__":
    main()
