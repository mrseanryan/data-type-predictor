from parameterized import parameterized
import unittest

import service_predict_via_heuristics

class TestPredictViaHeuristics(unittest.TestCase):
    @ parameterized.expand([
        # Boolean
        ('IsCar', 'Boolean'),
        ('isCar', 'Boolean'),
        ('CanCreate', 'Boolean'),
        ('canCreate', 'Boolean'),
        ('ShouldCopy', 'Boolean'),
        ('shouldCopy', 'Boolean'),
        ('WasActive', 'Boolean'),
        ('Active', 'Boolean'),
        ('ActiveItem', 'Boolean'),
        ('IgnoreEmptyKeys', 'Boolean'),
        ('IgnoreThis', 'Boolean'),
        ('Completed', 'Boolean'),
        ('Taken', 'Boolean'),
        ('Chosen', 'Boolean'),
        # Boolean - Fuzzy
        ('ConCreate', 'Boolean'),
        ('kanCreate', 'Boolean'),
        ('SholdCopy', 'Boolean'),
        ('shoudCopy', 'Boolean'),
        ('Actve', 'Boolean'),
        ('AtiveItem', 'Boolean'),
        ('IgnoorEmptyKeys', 'Boolean'),
        ('IgnreThis', 'Boolean'),
        ('Compltd', 'Boolean'),
        # Numeric - Integer
        ('BkdNumber', 'Integer'),
        ('NrOfRecords', 'Integer'),
        ('RowHeight', 'Integer'),
        ('FieldLength', 'Integer'),
        ('MaxWidth', 'Integer'),
        ('TopSpeed', 'Integer'),
        ('MaxVelocity', 'Integer'),
        ('ItemCount', 'Integer'),
        #('CalculatedSizeInBytes', 'Integer'),
        ('Priority', 'Integer'),
        ('TopPriority', 'Integer'),
        # Numeric - Decimal
        ('Inv_Balance', 'Decimal'),
        ('InitialBalance', 'Decimal'),
        ('BalancePaid', 'Decimal'),
        ('AmountReceived', 'Decimal'),
        ('ReceivedAmount', 'Decimal'),
        # Date
        ('UploadDate', 'Date'),
        ('DateCreated', 'Date'),
        ('ExpiresAt', 'Date'),
        ('CreatedOn', 'Date'),
        # # String
        ('Name', 'String'),
        ('BrandName', 'String'),
        ('Password', 'String'),
        ('MainPassword', 'String'),
        ('ZipCode', 'String'),
        ('EntryCode', 'String'),
        ('OrderedBy', 'String'),
        ('CustomerEmail', 'String'),
        ('HomeAddress', 'String'),
        # String - ends in language code
        ('InteriorEN', 'String'),
        ('InteriorNL', 'String'),
        # TODO xxx add more language codes via library?
        # Enumeration
        ('Color', 'Enumeration'),
        ('ItemColor', 'Enumeration'),
        ('Status', 'Enumeration'),
        ('ItemStatus', 'Enumeration'),
        ('RetrieveType', 'Enumeration'),
        ('Category', 'Enumeration'),
        ('ItemCategory', 'Enumeration')
    ])
    def test_excluding(self, property_name, expected):
        # Arrange
        # Act
        actual = service_predict_via_heuristics.predict_type_from_name(property_name)

        # Assert
        self.assertEqual(expected, actual, f'test: {property_name} = {expected}')

if __name__ == '__main__':
    unittest.main()
