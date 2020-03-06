import unittest
import FizzBuzz

class TestsFizzBuzz(unittest.TestCase):

    def testReturnsEmptyStringIfInputNotMultipleOfThreeNorFive(self):
        input = 2
        expectedOutput = ''
        self.assertEqual(FizzBuzz.fizzBuzz(input), expectedOutput)

    def testReturnFizzIfNumberIsMultipleOfThree(self):
        input = 9
        expectedOutput = 'fizz'
        self.assertEqual(FizzBuzz.fizzBuzz(input), expectedOutput)

    def testReturnFizzIfNumberIsMultipleOfThree(self):
        input = 10
        expectedOutput = 'buzz'
        self.assertEqual(FizzBuzz.fizzBuzz(input), expectedOutput)

if __name__ == '__main__':
    unittest.main()