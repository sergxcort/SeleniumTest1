"""Doc string
here is a phone numbers 123-45-67
123-54-65
123-45-67
123-54-65
123-45-67
"""
import unittest
from XML_Parser import Read_replace_save, Phone_email_replace


class TestClass(unittest.TestCase):

    def setUp(self):

        xml_file = Read_replace_save('XML_file.xml')
        self.string = Phone_email_replace(xml_file.open)

        #text_phone_file = Read_replace_save('XML_file.xml')
        #phone_numbers = Phone_email_replace(text_phone_file.open)




    def tearDown(self):
        pass#self.xml_file.close()


    def test_phone_change_Value_returned_correct(self):
        self.assertEquals('987-65-54\n32-32-32', self.string.phone_change('987-65-54'))

    def test_phone_change_Value_returned_incorrect(self):
        self.assertEquals('123-45-67\n32-32-32', self.string.phone_change('987-65-54'))









if __name__ == '__main__':
    unittest.main(verbosity=2)