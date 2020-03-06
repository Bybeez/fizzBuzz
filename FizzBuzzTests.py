import unittest
import FizzBuzz

class TestsFizzBuzz(unittest.TestCase):

    def testReturnsEmptyStringIfInputNotMultipleOfThreeNorFive(self):
        input = 2
        expectedOutput = ''
        self.assertEqual(FizzBuzz.fizzBuzz(input), expectedOutput)

if __name__ == '__main__':
    unittest.main()