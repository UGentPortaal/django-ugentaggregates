import unittest


class SetupTestCase(unittest.TestCase):
    """Tests for setting up package ``aggregates``.
    """

    def test_import(self):
        """Test for importing package ``aggregates``.
        """
        try:
            import aggregates
            import aggregates.aggregates
            import aggregates.collection
            import aggregates.utils
        except:
            self.fail()
