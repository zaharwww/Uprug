import numpy as np
import matplotlib.pyplot as plt


class Streamlines:
    def __init__(self, x_range, y_range, density=30):
        self.x_range = x_range
        self.y_range = y_range
        x = np.linspace(x_range[0], x_range[1], density)
        y = np.linspace(y_range[0], y_range[1], density)
        self.X, self.Y = np.meshgrid(x, y)

    def _get_velocity(self, t):
        U = -np.exp(t) * self.X
        V = np.exp(t) * self.Y
        return U, V

    def plot_streamlines(self, time, num_lines=1.0, t_end=None):
        fig, ax = plt.subplots(figsize=(6, 6))
        U, V = self._get_velocity(time)
        density_val = num_lines if num_lines < 5 else num_lines / 10.0
        st = ax.streamplot(self.X, self.Y, U, V, density=density_val, color='teal', arrowsize=1.5)
        ax.set_title(f"Линии тока при t = {time}")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_xlim(self.x_range)
        ax.set_ylim(self.y_range)
        ax.grid(True)
        return fig, ax

    def plot_multiple_streamlines(self, time_list, num_lines=1.0, t_end=None, figsize_per_plot=(5, 5)):
        n = len(time_list)
        fig, axes = plt.subplots(1, n, figsize=(figsize_per_plot[0] * n, figsize_per_plot[1]))
        if n == 1:
            axes = [axes]
        density_val = num_lines if num_lines < 5 else num_lines / 10.0
        for i, t in enumerate(time_list):
            U, V = self._get_velocity(t)
            axes[i].streamplot(self.X, self.Y, U, V, density=density_val, color='purple', arrowsize=1)
            axes[i].set_title(f"Линии тока, t = {t}")
            axes[i].set_xlabel("X")
            axes[i].set_ylabel("Y")
            axes[i].set_xlim(self.x_range)
            axes[i].set_ylim(self.y_range)
            axes[i].grid(True)
        plt.tight_layout()
        return fig, axes