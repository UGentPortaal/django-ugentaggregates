from .utils import get_field
from .utils import has_field

NO_DEFAULT = object()


class Aggregate(object):
    """Base class for aggregates.
    """

    def __call__(self, name, items):
        """Callable.
        """
        raise NotImplementedError


class FirstAggregate(Aggregate):
    """Aggregate that returns the first value.
    """

    def __init__(self, name=None, valid=None, default=NO_DEFAULT):
        """Initializer.
        """
        self.name = name
        self.valid = valid
        self.default = default

    def __call__(self, name, items):
        """Callable.
        """
        name = self.name or name

        for item in items:
            if has_field(item, name):
                value = get_field(item, name)
                if self.valid:
                    if self.valid(value):
                        return value
                else:
                    return value

        if self.default == NO_DEFAULT:
            raise AttributeError(name)
        else:
            return self.default


class AllAggregate(Aggregate):
    """Aggregate that returns all values.
    """

    def __init__(self, name=None, valid=None, unique=False):
        """Initializer.
        """
        self.name = name
        self.valid = valid
        self.unique = unique

    def __call__(self, name, items):
        """Callable.
        """
        result = []

        name = self.name or name

        for item in items:
            if has_field(item, name):
                value = get_field(item, name)
                if hasattr(value, "__iter__"):
                    result.extend(value)
                else:
                    result.append(value)

        if self.valid:
            result = [value for value in result if self.valid(value)]
        if self.unique:
            result = list(set(result))

        return result
