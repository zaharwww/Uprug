import numpy as np
class RungeKutta:
    def __init__(self, circle_object, end_time, step, start_time = 0):
        self.circle = circle_object
        self.end_time = end_time
        self.step = step
        self.list_x = []
        self.list_y = []
        self.general_list_x = []
        self.general_list_x = []

        print(circle_object.vector_of_points_inside_circle_x)
        print(circle_object.vector_of_points_inside_circle_y)

    def runge_kutta_x(self, circle_object, step, list_x, general_list_x):
        num_points = len(circle_object.vector_of_points_inside_circle_x)
        while step <= 2:
            for i in range(num_points):
                list_x = []
                t_0 = 0
                k_11 = - np.exp(t_0) * circle_object.vector_of_points_inside_circle_x[i]
                t_11 = t_0 + 2/3 * step
                x_11 = circle_object.vector_of_points_inside_circle_x[i] + (2/3 * step * k_11)
                k_12 = - np.exp(t_11) * x_11
                x_12 = circle_object.vector_of_points_inside_circle_x[i] + step * (-1/3 * k_11 + 1 * k_12)
                k_13 = - np.exp(t_11) * x_12
                x_11_final = circle_object.vector_of_points_inside_circle_x[i] + step * (1/4 * k_11 + 2/4 * k_12 + 1/4 * k_13)
                list_x.append(float(x_11_final))
                general_list_x.append(list_x)
            step = step + 2
        print(general_list_x)

    def runge_kutta_y(self, circle_object, step, list_y, general_list_y):
        num_points = len(circle_object.vector_of_points_inside_circle_y)
        while step <= 2:
            for i in range(num_points):
                list_y = []
                t_0 = 0
                k_21 = - np.exp(t_0) * circle_object.vector_of_points_inside_circle_y[i]
                t_21 = t_0 + 2/3 * step
                x_21 = circle_object.vector_of_points_inside_circle_y[i] + (2/3 * step * k_21)
                k_22 = - np.exp(t_21) * x_21
                x_22 = circle_object.vector_of_points_inside_circle_y[i] + step * (-1/3 * k_21 + 1 * k_22)
                k_23 = - np.exp(t_21) * x_22
                x_21_final = circle_object.vector_of_points_inside_circle_y[i] + step * (1/4 * k_21 + 2/4 * k_22 + 1/4 * k_23)
                list_y.append(float(x_21_final))
                general_list_y.append(list_y)
            step = step + 2
        print(general_list_y)
