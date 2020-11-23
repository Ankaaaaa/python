class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки Pen')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки Pencil')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки Handle')


a = Stationery('LIST')
a.draw()
print(30*'---')

b = Pen('LIST')
b.draw()
print(30*'---')

c = Pencil('LIST')
c.draw()
print(30*'---')

d = Handle('LIST')
d.draw()
print(30*'---')