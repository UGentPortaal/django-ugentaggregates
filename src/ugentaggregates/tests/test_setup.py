import unittest


class SetupTestCase(unittest.TestCase):
    """Tests for setting up package ``ugentaggregates``.
    """

    def test_import(self):
        """Test for importing package ``ugentaggregates``.
        """
        try:
            import ugentaggregates
            import ugentaggregates.aggregates
            import ugentaggregates.collection
            import ugentaggregates.utils  # NOQA
        except:
            self.fail()
