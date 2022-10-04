from tkinter.font import families
import unittest
import os
from gedFileParser import gedFileParser
from test_features import birth_before_marriage, us05
from models import individual, family



cur_path = os.path.dirname(__file__)

FAIL_DIR = "gedcom_files/fail/"
PASS_DIR = "gedcom_files/pass/"
acceptfile = "Team3-gedcom-testFile.ged"
fail_file = os.path.relpath("..\\" + FAIL_DIR + acceptfile, cur_path)
pass_file = os.path.relpath("..\\" + PASS_DIR + acceptfile, cur_path)

#  = "src/testFile_incorrectData.ged"
fail_file1='/Users/bharath/Documents/CS555-gedcom/CS555-GEDCOM/Sprint_1/src/testFile_incorrectData.ged'
 
class test_birth_before_marriage(unittest.TestCase):
    def test_birth_before_marriage_1(self):
        individuals, families = gedFileParser(acceptfile)
        self.assertTrue(birth_before_marriage(individuals, families), 'Test value is not true')

    def test_birth_before_marriage_2(self):
        individuals, families = gedFileParser(pass_file)
        for family in families:
            if family.fam_marr:
                husband = None
                wife = None
                for indiv in individuals:
                    if indiv.uniqueId == family.husband:
                        husband = indiv
                    if indiv.uniqueId == family.wife:
                        wife = indiv
                self.assertNotEquals(husband.indi_birth, wife.indi_birth)

    def test_birth_before_marriage_3(self):
        individuals, families = gedFileParser(fail_file)
        self.assertFalse(birth_before_marriage(individuals, families))

    def test_birth_before_marriage_4(self):
        individuals, families = gedFileParser(pass_file)
        self.assertIsNot(individuals, families)

    def test_birth_before_marriage_5(self):
        individuals, families = gedFileParser(pass_file)
        self.assertNotIsInstance(families,individuals)


class test_marriage_before_death(unittest.TestCase):
    def test_birth_before_death1(self):

        individuals, _ = gedFileParser(pass_file)
        self.assertTrue(us05(individuals))

    def test_marriage_before_death2(self):

        individuals, _ = gedFileParser(pass_file)
        self.assertEqual(us05(individuals),True)

    def test_marriage_before_death3(self):

        individuals, _ = gedFileParser(pass_file)
        self.assertIsNot(us05(individuals),False)

    def test_marriage_before_death4(self):

        individuals, _ = gedFileParser(fail_file1)
        self.assertIsNotNone(us05(families),True)

    def test_marriage_before_death5(self):
        individuals, _ = gedFileParser(pass_file)
        self.assertIs(us05(individuals),True)
if __name__ == '__main__':
    print("Inside unittest")
    unittest.main()
