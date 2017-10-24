import pydeepl
import unittest


class BasicTests(unittest.TestCase):
    def test(self):
        for e in [
                {
                    "sentence": "I like turtles.",
                    "from_language": "EN",
                    "to_language": "ES",
                    "result": "Me gustan las tortugas."
                }]:
            # Origin language provided
            translation = pydeepl.translate(e["sentence"], e["to_language"], e["from_language"])
            self.assertEqual(translation, e["result"])
            # Using auto-detection
            translation = pydeepl.translate(e["sentence"], e["to_language"])
            self.assertEqual(translation, e["result"])

    def test_exceptions(self):
        sentence = 'I like turtles.'
        # Language not available
        with self.assertRaises(pydeepl.TranslationError):
            pydeepl.translate(sentence, "XX")
        # Empty text
        with self.assertRaises(pydeepl.TranslationError):
            pydeepl.translate(None, "EN")
        # Text too long
        with self.assertRaises(pydeepl.TranslationError):
            pydeepl.translate("a" * 5001, "EN")

if __name__ == "__main__":
    unittest.main()
