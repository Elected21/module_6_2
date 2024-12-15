class Vehicle:
    _COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self._model = model
        self._engine_power = engine_power
        self._color = color

    def get_model(self):
        return f"Модель: {self._model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self._engine_power}"

    def get_color(self):
        return f"Цвет: {self._color}"

    def print_info(self):
        print (f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__class__._COLOR_VARIANTS:
            self._color = new_color
        else:
            print(f'Нельзя поменять цвет на {new_color}')


class Sedan(Vehicle):

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)
        self._PASSENGERS_LIMIT = 5



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)


vehicle1.print_info()


vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'


vehicle1.print_info()