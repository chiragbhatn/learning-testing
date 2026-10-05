import unittest


class Animal: pass
class Dog(Animal): pass


def find_user(users, name):
    return users.get(name)  # returns None when missing


def is_adult(age):
    return age >= 18


class TestAssertions(unittest.TestCase):
    def test_assertIsInstance(self):
        d = Dog()
        self.assertIsInstance(d, Dog)
        self.assertIsInstance(d, Animal)      # subclasses count
        self.assertIsInstance(3.5, (int, float))  # tuple of classes works
        self.assertNotIsInstance("5", int)

    def test_assertIsNone(self):
        users = {"alice": 30}
        self.assertIsNone(find_user(users, "bob"))
        self.assertIsNotNone(find_user(users, "alice"))
        self.assertIsNotNone(0)  # 0 is falsy but NOT None

    def test_assertFalse(self):
        self.assertFalse(is_adult(10))
        self.assertFalse([])      # empty list is falsy
        self.assertFalse("")
        self.assertFalse(0)
        self.assertFalse(None)

    def test_assertIs(self):
        a = [1, 2]
        b = a
        c = [1, 2]
        self.assertIs(a, b)        # same object
        self.assertEqual(a, c)     # equal value...
        self.assertIsNot(a, c)     # ...but different objects
        self.assertIs(None, None)
        self.assertIs(True, 1 == 1)

    def test_assertIn(self):
        self.assertIn(3, [1, 2, 3])
        self.assertIn("ell", "hello")
        self.assertIn("name", {"name": "Sam"})   # checks keys
        self.assertNotIn("Sam", {"name": "Sam"})  # not values
        self.assertIn(2, (1, 2))


if __name__ == "__main__":
    unittest.main(verbosity=2)
