import numpy as np
import matplotlib.pyplot as plt

def generate_points(n, max_distance):
    distances = np.random.uniform(0, max_distance, n)
    angles = np.random.uniform(0, 2 * np.pi, n)
    
    x = distances * np.cos(angles)
    y = distances * np.sin(angles)
    
    probabilities = 1 / np.sqrt(distances + 1e-8)
    probabilities /= probabilities.sum()
    
    return x, y, probabilities

def plot_points(x, y, probabilities, max_distance, title='Points with Probability Proportional to 1/sqrt(Distance)'):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(x, y, s=50, c=probabilities, cmap='viridis', alpha=0.7)
    ax.set_xlim([-1.1 * max_distance, 1.1 * max_distance])
    ax.set_ylim([-1.1 * max_distance, 1.1 * max_distance])
    ax.set_aspect('equal')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(title)
    
    fig.colorbar(ax.collections[0], label='Probability')
    plt.show()

def main(n=100, max_distance=10, title='Points with Probability Proportional to 1/sqrt(Distance)'):
    x, y, probabilities = generate_points(n, max_distance)
    plot_points(x, y, probabilities, max_distance, title)

if __name__ == "__main__":
    main()
