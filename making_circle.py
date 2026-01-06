import random
import matplotlib.pyplot as plt

class CircleCreate:
    def __init__(self, radius_of_circle):
        self.radius_of_circle = radius_of_circle
        self.counter = 0
        self.vector_of_points_inside_circle_x = []
        self.vector_of_points_inside_circle_y = []

    def create_ring(self):
        cunt = 0.0
        while cunt >= -100.0:
            if -3 * self.radius_of_circle ** 2 - cunt ** 2 - 4 * cunt * self.radius_of_circle >= 0:
                y_1 = - ((-3 * self.radius_of_circle ** 2 - cunt ** 2 - 4 * cunt * self.radius_of_circle) ** (1/2)) - 2 * self.radius_of_circle
                y_2 = ((-3 * self.radius_of_circle ** 2 - cunt ** 2 - 4 * cunt * self.radius_of_circle) ** (1/2)) - 2 * self.radius_of_circle
                self.vector_of_points_inside_circle_x.append(cunt)
                self.vector_of_points_inside_circle_x.append(cunt)
                self.vector_of_points_inside_circle_y.append(y_1)
                self.vector_of_points_inside_circle_y.append(y_2)
            cunt = cunt - 0.0005
        print(self.vector_of_points_inside_circle_x)
        print(self.vector_of_points_inside_circle_y)


    def create_circle(self, num_points):
        while self.counter != num_points:
            x_circle = random.uniform(-1 * self.radius_of_circle, -1 * self.radius_of_circle - 2 * self.radius_of_circle)
            y_circle = random.uniform(-1 * self.radius_of_circle, -1 * self.radius_of_circle - 2 * self.radius_of_circle)

            if (y_circle + 2 * self.radius_of_circle) ** 2 + (x_circle + 2 * self.radius_of_circle) ** 2 <= self.radius_of_circle ** 2:
                self.vector_of_points_inside_circle_x.append(x_circle)
                self.vector_of_points_inside_circle_y.append(y_circle)
            self.counter = self.counter + 1

    def plot_circle(self):
        plt.scatter(self.vector_of_points_inside_circle_x, self.vector_of_points_inside_circle_y)
        plt.show()

