import making_circle
from making_circle import CircleCreate

class RungeKutta(CircleCreate):
    def __init__(self, app_name):
        super().__init__()

        self.app_name = app_name

        print()