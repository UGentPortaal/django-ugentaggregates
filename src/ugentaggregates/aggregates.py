from .utils import get_field
from .utils import has_field

NO_DEFAULT = object()  # Marker for missing default value.
NO_VALUE = object()  # Marker for missing value.


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

    def __init__(self, name=None, valid=None, format=None, default=NO_DEFAULT):
        """Initializer.

        :param name: the field name (optional)
        :type name: str
        :param valid: filter for valid values (optional)
        :type valid: function
        :param format: formatter for values (optional)
        :type format: function
        :param default: the default value (optional)
        :type default: object
        """
        self.name = name
        self.valid = valid
        self.format = format
        self.default = default

    def __call__(self, name, items):
        """Callable.

        :param name: the field name
        :type name: str
        :param items: list of data objects
        :type items: list
        :returns: the first field value
        :rtype: object
        :raises AttributeError: if field is missing
        """
        # Override the name if necessary.
        name = self.name or name

        for item in items:
            if has_field(item, name):
                value = get_field(item, name)
                if callable(value):
                    value = value()

                if self.valid and not self.valid(value):
                    continue

                if self.format:
                    return self.format(value)

                return value

        if self.default == NO_DEFAULT:
            # Default value is missing; raise an exception.
            raise AttributeError(name)
        else:
            # Return the default value.
            return self.default


class AllAggregate(Aggregate):
    """Aggregate that returns all values.
    """

    def __init__(self, name=None, valid=None, format=None, unique=False):
        """Initializer.

        :param name: the field name (optional)
        :type name: str
        :param valid: filter for valid values (optional)
        :type valid: function
        :param format: formatter for values (optional)
        :type format: function
        :param unique: flag for unique values (optional)
        :type unique: bool
        """
        self.name = name
        self.valid = valid
        self.format = format
        self.unique = unique

    def __call__(self, name, items):
        """Callable.

        :param name: the field name
        :type name: str
        :param items: list of data objects
        :type items: list
        :returns: list of field values
        :rtype: list
        """
        result = []

        # Override the name if necessary.
        name = self.name or name

        # Find all values for the field.
        for item in items:
            if has_field(item, name):
                values = get_field(item, name)
                if callable(values):
                    values = values()
                if not hasattr(values, "__iter__"):
                    values = [values]

                for value in values:
                    if self.valid and not self.valid(value):
                        continue

                    if self.format:
                        value = self.format(value)

                    if self.unique and value in result:
                        continue

                    result.append(value)

        return result
