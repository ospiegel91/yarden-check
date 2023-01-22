import unittest
from src.main import Checker


class CheckerTest(unittest.TestCase):

    def test_check_index_count(self):
        checker_instance = Checker()
        results = checker_instance.check_dir("/Users/orenspiegel/desktop/projects/tmp")
        self.assertEqual(results["metadata"]["files"], 2)


if __name__ == '__main__':
    unittest.main()