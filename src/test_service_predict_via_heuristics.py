from parameterized import parameterized
import unittest

import service_predict_via_heuristics

class TestPredictViaHeuristics(unittest.TestCase):

    @ parameterized.expand([
        ('IsCar [Boolean]', 'IsCar', 'Boolean'),
        ('isCar [Boolean]', 'isCar', 'Boolean'),
        ('CanCreate [Boolean]', 'CanCreate', 'Boolean'),
        ('canCreate [Boolean]', 'canCreate', 'Boolean'),
        ('ShouldCopy [Boolean]', 'ShouldCopy', 'Boolean'),
        ('shouldCopy [Boolean]', 'shouldCopy', 'Boolean'),
    ])
    def test_excluding(self, description, property_name, expected):
        # Arrange
        # Act
        actual = service_predict_via_heuristics.predict_type_from_name(property_name)

        # Assert
        self.assertEqual(expected, actual, f'test: {description}')

if __name__ == '__main__':
    unittest.main()
