
from Circle import making_circle
from Trajectory import runge_kutta_method
import matplotlib.pyplot as plt
from Field_of_velocity import velocity_field
from StreamLine import streamlines

plt.ion()
circle = making_circle.CircleCreate(4)
circle.create_ring()
circle.create_circle(0)
circle.plot_circle()

runge_kutta = runge_kutta_method.RungeKutta(circle)
runge_kutta.runge_kutta(circle, 0.001, 0.7, 0)

plt.xlim(0, -40)
plt.ylim(0, -30)
plt.xlabel('X1')
plt.ylabel('X2')
plt.grid()
plt.ioff()
plt.show()
plt.ion()
runge_kutta.runge_kutta_fast_step(circle, 0.001, 0.7, 0)
plt.xlim(0, -40)
plt.ylim(0, -30)
plt.xlabel('X1')
plt.ylabel('X2')
plt.grid()
plt.ioff()
plt.show()

field = velocity_field.VelocityField(x_range=(-30, 2), y_range=(-30, 2), density=50)
field.plot_velocity_distribution(time_list=[0, 1, 2, 3])

stream = streamlines.Streamlines(x_range=(-30, 2), y_range=(-30, 2), density=50)

fig2, axes2 = stream.plot_multiple_streamlines(
    time_list=[0, 1, 2, 3],
    num_lines=1.2,
    t_end=3,
    figsize_per_plot=(5, 5)
)
plt.show()