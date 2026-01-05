import making_circle
import runge_kutta_method

circle = making_circle.CircleCreate(4)
circle.create_circle(3)
circle.plot_circle()

runge_kutta = runge_kutta_method.RungeKutta(circle, 2, 0.05)
print()
runge_kutta.runge_kutta_x(circle, 0.05, [], [])
runge_kutta.runge_kutta_y(circle, 0.05, [], [])



