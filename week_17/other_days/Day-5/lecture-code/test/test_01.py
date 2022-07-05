import unittest
from  problem_1 import Cat


# class TestCatInitialize(unittest.TestCase):
#     def test_initialize_cat_with_color(self):
#         # arrange
#         color = "black"
#         test_cat = Cat(color, 4)
#         # act
#         result = test_cat._color
#         # assert
#         self.assertEqual(result, color)


#     def test_initialize_cat_with_age(self):
#         # arrange
#         age = 5
#         test_cat = Cat("pink", 5)
#         # act
#         result = test_cat.age
#         # assert
#         self.assertEqual(result, age)




def test_initialize_cat_with_color():
    # arrange
    color = "black"
    test_cat = Cat(color, 4)
    print("Are we here?")
    # act
    result = test_cat._color
    # assert
    assert result == color


def test_initialize_cat_with_age():
    # arrange
    age = 5
    test_cat = Cat("pink", 5)
    # act
    result = test_cat.age
    # assert
    assert result == age