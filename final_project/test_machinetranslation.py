import unittest
from machinetranslation import translator

class TestMachineTranslations(unittest.TestCase):

  def test_frenchToEnglish(self):
    self.assertEqual(translator('Bonjour, comment vous êtes aujourd\'hui?', 'fr-en'), 'Hello, how are you today?')
    self.assertNotEqual(translator('Bonjour, comment vous êtes aujourd\'hui?', 'fr-en'), "Bonjour, comment vous êtes aujourd'hui?")


  def test_englishToFrench(self):
    self.assertEqual(translator('Hello, how are you today?', 'en-fr'), 'Bonjour, comment vous êtes aujourd\'hui?')
    self.assertNotEqual(translator('Hello, how are you today?', 'en-fr'), 'Hello, how are you today?')

