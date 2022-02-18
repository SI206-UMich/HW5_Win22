# Your name:
# Your student id:
# Your email:
# List who you have worked with on this homework:

import re, os, unittest

def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """

    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r', encoding='utf-8')

    # Read the lines from the file object into a list
    lines = infile.readlines()

    # Close the file object
    infile.close()

    # return the list of lines
    return lines

def find_movie_titles(string_list):
    """
    This function returns a dictionary with the keys being numbers, (1 - 8)
    and the values being the names of movies.
    """
    pass

def find_and_phrases(string_list):
    """
    This function finds all phrases with the word "and"
    and then returns them in a list.
    """
    pass

def find_urls(string_list):
    """
    This functions returns a list of valid urls in the list of strings
    """
    pass

def find_valid_release_dates(string_list):
    """
    This function returns a list of valid release dates.
    Sample format:
        mm/dd/yyyy
        mm/dd/yy
        mm-dd-yyyy
        mm-dd-yy
    Please refer to the instructions and be careful about invalid dates!
    """
    pass

## Extra credit
def count_mid_str(string_list, string):
    """
    This function returns a count of the number of times a specified string appears
    in the text. The matched string should be in the middle of a word (ie: Not at 
    the start of end of a word).
    """
    pass

#Implement your own tests
class TestAllMethod(unittest.TestCase):

    def test_find_movie_titles(self):
        pass

    def test_find_valid_release_dates(self):
        pass

    def test_find_and_phrases(self):
        pass

    def test_find_urls(self):
        pass

    #Uncomment if working on Extra Credit
    #def test_count_mid_str(self):
    #    pass


def main():
    #Feel free run your functions here as well!
    pass

if __name__ == '__main__':
    main()
    print()
    unittest.main(verbosity=2)