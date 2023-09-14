import unittest
import random
from WordleDictionary import FIVE_LETTER_WORDS


class TestWords(unittest.TestCase):
    def test_dictionaryHasWord(self):
        word = "aahed"
        test = FIVE_LETTER_WORDS[0]
        self.assertEqual(word, test, "Should be equal")
        self.assertIn(word, FIVE_LETTER_WORDS)

    def test_dictionaryWithoutWord(self):
        nonWord = "aaaaa"
        self.assertNotIn(nonWord, FIVE_LETTER_WORDS)


class TestRandomWordSelector(unittest.TestCase):
    def test_checkRandomWord(self):
        randomWord = random.choice(FIVE_LETTER_WORDS)
        self.assertIn(randomWord, FIVE_LETTER_WORDS, "Random word in list")
