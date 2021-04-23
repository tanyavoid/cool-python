# it's possible to use non-ASCII characters in identifiers.
# best (only?) suitable for educational purposes.


class Кошачьи:
    """=^..^="""
    семейство_латинский = 'Felidae'

    @property
    def семейство(self):
        return self.__class__.__name__

    def мурлыкай(self):
        return 'мрр-фрр-мрр'


class БольшиеКошки(Кошачьи):
    подсемейство_латинский = 'Felinae'

    @property
    def подсемейство(self):
        return self.__class__.__name__

    def рычи(self):
        return 'ррр-ррр-ррр'


class МалыеКошки(Кошачьи):
    подсемейство_латинский = 'Felinae'

    @property
    def подсемейство(self):
        return self.__class__.__name__


if __name__ == '__main__':
    манул = МалыеКошки()
    assert isinstance(манул, Кошачьи), 'Не кошка!'
    try:
        манул.рычи
    except AttributeError:
        print('Малые кошки не могут рычать!')

    тигр = Кошачьи()
    assert isinstance(тигр, МалыеКошки), 'Не малая кошка!'
