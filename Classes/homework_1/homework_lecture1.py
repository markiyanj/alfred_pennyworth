class CustomInt(int):
    """
    Make class for custom int, which will behave "vice versa" for comparison operations:
    e.g., int < int means less then, but custom int < int should equal custom int > int.
    Take into account <, >, >=, <=
    ** try to achieve this without __init__ rewriting
    """

    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        return self.x > other

    def __gt__(self, other):
        return self.x < other

    def __le__(self, other):
        return self.x >= other

    def __ge__(self, other):
        return self.x <= other


class PersonWithLimitedSkills:
    """
    Make class which is limited to 2 actions - eat and sleep
    Any other attributes addition should result in an error.
    """
    __slots__ = ('sleep', 'eat')


class HiddenAttrs:
    """
    Make class which never tells about its attributes.
    Its attribute list is always empty and attributes dictionary is always empty.
    """
    __dict__ = {}

    def __dir__(self):
        return []


class CallableInstances:
    """
    Make class which takes func parameter on initialization, which is a callable that can be passed.
    Then object of this class may be called - callable passed on init will be called with passed parameters.
    """

    def __init__(self, func):
        self.func = func

    def __call__(self, a, *args, **kwargs):
        return self.func(a)
