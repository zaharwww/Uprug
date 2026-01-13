import numpy as np
import matplotlib.pyplot as plt


class VelocityField:
    def __init__(self, x_range, y_range, density=20):
        self.x_range = x_range
        self.y_range = y_range
        self.density = density

    def plot_multiple_fields(self, time_list):
        n = len(time_list)
        fig, axes = plt.subplots(1, n, figsize=(5 * n, 5))

        if n == 1:
            axes = [axes]

        x = np.linspace(self.x_range[0], self.x_range[1], self.density)
        y = np.linspace(self.y_range[0], self.y_range[1], self.density)
        X, Y = np.meshgrid(x, y)

        for i, t in enumerate(time_list):
            U = - np.exp(t) * X
            V = np.exp(t) * Y

            axes[i].quiver(X, Y, U, V, color='blue', alpha=0.6)
            axes[i].set_title(f"Поле при t = {t}")
            axes[i].set_xlabel("X")
            axes[i].set_ylabel("Y")
            axes[i].grid(True)
            axes[i].set_aspect('equal')

        plt.tight_layout()
        plt.show()