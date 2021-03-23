class Road:
    def __init__(self, _length, _width, height=5, meter_mass_kg=25):
        self._area = _length * _width
        self.meter_mass_ton = meter_mass_kg / 1000 * height  # Масса асфальта для одного квадратного метра
        # дорожного покрытия в тоннах, при толщине дорожного покрытия height в 5 см.

    def mass(self):
        return f'{self._area * self.meter_mass_ton} т.'  # Вычисление массы асфальта для заданной площади,
    # и толщине покрытия в 5 см.


r = Road(20, 5000)
print(r.mass())
