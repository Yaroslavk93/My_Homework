class Fire:
    element = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Ground):
            return Lava()
        elif isinstance(other, Air):
            return Lightning()


class Water:
    element = 'Вода'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Ground):
            return Dirt()
        elif isinstance(other, Air):
            return Storm()


class Ground:
    element = 'Земля'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()


class Air:
    element = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Water):
            return Storm()
        elif isinstance(other, Ground):
            return Dust()


class Lightning:
    def __str__(self):
        return 'Молния'


class Steam:
    def __str__(self):
        return 'Пар'


class Lava:
    def __str__(self):
        return 'Лава'


class Dirt:
    def __str__(self):
        return 'Грязь'


class Storm:
    def __str__(self):
        return 'Шторм'


class Dust:
    def __str__(self):
        return 'Пыль'
