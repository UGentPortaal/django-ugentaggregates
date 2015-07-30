Aggregates
==========

Aggregates for Django.


Description
-----------

Aggregates allow acces to the attributes of a set of objects or dictionaries
through a single interface.


Installation
------------

The following command will install the package::

    $ python setup.py install

The following command will install the package in development mode::

    $ python setup.py develop


Tests
-----

The following command will run the tests::

    $ python setup.py test


Contents
--------

class ``Aggregate``
    Base class for all aggregates.  Subclass this class to create a custom
    aggregate.

class ``FirstAggregate``
    Aggregate that returns the first value for a field.

class ``AllAggregate``
    Aggregate that returns all values for a field.

class ``Collection``
    Base class for all collections.  Subclass this class to create a custom
    collection, adding the required aggregates.


Usage
-----

1. Define a custom collection, adding the required aggregates::

    >>> from aggregates import FirstAggregation, AllAggregation
    >>> from aggregates import Collection
    >>> class MyCollection(Collection):
    ...     field1 = FirstAggregation()
    ...     field2 = AllAggregation()

2. Create a collection, containing the items::

    >>> my_items = [{"field1": 1, "field2": 3, "field3": 5},
    ...             {"field1": 2, "field2": 4, "field3": 6}]
    >>> my_collection = MyCollection(my_items)

3. Access the fields through the collection::

    >>> my_collection.field1
    1
    >>> my_collection.field2
    [3, 4]
    >>> my_collection.field3
    Traceback (most recent call last):
      ...
    AttributeError: 'MyCollection' object has no attribute 'field3'


Contibutors
-----------

- Bert Vanderbauwhede (bert.vanderbauwhede@ugent.be), original author
