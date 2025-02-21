class Color:
    def __init__(self, color):
        self._color = color

    # Método get
        @property
        def color(self):
            return self._color
        
    # Método set
        @color.setter
        def color(self, color):
            self._color = color

    def __str__(self):
        return f'Color: {self._color}\n'
    