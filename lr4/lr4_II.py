import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

NUMBER_OF_PIXEL = 100
K = 10

def main():
    pixels = np.random.randint(0, 255 + 1, size=(NUMBER_OF_PIXEL, 3))
    k_means_for_pixels(pixels)
    
def rand_pixel():
    pass

def pixel_bright(pix1, pix2):
    """Evaluates the proximity of pixel brightness.
    
    f_i = 30 * (Ri-R0)**2 + 59 * (Gi-G0)**2 + 11 * (Bi-B0)**2
    30, 59, 11 -- sensitivity of the human eye to 
    red, green and blue colors.

    """
    R1, G1, B1 = pix1[0], pix1[1], pix1[2]
    R2, G2, B2 = pix2[0], pix2[1], pix2[2]
    return 30 * (R1-R2)**2 + 59 * (G1-G2)**2 + 11 * (B1-B2)**2

def estimate_center(cluster):
    """Find and return mean RGB value in cluster."""
    R, G, B = 0, 0, 0
    len_cluster = len(cluster)
    for pixel in cluster:
        R += pixel[0]
        G += pixel[1]
        B += pixel[2]
    R = round(R / len_cluster)
    G = round(G / len_cluster)
    B = round(B / len_cluster)
    return [R, G, B]

def visualisation_2d(clusters):
    """Show 2D scatter of clusters."""
    k = len(clusters)
    plt.grid() 
    plt.xlabel("x")    
    plt.ylabel("y")
    for i in range(k):
        x_coordinates = []
        y_coordinates = []
        for q in range(len(clusters[i])):
            x_coordinates.append(clusters[i][q][0])
            y_coordinates.append(clusters[i][q][1])
        plt.scatter(x_coordinates, y_coordinates)
    plt.show()
    
def visualisation_3d(clusters):
    """Show 3D scatter of clusters."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(len(clusters)):
        for j in range(len(clusters[i])):
            R = clusters[i][j][0]
            G = clusters[i][j][1]
            B = clusters[i][j][2]
            ax.scatter(R, G, B, color=(R / 255, G / 255, B / 255))
    ax.set_xlabel('R')
    ax.set_ylabel('G')
    ax.set_zlabel('B')
    plt.show()
    
def k_means_for_pixels(pixels):
    """Method k-means for pixels."""
    # 1 point
    samples = random.sample(range(0, NUMBER_OF_PIXEL), K)
    centers = [pixels[s] for s in samples]
    clusters = [[]] * K
    while True:
        clusters0 = clusters[:]
        clusters = [[] for _ in range(K)]
        # 2 point
        for pixel in pixels:
            proximity = [pixel_bright(pixel, c) for c in centers]
            clusters[np.argmin(proximity)].append(pixel)
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
        if check:
            break
        visualisation_3d(clusters)
    
if __name__ == '__main__':
    main()