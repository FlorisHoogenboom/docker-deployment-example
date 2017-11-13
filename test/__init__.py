import unittest

class DummyTest(unittest.TestCase):
    def test_whether_the_galaxy_still_exists(self):
        self.assertTrue(
            True,
            "Ohh no, the galaxy should exists..."
        )