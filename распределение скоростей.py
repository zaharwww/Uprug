import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Параметры распределения
mean_velocity = 50  # средняя скорость (м/с)
std_velocity = 15   # стандартное отклонение (м/с)
num_particles = 1000  # количество частиц

# Генерация скоростей
velocities = np.random.normal(mean_velocity, std_velocity, num_particles)

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(velocities, bins=30, density=True, alpha=0.7, color='blue', edgecolor='black')

# Теоретическая кривая
x = np.linspace(min(velocities), max(velocities), 100)
pdf = norm.pdf(x, mean_velocity, std_velocity)
plt.plot(x, pdf, 'r-', linewidth=2, label=f'Теоретическое\nμ={mean_velocity}, σ={std_velocity}')

plt.xlabel('Скорость (м/с)', fontsize=12)
plt.ylabel('Плотность вероятности', fontsize=12)
plt.title('Нормальное распределение скоростей', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Статистики
print(f"Средняя скорость: {np.mean(velocities):.2f} м/с")
print(f"Стандартное отклонение: {np.std(velocities):.2f} м/с")
print(f"Минимальная скорость: {np.min(velocities):.2f} м/с")
print(f"Максимальная скорость: {np.max(velocities):.2f} м/с")