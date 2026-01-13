
import numpy as np
import matplotlib.pyplot as plt

class RungeKutta:
    def __init__(self, circle_object):
        self.circle = circle_object

    def runge_kutta(self, circle_object, step, end_time, start_time):
        list_of_coordinate_x_forall = []
        list_of_coordinate_y_forall = []
        list_x = circle_object.vector_of_points_inside_circle_x
        list_y = circle_object.vector_of_points_inside_circle_y

        num_points = len(circle_object.vector_of_points_inside_circle_x)
        while start_time < end_time:
            for i in range(num_points):
                k_11 = - np.exp(start_time) * list_x[i]
                t_11 = start_time + (2/3) * step
                x_11 = list_x[i] + ((2/3) * step * k_11)
                k_12 = - np.exp(t_11) * x_11
                t_12 = start_time + (2/3) * step
                x_12 = list_x[i] + step * ((-1/3) * k_11 + 1 * k_12)
                k_13 = - np.exp(t_12) * x_12
                x_11_final = list_x[i] + step * ((1/4) * k_11 + (2/4) * k_12 + (1/4) * k_13)
                list_of_coordinate_x_forall.append(float(x_11_final))

                k_21 = np.exp(start_time) * list_y[i]
                t_21 = start_time + (2/3) * step
                x_21 = list_y[i] + ((2/3) * step * k_21)
                k_22 = np.exp(t_21) * x_21
                t_22 = start_time + (2/3) * step
                x_22 = list_y[i] + step * ((-1/3) * k_21 + 1 * k_22)
                k_23 = np.exp(t_22) * x_22
                x_21_final = list_y[i] + step * ((1/4) * k_21 + (2/4) * k_22 + (1/4) * k_23)
                list_of_coordinate_y_forall.append(float(x_21_final))

            start_time = start_time + step
            list_x = list_of_coordinate_x_forall
            list_y = list_of_coordinate_y_forall
            list_of_coordinate_x_forall = []
            list_of_coordinate_y_forall = []
        plt.scatter(list_x, list_y, s=5)
        plt.show()

    def runge_kutta_fast_step(self, circle_object, step, end_time, start_time):
        list_of_coordinate_x_for_several_points = []
        list_of_coordinate_y_for_several_points = []
        list_x_1 = circle_object.vector_of_points_inside_circle_x
        list_y_1 = circle_object.vector_of_points_inside_circle_y

        num_points = len(circle_object.vector_of_points_inside_circle_x)
        for g in range(num_points):
            dop_x = list_x_1[g]
            dop_y = list_y_1[g]
            while start_time < end_time:
                k_11 = - np.exp(start_time) * dop_x
                t_11 = start_time + (2/3) * step
                x_11 = dop_x + ((2/3) * step * k_11)
                k_12 = - np.exp(t_11) * x_11
                t_12 = start_time + (2/3) * step
                x_12 = dop_x + step * ((-1/3) * k_11 + 1 * k_12)
                k_13 = - np.exp(t_12) * x_12
                x_11_final = dop_x + step * ((1/4) * k_11 + (2/4) * k_12 + (1/4) * k_13)
                list_of_coordinate_x_for_several_points.append(float(x_11_final))
                dop_x = x_11_final

                k_21 = np.exp(start_time) * dop_y
                t_21 = start_time + (2/3) * step
                x_21 = dop_y + ((2/3) * step * k_21)
                k_22 = np.exp(t_21) * x_21
                t_22 = start_time + (2/3) * step
                x_22 = dop_y + step * ((-1/3) * k_21 + 1 * k_22)
                k_23 = np.exp(t_22) * x_22
                x_21_final = dop_y + step * ((1/4) * k_21 + (2/4) * k_22 + (1/4) * k_23)
                list_of_coordinate_y_for_several_points.append(float(x_21_final))
                dop_y = x_21_final
                start_time = start_time + step
            if g == 0:
                plt.plot(list_of_coordinate_x_for_several_points, list_of_coordinate_y_for_several_points, color = 'red', linewidth = 0.5)
            else:
                plt.plot(list_of_coordinate_x_for_several_points, list_of_coordinate_y_for_several_points, color='red',linewidth=0.1)


            list_of_coordinate_x_for_several_points = []
            list_of_coordinate_y_for_several_points = []
            list_x_1 = circle_object.vector_of_points_inside_circle_x
            list_y_1 = circle_object.vector_of_points_inside_circle_y
            start_time = 0


