class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass_of_asphalt(self, asphalt=25, thickness=5):
        mass = self._length * self._width * asphalt * thickness / 1000
        print(f'The mass of asphalt on this selection of the road = {mass:.3f} ton')


road_section_1 = Road(5000, 20)
road_section_2 = Road(4321, 27)
road_section_1.mass_of_asphalt()
road_section_2.mass_of_asphalt(45, 7)
