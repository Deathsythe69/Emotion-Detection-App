import unittest
from emotion_package import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_output(self):
        result = emotion_detector("I am so happy today!")
        self.assertIsNotNone(result, "emotion_detector returned None")
        self.assertIn("joy", result)
        self.assertEqual(result["dominant_emotion"], "joy")

if __name__ == '__main__':
    unittest.main()
