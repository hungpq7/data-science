import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

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

def plot_pp(var, dist):
    var = var.flatten()
    n = len(var)
    pe = (np.arange(1, n+1)-0.5) / n
    pp = np.sort(dist.cdf(var))
    
    fig, ax = plt.subplots(ncols=2, figsize=(10,4), tight_layout=True)
    
    ax[0].plot(np.linspace(0,1), np.linspace(0,1), 'grey')
    ax[0].plot(pe, pp, 'o', color='steelblue', alpha=0.5)
    ax[0].axis('scaled')
    ax[0].set_xlabel('Observed variable')
    ax[0].set_ylabel('Theoretical distribution')
    ax[0].set_title('P-P Plot')
    
    ax[1] = sns.histplot(var, edgecolor='w', kde=True)
    ax[1].set_title('Histogram')
    
    plt.show()

def plot_qq(var, dist):
    # var = stats.zscore(var)
    var = np.sort(var)
    n = var.size
    cut = np.linspace(0, 1, n-1)
    quantile_var = np.quantile(var, q=cut)
    quantile_dist = [stats.norm.ppf(q) for q in cut]
    
    fig, ax = plt.subplots(ncols=2, figsize=(10,4), tight_layout=True)
    
    ax[0].plot(quantile_dist, quantile_dist, 'grey')
    ax[0].plot(quantile_var, quantile_dist, 'o', color='steelblue')
    ax[0].axis('scaled')
    ax[0].set_title('Q-Q Plot')
    ax[0].set_xlabel('Observed quantile')
    ax[0].set_ylabel('Theoretical quantile')
    
    ax[1] = sns.histplot(var, kde=True, edgecolor='w')
    ax[1].set_title('Histogram')
    
    plt.show()