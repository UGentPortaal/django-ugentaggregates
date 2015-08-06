import unittest


class AggregateTestCase(unittest.TestCase):
    """Tests for class ``Aggregate``.
    """

    @classmethod
    def setUpClass(cls):
        """Set up the class fixture.
        """
        from aggregates.aggregates import Aggregate

        cls.Aggregate = Aggregate

    def setUp(self):
        """Set up the fixture.
        """
        self.aggr1 = self.Aggregate()

    def tearDown(self):
        """Tear down the fixture.
        """
        self.aggr1 = None

    def test_creation(self):
        """Test for creating an ``Aggregate`` object.
        """
        self.assertTrue(isinstance(self.aggr1, self.Aggregate))

    def test_callable(self):
        """Test for calling an ``Aggregate`` object.
        """
        with self.assertRaises(NotImplementedError):
            self.aggr1("field1", [])


class FirstAggregateTestCase(unittest.TestCase):
    """Tests for class ``FirstAggregate``.
    """

    @classmethod
    def setUpClass(cls):
        """Set up the class fixture.
        """
        from aggregates.aggregates import Aggregate
        from aggregates.aggregates import FirstAggregate
        from aggregates.aggregates import NO_DEFAULT

        cls.Aggregate = Aggregate
        cls.FirstAggregate = FirstAggregate
        cls.NO_DEFAULT = NO_DEFAULT

    def test_creation(self):
        """Test for creating a ``FirstAggregate`` object.
        """
        aggr1 = self.FirstAggregate()
        self.assertTrue(isinstance(aggr1, self.FirstAggregate))

    def test_inheritance(self):
        """Test for the inheritance of class ``FirstAggregate``.
        """
        self.assertTrue(issubclass(self.FirstAggregate, self.Aggregate))

    def test_callable(self):
        """Test for calling a ``FirstAggregate`` object.
        """
        aggr1 = self.FirstAggregate()
        self.assertEqual(aggr1("field1", [{"field1": 1},
                                          {"field1": 2}]),
                         1)
        self.assertEqual(aggr1("field1", [{"field2": 1},
                                          {"field1": 2}]),
                         2)

    def test_missing(self):
        """Test for calling a ``FirstAggregate`` object for a missing
        attribute.
        """
        aggr1 = self.FirstAggregate()
        with self.assertRaises(AttributeError):
            aggr1("field1", [{"field2": 1},
                             {"field2": 2}])

    def test_empty(self):
        """Test for calling a ``FirstAggregate`` object with an empty list.
        """
        aggr1 = self.FirstAggregate()
        with self.assertRaises(AttributeError):
            aggr1("field1", [])

    def test_name(self):
        """Test for the attribute ``name`.
        """
        aggr1 = self.FirstAggregate(name="field1")
        self.assertEqual(aggr1.name, "field1")
        self.assertEqual(aggr1("field2", [{"field1": 1,
                                           "field2": 2}]),
                         1)

    def test_valid(self):
        """Test for the attribute ``valid``.
        """
        is_even = lambda i: i % 2 == 0
        aggr1 = self.FirstAggregate(valid=is_even)
        self.assertEqual(aggr1.valid, is_even)
        self.assertEqual(aggr1("field1", [{"field1": 1},
                                          {"field1": 2}]),
                         2)
        self.assertEqual(aggr1("field1", [{"field1": 2},
                                          {"field1": 4}]),
                         2)

    def test_format(self):
        """Test for the attribute ``format``.
        """
        double = lambda i: i * 2
        aggr1 = self.FirstAggregate(format=double)
        self.assertEqual(aggr1.format, double)
        self.assertEqual(aggr1("field1", [{"field1": 1},
                                          {"field1": 2}]),
                         2)

    def test_default(self):
        """Test for the attribute ``default``.
        """
        # Without default.
        aggr1 = self.FirstAggregate()
        self.assertEqual(aggr1.default, self.NO_DEFAULT)

        # With default.
        aggr2 = self.FirstAggregate(default=-1)
        self.assertEqual(aggr2.default, -1)
        self.assertEqual(aggr2("field1", []),
                         -1)
        self.assertEqual(aggr2("field1", [{"field2": 1},
                                          {"field2": 2}]),
                         -1)


class AllAggregateTestCase(unittest.TestCase):
    """Tests for class ``AllAggregate``.
    """

    @classmethod
    def setUpClass(cls):
        """Set up the class fixture.
        """
        from aggregates.aggregates import Aggregate
        from aggregates.aggregates import AllAggregate

        cls.Aggregate = Aggregate
        cls.AllAggregate = AllAggregate

    def test_creation(self):
        """Test for creating a ``AllAggregate`` object.
        """
        aggr1 = self.AllAggregate()
        self.assertTrue(isinstance(aggr1, self.AllAggregate))

    def test_inheritance(self):
        """Test for the inheritance of class ``AllAggregate``.
        """
        self.assertTrue(issubclass(self.AllAggregate, self.Aggregate))

    def test_callable(self):
        """Test for calling an ``AllAggregate`` object.
        """
        aggr1 = self.AllAggregate()
        self.assertEqual(aggr1("field1", [{"field1": 1},
                                          {"field1": 2}]),
                         [1, 2])
        self.assertEqual(aggr1("field1", [{"field2": 1},
                                          {"field1": 2}]),
                         [2])

    def test_list(self):
        """Test for calling an ``AllAggregate`` object with list
        attributes.
        """
        aggr1 = self.AllAggregate()
        self.assertEqual(aggr1("field1", [{"field1": [1, 2]},
                                          {"field1": [3, 4]}]),
                         [1, 2, 3, 4])
        self.assertEqual(aggr1("field1", [{"field1": 1},
                                          {"field1": [2, 3]}]),
                         [1, 2, 3])
        self.assertEqual(aggr1("field1", [{"field1": [1, 2]},
                                          {"field1": 3}]),
                         [1, 2, 3])

    def test_missing(self):
        """Test for calling an ``AllAggregate`` object for a missing
        attribute.
        """
        aggr1 = self.AllAggregate()
        self.assertEqual(aggr1("field1", [{"field2": 1},
                                          {"field2": 2}]),
                         [])

    def test_empty(self):
        """Test for calling an ``AllAggregate`` object with an empty list.
        """
        aggr1 = self.AllAggregate()
        self.assertEqual(aggr1("field1", []),
                         [])

    def test_name(self):
        """Test for the attribute ``name`.
        """
        aggr1 = self.AllAggregate(name="field1")
        self.assertEqual(aggr1.name, "field1")
        self.assertEqual(aggr1("field2", [{"field1": 1, "field2": 2},
                                          {"field1": 3, "field2": 4}]),
                         [1, 3])

    def test_valid(self):
        """Test for the attribute ``valid``.
        """
        is_even = lambda i: i % 2 == 0
        aggr1 = self.AllAggregate(valid=is_even)
        self.assertEqual(aggr1.valid, is_even)
        self.assertEqual(aggr1("field1", [{"field1": 1},
                                          {"field1": 2}]),
                         [2])
        self.assertEqual(aggr1("field1", [{"field1": 2},
                                          {"field1": 4}]),
                         [2, 4])

    def test_format(self):
        """Test for the attribute ``format``.
        """
        double = lambda i: i * 2
        aggr1 = self.AllAggregate(format=double)
        self.assertEqual(aggr1.format, double)
        self.assertEqual(aggr1("field1", [{"field1": 1},
                                          {"field1": 2}]),
                         [2, 4])

    def test_unique(self):
        """Test for the attribute ``unique``.
        """
        # Unique is false.
        aggr1 = self.AllAggregate()
        self.assertEqual(aggr1.unique, False)
        self.assertEqual(aggr1("field1", [{"field1": 1},
                                          {"field1": 1}]),
                         [1, 1])

        # Unique is true.
        aggr2 = self.AllAggregate(unique=True)
        self.assertEqual(aggr2.unique, True)
        self.assertEqual(aggr2("field1", [{"field1": 1},
                                          {"field1": 1}]),
                         [1])
