import unittest
from gedFileParser import parser_file
from features import birth_before_marriage, us05, us15, us16, us22_unique_ids, us23_unique_name_bday



acceptfile = "Team3-gedcom-testFile.ged"
fail_file1='testFile_incorrectData.ged'

 
class test_more_than_15_siblings(unittest.TestCase):

    def test_more_than_15_siblings(self):
        individuals, families = parser_file(fail_file1)
        self.assertTrue(us15(families))
    def test_more_than_15_siblings(self):
        individuals, families = parser_file(acceptfile)
        self.assertFalse(us15(families), "Test value is not False")

class test_birth_before_marriage(unittest.TestCase):
    def test_birth_before_marriage_1(self):
        individuals, families = parser_file(acceptfile)
        self.assertFalse(birth_before_marriage(individuals, families), 'Test value is not true')

    def test_birth_before_marriage_2(self):
        individuals, families = parser_file(acceptfile)
        self.assertTrue(individuals,families)

    def test_birth_before_marriage_3(self):
        individuals, families = parser_file(fail_file1)
        self.assertFalse(birth_before_marriage(individuals, families))

    def test_birth_before_marriage_4(self):
        individuals, families = parser_file(acceptfile)
        self.assertIsNot(individuals, families)



class test_marriage_before_death(unittest.TestCase):
      

    def test_marriage_before_death1(self):

        individuals, families = parser_file(fail_file1)
        self.assertFalse(us05(individuals, families),True)

    def test_marriage_before_death2(self):
        individuals, families = parser_file(acceptfile)
        self.assertFalse(us05(individuals, families),True)

class test_male_last_name(unittest.TestCase):
    def test_male_last_name(self):
        individuals, families = parser_file(acceptfile)
        self.assertTrue(us16(individuals, families))
    def test_male_last_name(self):
        individuals, families = parser_file(fail_file1)
        self.assertFalse(us16(individuals, families))

class test_us22(unittest.TestCase):
    def test_us22_unique_ids(self):
        individuals, families = parser_file(acceptfile)
        self.assertTrue(us22_unique_ids(individuals, families))
    def test_us22_unique_ids(self):
        individuals, families = parser_file(fail_file1)
        self.assertFalse(us22_unique_ids(individuals, families))



class test_us23(unittest.TestCase):
    def test_male_last_name(self):
        individuals, families = parser_file(fail_file1)
        self.assertFalse(us23_unique_name_bday(individuals))

if __name__ == '__main__':
    #print("Inside unittest")
    unittest.main()
