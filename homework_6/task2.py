class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def running(self):
        result = self._length * self._width * 25 * 5 / 1000
        print(f'масса асфальта с длинной {self._length} м и шириной {self._width} м: {result}')


road = Road(20, 5000)
road.running()