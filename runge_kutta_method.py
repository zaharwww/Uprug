import numpy as np
import matplotlib.pyplot as plt


class RungeKutta:
    def __init__(self, circle_object, end_time, step, start_time = 0):
        self.circle = circle_object
        self.end_time = end_time
        self.step = step
        self.list_x = []
        self.list_y = []
        self.general_list_x = []
        self.general_list_y = []
        self.list_x_trajectory = []
        self.list_y_trajectory = []


    def runge_kutta_x(self, circle_object, step, list_x, end_time):
        num_points = len(circle_object.vector_of_points_inside_circle_x)

        while step < end_time:
            u = 1
            print(step)
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


                list_y = []
                t_0 = 0
                k_21 = np.exp(t_0) * circle_object.vector_of_points_inside_circle_y[i]
                t_21 = t_0 + 2 / 3 * step
                x_21 = circle_object.vector_of_points_inside_circle_y[i] + (2 / 3 * step * k_21)
                k_22 = np.exp(t_21) * x_21
                x_22 = circle_object.vector_of_points_inside_circle_y[i] + step * (-1 / 3 * k_21 + 1 * k_22)
                k_23 = np.exp(t_21) * x_22
                x_21_final = circle_object.vector_of_points_inside_circle_y[i] + step * (1 / 4 * k_21 + 2 / 4 * k_22 + 1 / 4 * k_23)
                if i == num_points-1 or i == 0:
                    self.list_x_trajectory.append(x_11_final)
                    self.list_y_trajectory.append(x_21_final)

                tolerance = 0.0001
                if abs(step - end_time / 2) < tolerance:
                    list_y.append(float(x_21_final))
                    self.general_list_y.append(list_y)
                    list_x.append(float(x_11_final))
                    self.general_list_x.append(list_x)
            tolerance = 0.0001
            if abs(step - end_time) < tolerance or abs(step - end_time / 2) < tolerance or abs(step - end_time / 4) < tolerance or abs(step - end_time / 5) < tolerance:
                plt.scatter(self.general_list_x, self.general_list_y, s=5)

                plt.show()


            self.general_list_x = []
            self.general_list_y = []
            step = step + 0.01
            u = u + 1

            plt.plot(self.list_x_trajectory, self.list_y_trajectory, '.')
            plt.show()
            self.list_x_trajectory = []
            self.list_y_trajectory = []



#   def runge_kutta_y(self, circle_object, step, list_y, end_time):
        #num_points = len(circle_object.vector_of_points_inside_circle_y)
        #print(num_points)
        #while step <= end_time:
            #u = 1
            #if step == end_time / 2 or step == end_time / 4 or step == end_time / 5 or u == 1:
                #for i in range(num_points):
                    #list_y = []
                    #t_0 = 0
                    #k_21 = np.exp(t_0) * circle_object.vector_of_points_inside_circle_y[i]
                    #t_21 = t_0 + 2/3 * step
                    #x_21 = circle_object.vector_of_points_inside_circle_y[i] + (2/3 * step * k_21)
                   # k_22 = np.exp(t_21) * x_21
                    #x_22 = circle_object.vector_of_points_inside_circle_y[i] + step * (-1/3 * k_21 + 1 * k_22)
                    #k_23 = np.exp(t_21) * x_22
                   # x_21_final = circle_object.vector_of_points_inside_circle_y[i] + step * (1/4 * k_21 + 2/4 * k_22 + 1/4 * k_23)
                    #list_y.append(float(x_21_final))
                   # self.general_list_y.append(list_y)
                   # if i == 1:
#                       # self.list_y_trajectory.append(list_y)

            #step = step + 0.001
           # u = u+1


   # def deformation(self):
        #plt.axis('equal')
        #plt.scatter(self.general_list_x, self.general_list_y)
        #plt.show()

   # def trajectory(self):
        #plt.axis('equal')
        #plt.scatter(self.list_x_trajectory, self.list_y_trajectory, color = "red")
       # plt.show()