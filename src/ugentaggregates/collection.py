from .aggregates import Aggregate


class Collection(object):
    """Base class for collections.
    """

    def __init__(self, items):
        """Initializer.

        :param items: list of data objects
        :type items: list
        """
        self.items = items

    def __getattribute__(self, name):
        """Priority accessor.

        :param name: the field name
        :type name: str
        :returns: the aggregate value or the attribute value
        :rtype: object
        """
        value = super(Collection, self).__getattribute__(name)
        if isinstance(value, Aggregate):
            # Return the aggregate value.
            return value(name, self.items)
        else:
            # Return the attribute value.
            return value

    def __iter__(self):
        """Iterator.

        :yields: every data object
        :ytype: object or dict
        """
        # Yield every item.
        for item in self.items:
            yield item

    def __getitem__(self, index):
        """Indexer.

        :param index: the index
        :type: int
        :returns: the indexed data object
        :rtype: object or dict
        """
        # Return the indexed item.
        return self.items[index]

    def __len__(self):
        """Length.

        :returns: the number of items
        :rtype: int
        """
        # Return the number of items.
        return len(self.items)
