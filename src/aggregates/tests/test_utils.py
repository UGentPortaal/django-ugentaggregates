import unittest


class UtilsTestCase(unittest.TestCase):
    """Tests for module ``aggregates.utils``.
    """

    def setUp(self):
        """Set up the fixture.
        """
        class DummyObject(object):
            def __init__(self, field1):
                self.field1 = field1

        self.object1 = DummyObject("abc")
        self.dict1 = {"field1": "abc"}

    def tearDown(self):
        """Tear down the fixture.
        """
        self.object1 = None
        self.dict1 = None

    def test_has_field(self):
        """Test for function ``has_field``.
        """
        from aggregates.utils import has_field

        self.assertTrue(has_field(self.object1, "field1"))
        self.assertFalse(has_field(self.object1, "field2"))

        self.assertTrue(has_field(self.dict1, "field1"))
        self.assertFalse(has_field(self.dict1, "field2"))

    def test_get_field(self):
        """Test for function ``get_field``.
        """
        from aggregates.utils import get_field

        self.assertEqual(get_field(self.object1, "field1"), "abc")
        with self.assertRaises(AttributeError):
            get_field(self.object1, "field2")
        self.assertEqual(get_field(self.object1, "field2", "def"), "def")

        self.assertEqual(get_field(self.dict1, "field1"), "abc")
        with self.assertRaises(KeyError):
            get_field(self.dict1, "field2")
        self.assertEqual(get_field(self.dict1, "field2", "def"), "def")
