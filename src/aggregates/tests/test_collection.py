import unittest


class CollectionTestCase(unittest.TestCase):
    """Tests for collection ``Collection``.
    """

    @classmethod
    def setUpClass(cls):
        """Set up the class fixture.
        """
        from aggregates.aggregates import AllAggregate
        from aggregates.aggregates import FirstAggregate
        from aggregates.collection import Collection

        class Obj1(object):
            pass

        class Coll1(Collection):
            field1 = FirstAggregate()
            field2 = AllAggregate()

        cls.Obj1 = Obj1
        cls.Coll1 = Coll1

    def test_creation(self):
        """Test for creating a ``Collection`` object.
        """
        items = [{"field1": 1},
                 {"field1": 2}]
        coll1 = self.Coll1(items)
        self.assertTrue(isinstance(coll1, self.Coll1))
        self.assertEqual(coll1.items, items)

    def test_aggregates(self):
        """Test for a ``Collection`` object's aggregates.
        """
        coll1 = self.Coll1([{"field1": 1, "field2": 2},
                            {"field1": 3, "field2": 4}])
        self.assertEqual(coll1.field1, 1)
        self.assertEqual(coll1.field2, [2, 4])

    def test_inaccessible(self):
        """Test for a ``Collection`` object's inaccessible fields.
        """
        coll1 = self.Coll1([{"field1": 1, "field2": 2},
                            {"field1": 3, "field2": 4}])
        with self.assertRaises(AttributeError):
            coll1.field3

    def test_index(self):
        """Test for indexing a ``Collection`` object.
        """
        coll1 = self.Coll1([{"field1": 1},
                            {"field1": 2}])
        self.assertEqual(coll1[0], coll1.items[0])
        self.assertEqual(coll1[1], coll1.items[1])
        with self.assertRaises(IndexError):
            coll1[2]

    def test_lenght(self):
        """Test for the length of a ``Collection`` object.
        """
        coll1 = self.Coll1([])
        self.assertEqual(len(coll1), 0)

        coll2 = self.Coll1([{}, {}])
        self.assertEqual(len(coll2), 2)

    def test_iteration(self):
        """Test for iterating a ``Collection`` object.
        """
        coll1 = self.Coll1([{"field1": 1},
                            {"field1": 2}])
        i = 0
        for item in coll1:
            i += 1
            self.assertEqual(item["field1"], i)
