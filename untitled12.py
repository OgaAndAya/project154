import matplotlib.pyplot as plt
data = [
    [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 6,12,12,12],
    [12, 12, 12, 12, 12, 12, 12, 12, 12, 10, 7,6,12,12],
    [12, 12, 12, 12, 12, 12, 12, 12, 10, 10, 10,7,6,12],
    [12, 12, 12, 12, 12, 12, 12, 10, 10, 1, 10,10,7,6],
    [12, 12, 12, 12, 12, 12, 10, 10, 10, 10, 10,10,7,6],
    [12, 12, 12, 12, 12, 10, 10, 10, 10, 1, 10,10,7,6],
    [12, 12, 12, 12, 10, 10, 10, 10, 10, 10, 10,7,6,6],
    [12, 12, 12, 10, 10, 10, 10, 1, 10, 10, 10,7,6,6],
    [12, 12, 10, 1, 10, 1, 10, 10, 10, 10, 7,6,6,12],
    [12, 6, 7, 10, 10, 10, 10, 10, 10, 10, 7,6,12,12],
    [12, 12, 6, 7, 7, 7, 7, 7, 7, 7, 6,12,12,12],
    [12, 12, 12, 6, 6, 6, 6, 6, 6, 6, 12,12,12,12]
]
plt.imshow(data, cmap="nipy_spectral")
plt.show()
