import numpy as np
import matplotlib.pyplot as plt

class RungeKutta:
    def __init__(self, circle_object, end_time, step, start_time):
        self.circle = circle_object
        self.end_time = end_time
        self.step = step
        self.start_time = start_time

    def runge_kutta(self, circle_object, step, end_time, start_time):
        list_of_coordinate_x_forall = []
        list_of_coordinate_y_forall = []

        num_points = len(circle_object.vector_of_points_inside_circle_x)
        while start_time < end_time:
            for i in range(num_points):
                k_11 = - np.exp(start_time) * circle_object.vector_of_points_inside_circle_x[i]
                t_11 = start_time + (2/3) * step
                x_11 = circle_object.vector_of_points_inside_circle_x[i] + ((2/3) * step * k_11)
                k_12 = - np.exp(t_11) * x_11
                x_12 = circle_object.vector_of_points_inside_circle_x[i] + step * ((-1/3) * k_11 + 1 * k_12)
                k_13 = - np.exp(t_11) * x_12
                x_11_final = circle_object.vector_of_points_inside_circle_x[i] + step * ((1/4) * k_11 + (2/4) * k_12 + (1/4) * k_13)
                list_of_coordinate_x_forall.append(float(x_11_final))

                k_21 = np.exp(start_time) * circle_object.vector_of_points_inside_circle_y[i]
                t_21 = start_time + (2/3) * step
                x_21 = circle_object.vector_of_points_inside_circle_y[i] + ((2/3) * step * k_21)
                k_22 = np.exp(t_21) * x_21
                x_22 = circle_object.vector_of_points_inside_circle_y[i] + step * ((-1/3) * k_21 + 1 * k_22)
                k_23 = np.exp(t_21) * x_22
                x_21_final = circle_object.vector_of_points_inside_circle_y[i] + step * ((1/4) * k_21 + (2/4) * k_22 + (1/4) * k_23)
                list_of_coordinate_y_forall.append(float(x_21_final))

            start_time = start_time + step
        plt.scatter(list_of_coordinate_x_forall, list_of_coordinate_y_forall, s=5)
        plt.show()

    def runge_kutta_fast_step(self, circle_object, step, end_time, start_time):
        list_of_coordinate_x_for_several_points = []
        list_of_coordinate_y_for_several_points = []

        while start_time < end_time:
            k_11 = - np.exp(start_time) * circle_object.vector_of_points_inside_circle_x[0]
            t_11 = start_time + (2/3) * step
            x_11 = circle_object.vector_of_points_inside_circle_x[0] + ((2/3) * step * k_11)
            k_12 = - np.exp(t_11) * x_11
            x_12 = circle_object.vector_of_points_inside_circle_x[0] + step * ((-1/3) * k_11 + 1 * k_12)
            k_13 = - np.exp(t_11) * x_12
            x_11_final = circle_object.vector_of_points_inside_circle_x[0] + step * ((1/4) * k_11 + (2/4) * k_12 + (1/4) * k_13)
            list_of_coordinate_x_for_several_points.append(float(x_11_final))

            k_21 = np.exp(start_time) * circle_object.vector_of_points_inside_circle_y[0]
            t_21 = start_time + (2/3) * step
            x_21 = circle_object.vector_of_points_inside_circle_y[0] + ((2/3) * step * k_21)
            k_22 = np.exp(t_21) * x_21
            x_22 = circle_object.vector_of_points_inside_circle_y[0] + step * ((-1/3) * k_21 + 1 * k_22)
            k_23 = np.exp(t_21) * x_22
            x_21_final = circle_object.vector_of_points_inside_circle_y[0] + step * ((1/4) * k_21 + (2/4) * k_22 + (1/4) * k_23)
            list_of_coordinate_y_for_several_points.append(float(x_21_final))

            start_time = start_time + step

        plt.scatter(list_of_coordinate_x_for_several_points, list_of_coordinate_y_for_several_points, s=5, color = 'red')
        plt.show()

