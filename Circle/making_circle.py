import random
import matplotlib.pyplot as plt

class CircleCreate:
    def __init__(self, radius_of_circle):
        self.radius_of_circle = radius_of_circle
        self.counter = 0
        self.vector_of_points_inside_circle_x = [-2 * self.radius_of_circle]
        self.vector_of_points_inside_circle_y = [-2 * self.radius_of_circle]

    def create_ring(self):
        count = -2 * self.radius_of_circle - self.radius_of_circle - 1
        while count <= 0:
            if -3 * self.radius_of_circle ** 2 - count ** 2 - 4 * count * self.radius_of_circle >= 0:
                y_1 = - ((-3 * self.radius_of_circle ** 2 - count ** 2 - 4 * count * self.radius_of_circle) ** (1/2)) - 2 * self.radius_of_circle
                y_2 = ((-3 * self.radius_of_circle ** 2 - count ** 2 - 4 * count * self.radius_of_circle) ** (1/2)) - 2 * self.radius_of_circle
                self.vector_of_points_inside_circle_x.append(count)
                self.vector_of_points_inside_circle_x.append(count)
                self.vector_of_points_inside_circle_y.append(y_1)
                self.vector_of_points_inside_circle_y.append(y_2)
            if count < -2 * self.radius_of_circle - self.radius_of_circle*6.4/7 or (count > -2 * self.radius_of_circle + self.radius_of_circle*6.4/7 and count < -2 * self.radius_of_circle + self.radius_of_circle):
                count = count + 0.02
            else:
                count = count + 0.06
    def create_circle(self, num_points):
        while self.counter != num_points:
            x_circle = random.uniform(-1 * self.radius_of_circle, -1 * self.radius_of_circle - 2 * self.radius_of_circle)
            y_circle = random.uniform(-1 * self.radius_of_circle, -1 * self.radius_of_circle - 2 * self.radius_of_circle)

            if (y_circle + 2 * self.radius_of_circle) ** 2 + (x_circle + 2 * self.radius_of_circle) ** 2 <= self.radius_of_circle ** 2:
                self.vector_of_points_inside_circle_x.append(x_circle)
                self.vector_of_points_inside_circle_y.append(y_circle)
            self.counter = self.counter + 1

    def plot_circle(self):
        plt.scatter(self.vector_of_points_inside_circle_x, self.vector_of_points_inside_circle_y, s=5)

