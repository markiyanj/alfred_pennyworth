import dataclasses


class Maths:
    """
    Make class with one method "add_num" with 2 parameters, which returns sum of these parameters.
    Note: this method should not take instance as first parameter.
    """

    @staticmethod
    def add_num(x, y):
        return x + y


class Pizza:
    """
    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
    It should have 2 methods:
    margherita (['mozzarella', 'tomatoes']) and prosciutto (['mozzarella', 'tomatoes', 'ham'])
    which should create Pizza instances with predefined list of ingredients.
    Example:
        pizza1 = Pizza(["tomato", "cucumber"])
        pizza1.ingredients will equal to ["tomato", "cucumber"]
        pizza2 = Pizza.prosciutto()
        pizza2.ingredients will equal to ['mozzarella', 'tomatoes', 'ham']
    """

    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """
    max_visitors_num = 0

    class Value:
        def __init__(self):
            self.value = None

        @classmethod
        def _new_value(cls, value):
            if value > Concert.max_visitors_num:
                return Concert.max_visitors_num
            else:
                return value

        def __get__(self, instance, owner):
            return self.value

        def __set__(self, instance, value):
            self.value = self._new_value(value)

    visitors_count = Value()


@dataclasses.dataclass
class BookDataclass:
    """
    Create dataclass with 3 fields - title (str), author (str), pages_num (int)
    """
    title: str
    author: str
    pages_num: int


class Book:
    """
    Create regular class taking 3 params on init - title, author, pages_num
    Make its str() representation the same as for BookDataclass defined above.
    """

    def __init__(self, title, author, pages_num):
        self.title = title
        self.author = author
        self.pages_num = pages_num

    def __str__(self):
        return str(BookDataclass(title=self.title, author=self.author, pages_num=self.pages_num))