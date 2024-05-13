import numpy as np
import matplotlib.pyplot as plt

def plot_vectors(data):
    data = np.array(data).T
    num_vectors = data.shape[1]

    initial = np.zeros((2, num_vectors), dtype=float)
    data = np.concatenate([initial, data], axis=0)

    default = np.array([0, 1e-6, 0, 0, 'black']).reshape(-1, 1)
    data = np.concatenate([default, data], axis=1)

    c = data[4]
    data = data[:4].astype(float)
    x, y, u, v = data

    edge = 0.5
    
    right = np.max(x + u)
    if right < 0: right = 0
    right += edge
    
    left = np.min(x + u)
    if left > 0: left = 0
    left -= edge
    
    upper = np.max(y + v)
    if upper < 0: upper = 0
    upper += edge
    
    lower = np.min(y + v)
    if lower > 0: lower = 0
    lower -= edge

    fig, ax = plt.subplots()
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(1))
    ax.quiver(x, y, u, v,
        color=c,
        units='xy',
        scale=1
    )
    ax.axis('scaled')
    ax.set_xlim(left, right)
    ax.set_ylim(lower, upper)
    plt.show()