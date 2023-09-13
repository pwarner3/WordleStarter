import unittest
from WordleDictionary import FIVE_LETTER_WORDS

class TestRandomWordSelector(unittest.TestCase):
    def test_dictionary(self):
        word = "aahed"
        test = FIVE_LETTER_WORDS[0]
        self.assertEqual(word,test,"Should be equal")
        self.assertIn("abort",FIVE_LETTER_WORDS)

class TestWords(unittest.TestCase):
    def test_checkRealWord(self):
        self.assertEqual(1,1,"Test")