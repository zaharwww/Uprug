import making_circle
import runge_kutta_method
import matplotlib.pyplot as plt
plt.ion()
circle = making_circle.CircleCreate(4)
circle.create_ring()
circle.create_circle(10000)
circle.plot_circle()


runge_kutta = runge_kutta_method.RungeKutta(circle, 1, 0.05)
print()
runge_kutta.runge_kutta_x(circle, 0.05, [], 1)
#runge_kutta.runge_kutta_y(circle, 0.05, [], 0.5)
#runge_kutta.deformation()
#runge_kutta.trajectory()

plt.xlim(0, -20)
plt.ylim(0, -20)
plt.ioff()  # выключаем
plt.show(block=True)




