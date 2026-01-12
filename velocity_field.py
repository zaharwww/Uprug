import numpy as np
import matplotlib.pyplot as plt


class VelocityField:
    def __init__(self, x_range=(-30, 2), y_range=(-30, 2), density=30):
        self.x_min, self.x_max = x_range
        self.y_min, self.y_max = y_range
        self.x = np.linspace(self.x_min, self.x_max, density)
        self.y = np.linspace(self.y_min, self.y_max, density)
        self.X, self.Y = np.meshgrid(self.x, self.y)

    def _calculate_velocity(self, t):
        u = -np.exp(t) * self.X
        v = np.exp(t) * self.Y
        return u, v

    def plot_velocity_distribution(self, time_list=[0, 1, 2, 3]):
        num_plots = len(time_list)
        fig, axs = plt.subplots(1, num_plots, figsize=(5 * num_plots, 5))
        if num_plots == 1:
            axs = [axs]
        for i, t in enumerate(time_list):
            u = -np.exp(t) * self.X
            v = np.exp(t) * self.Y
            speed = np.sqrt(u**2 + v**2)
            im = axs[i].imshow(
                speed,
                extent=[self.x_min, self.x_max, self.y_min, self.y_max],
                origin='lower',
                cmap='viridis',
                aspect='auto'
            )

            axs[i].set_title(f"Распределение скоростей\nпри t = {t:.2f}")
            axs[i].set_xlabel("x")
            axs[i].set_ylabel("y")
            fig.colorbar(im, ax=axs[i], label='Модуль скорости')

        plt.tight_layout()
        plt.show()