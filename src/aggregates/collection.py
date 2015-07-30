from .aggregates import Aggregate


class Collection(object):
    """Base class for collections.
    """

    def __init__(self, items):
        """Initializer.
        """
        self.items = items

    def __getattribute__(self, name):
        """Priority accessor.
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
        """
        # Yield every item.
        for item in self.items:
            yield item

    def __getitem__(self, index):
        """Indexer.
        """
        # Return the indexed item.
        return self.items[index]

    def __len__(self):
        """Length.
        """
        return len(self.items)
