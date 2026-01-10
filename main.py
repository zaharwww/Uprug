import making_circle
import runge_kutta_method
import matplotlib.pyplot as plt
import velocity_field
plt.ion()
circle = making_circle.CircleCreate(4)
circle.create_ring()
circle.create_circle(0)
circle.plot_circle()


runge_kutta = runge_kutta_method.RungeKutta(circle, 1, 0.2, 0)
print()
runge_kutta.runge_kutta(circle, 0.6, 0.6, 0)

#runge_kutta.runge_kutta_y(circle, 0.05, [], 0.5)
#runge_kutta.deformation()
#runge_kutta.trajectory()
plt.xlim(0, -30)
plt.ylim(0, -30)
plt.ioff()
plt.show()
plt.ion()
runge_kutta.runge_kutta_fast_step(circle, 0.02, 3.7, 0)
plt.xlim(0, -30)
plt.ylim(0, -30)
plt.ioff()
plt.show()

field = velocity_field.VelocityField(x_range=(-30, 2), y_range=(-30, 2), density=20)
field.plot_multiple_fields(time_list=[0, 1, 2, 3])


