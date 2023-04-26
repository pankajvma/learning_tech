import unittest 
from phonebook import PhoneBook 

class PhoneBookTest(unittest.TestCase) : 

    # setup called before every test method. It is a 'Test Fixture.
    def setUp(self) -> None: 
        self.phonebook = PhoneBook() 
    
    # tearDown called after every test method. (Fixture method) 
    # Normally used to release the resources. 
    # Since here we are not occupying any resources and the code run fully on memory, we can keep it empty.
    def tearDown(self) -> None: 
        pass 
    
    
    def test_lookup_by_name(self) :                 #Test case name should be a clear indicator of what test case is being tested. 
        self.phonebook.add("Bob", "12345")          # Arrange 
        number = self. phonebook. lookup("Bob")     # Act 
        self.assertEqual("12345", number)           # Assert
    
    
    def test_missing_name(self): 
        with self. assertRaises(KeyError):          # Assert. This check needs a Context manager. 
            self.phonebook.lookup("Bob")          # Act
    
    
    # @uniitest.skip()"WIP")                        # TO skip a test case.  
    def test_empty_phonebook_isconsistent(self) : 
        self.assertTrue(self.phonebook.is_consistent()) 
    
    
    # Poor test design example 
    # Below test case actually test mulitple functionality. so it is not clear what test passes/ fails. 
    # Also, in case an exception occurs, there are chances that some of the test cases might not execute. 
    def test_is_consistent(self): 
        self.phonebook.add("Bob", "12345")
        self.assertTrue(self. phonebook.is_consistent()) 
        self.phonebook.add("Anna", "012345")
        self.assertTrue(self. phonebook.is_consistent())
        self.phonebook.add("Sue", "12345")                      # Identical to Bob
        self.assertFalse( self.phonebook.is_consistent())  
        self.phonebook.add("Sue" , "123")                       # prefix of Bob
        self.assertFalse(self.phonebook.is_consistent()) 
    

    #Good test design examples
    def test_is_consistent_with_different_entries(self): 
        self.phonebook.add("Bob", "12345")                      # Arrange
        self.phonebook.add("Anna", "012345")
        self.assertTrue(self.phonebook.is_consistent())        # Act and Assert
    
    
    def test_is_consistent_with_duplicate_entries(self): 
        self.phonebook.add("Bob", "12345")                      # Arrange
        self.phonebook.add("Sue", "12345")
        self.assertFalse(self.phonebook.is_consistent())        # Act and Assert
     

    def test_is_consistent_with_duplicate_prefix(self): 
        self.phonebook.add("Bob", "12345")                      # Arrange
        self.phonebook.add("Sue", "123")
        self.assertFalse(self.phonebook.is_consistent())         # Act and Assert     

    # Multiple asserts 
    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add("Bob", "12345")                      # Arrange
        self.assertIn("Bob", self.phonebook.get_names())        # Act and Assert
        self.assertIn("12345", self.phonebook.get_numbers())      # Act and Assert