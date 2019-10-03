import unittest
from lambdata_eyvonne.df_utils import ManageDF
from lambdata_eyvonne.df_utils import TEST_DF

row, col = TEST_DF.shape


class ManagerTest(unittest.TestCase):
    """This class tests the manageDF for common input errors"""

    def test_genData(self):
        """this function runs through being given good input"""
        factor = 3
        self.assertEqual(ManageDF(TEST_DF).genData(factor).shape,
                         (row+factor, col))

    def test_listCol(self):
        self.assertEqual(ManageDF(TEST_DF).listCol([6, 7, 8], 'c').shape,
                         (row, col+1))


if __name__ == '__main__':
    unittest.main()
