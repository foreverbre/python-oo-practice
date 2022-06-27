import random  
"""Word Finder: finds random words from a dictionary.

    >>> wf = WordFinder("/Users/student/words.txt")
        3 words read

    >>> wf.random()
        'cat'

    >>> wf.random()
        'cat'

    >>> wf.random()
        'porcupine'

    >>> wf.random()
        'dog'
        """


class WordFinder:
    def __init__(self, path):
        """read dictionary and reports # items read"""
        dict_file = open(path)

        self.words = self.parse(dict_file)

        print (f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file list of words"""
        return [w.strip() for w in dict_file]

    def random(self):
        """returns random word"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments
    
    >>> swf.random() in ["mango", "apple", "kale"]
    True
    
    >>> swf.random() in ["parsnips", "apple", "kale"]
    True
    
    >>> swf.random() in ["mango", "apple", "parsnips"]
    True
    """
    
    def parse(self, dict_file):
        """Parse dict_file list of words exludes blanks/comments"""
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]