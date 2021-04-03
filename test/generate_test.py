import unittest

from minimal_l_system_generator.generate import generate


class Minimal_L_System_Processor_TestCase(unittest.TestCase):
    def test_generate_success_one_iteration(self):
        n = 1
        o = "A"
        pr = {"A": "BC"}

        result = generate(o, pr, n)

        self.assertEqual(result, "BC")

    def test_generate_success_many_iterations(self):
        # example test taken from https://en.wikipedia.org/wiki/L-system#L-system_structure

        # number of iterations
        n = 7
        o = "A"
        pr = {
            "A": "AB",
            "B": "A",
        }

        result = generate(o, pr, n)

        self.assertEqual(result, "ABAABABAABAABABAABABAABAABABAABAAB")


if __name__ == '__main__':
    unittest.main()
