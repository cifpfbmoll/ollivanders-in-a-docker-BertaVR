class Inventory(object):
    def __init__(self, items):
        self.items = list(items)

    def update_quality(self):
        for item in self.items:
            item.update_quality()

    def get_items(self):
        return self.items


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    @property
    def name(self):
        return self.__name

    @property
    def sell_in(self):
        return self.__sell_in

    @property
    def quality(self):
        return self.__quality

    @name.setter
    def name(self, value):
        self.__name = value

    @sell_in.setter
    def sell_in(self, value):
        self.__sell_in = value

    @quality.setter
    def quality(self, value):
        self.__quality = value

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.sell_in == other.sell_in
            and self.quality == other.quality
        )

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Updateable:
    def update_quality(self):  # es una interfaz
        pass


class ConjuredItem(Item, Updateable):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def update_sell_in(self):
        self.sell_in -= 1

    def update_quality(self):
        if self.sell_in > 0:
            quality_increase = -2
        elif self.sell_in < 0:
            quality_increase = -4
        self.quality += quality_increase
        if (
            self.quality < 0
        ):  # esto nos asegura que la calidad no sea negativa, lo cual no es posible######
            self.quality = 0
        return self.quality


class NormalItem(Item, Updateable):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def setSell_in(self):
        self.sell_in = self.sell_in - 1

    def update_sell_in(self):
        self.sell_in -= 1  # tenemos dudas

    def setQuality(self, valor):
        if self.quality + valor > 50:
            self.quality = 50
        elif self.quality + valor >= 0:
            self.quality = self.quality + valor
        else:
            self.quality = 0
        assert 0 <= self.quality <= 50, (
            "quality de %s fuera de rango" % self.__class__.__name__
        )

    def update_quality(self):
        if self.sell_in > 0:
            quality_increase = -1
        elif self.sell_in < 0:
            quality_increase = -2
        self.quality += quality_increase
        if self.quality < 0:
            self.quality = 0
        return self.quality


class Sulfuras(NormalItem):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def update_quality(self):
        # Seteamos la calidad en 80 por si fuera el caso de que hubiera un error a la hora de introducir la calidad del sulfuras, no hacemos un assert porque es más eficiente que el programa no se pare, no??
        self.quality = 80
        return self.quality


class AgedBrie(NormalItem):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def setQuality(self, valor):
        NormalItem.setQuality(self, valor)

    def update_quality(self):
        if self.sell_in >= 0:
            quality_increase = 1
        elif self.sell_in < 0:
            quality_increase = 2
        self.quality += quality_increase
        if self.quality > 50:
            self.quality = 50
        return self.quality


class Backstage(NormalItem):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def update_quality(self):
        if self.sell_in > 10:
            quality_increase = 1
        elif self.sell_in > 5:
            quality_increase = 2
        elif self.sell_in > 0:
            quality_increase = 3
        elif self.sell_in == 0:
            quality_increase = -self.quality
        self.quality += quality_increase
        if self.quality > 50:
            self.quality = 50
        return self.quality
