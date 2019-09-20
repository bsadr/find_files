import unittest
import match_files


class RunTests(unittest.TestCase):
    def test_string(self):
        # call find_regex method
        path = '../test/data/1/'
        regexp = 'john'
        test_path = '../test/string/'
        program_result = match_files.find_regex(path, regexp)

        expected_result = []
        with open(test_path+'output.txt', 'r') as exp_result:
            for line in exp_result:
                expected_result.append(line.rstrip())
        # print(expected_result)
        self.assertEqual(sorted(expected_result), sorted(program_result))

    def test_empty_string(self):
        # call find_regex method
        path = '../test/data/1/'
        regexp = ''
        test_path = '../test/empty_string/'
        program_result = match_files.find_regex(path, regexp)

        expected_result = []
        with open(test_path+'output.txt', 'r') as exp_result:
            for line in exp_result:
                expected_result.append(line.rstrip())
        self.assertEqual(sorted(expected_result), sorted(program_result))

    def test_underline(self):
        # call find_regex method
        path = '../test/data/1'
        regexp = '_'
        test_path = '../test/underline/'
        program_result = match_files.find_regex(path, regexp)

        expected_result = []
        with open(test_path+'output.txt', 'r') as exp_result:
            for line in exp_result:
                expected_result.append(line.rstrip())
        self.assertEqual(sorted(expected_result), sorted(program_result))

    def test_space(self):
        # call find_regex method
        path = '../test/data/'
        regexp = ' '
        test_path = '../test/space/'
        program_result = match_files.find_regex(path, regexp)

        expected_result = []
        with open(test_path+'output.txt', 'r') as exp_result:
            for line in exp_result:
                expected_result.append(line.rstrip())
        self.assertEqual(sorted(expected_result), sorted(program_result))

    def test_size(self):
        # call find_regex method
        path = '../test/data/'
        regexp = ''
        max_size = 1000
        test_path = '../test/size/'
        program_result = match_files.find_regex(path, regexp, max_size)

        expected_result = []
        with open(test_path+'output.txt', 'r') as exp_result:
            for line in exp_result:
                expected_result.append(line.rstrip())
        self.assertEqual(sorted(expected_result), sorted(program_result))
        print program_result


if __name__ == "__main__":
    unittest.main()