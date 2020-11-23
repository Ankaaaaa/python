from itertools import cycle
import time
class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running (self):
        count = 1
        for i in cycle(self.__color):
            if i == 'green':
                print(i)
                time.sleep(6)
            if i == 'yellow':
                print(i)
                time.sleep(2)
            if i == 'red':
                print(i)
                time.sleep(7)
            count += 1
            if count == 7:
                print('выход')
                break



my_traffic = TrafficLight (['red', 'yellow', 'green'])
my_traffic.running()