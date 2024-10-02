import unittest
import tempfile
import os
from repotext.diff_generator import generate_diff

class TestDiffGenerator(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        os.rmdir(self.temp_dir)

    def test_generate_diff(self):
        old_content = ['line 1', 'line 2', 'line 3']
        new_content = ['line 1', 'line 2 modified', 'line 4']

        # First run to create the .last_repotext_pack.txt file
        generate_diff(old_content, self.temp_dir)

        # Generate diff
        diff = generate_diff(new_content, self.temp_dir)

        self.assertIn('  line 1', diff)
        self.assertIn('- line 2', diff)
        self.assertIn('+ line 2 modified', diff)
        self.assertIn('- line 3', diff)
        self.assertIn('+ line 4', diff)

if __name__ == '__main__':
    unittest.main()