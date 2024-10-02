import unittest
import tempfile
import os
from repotext.utils import get_file_order, analyze_dependencies, get_project_structure

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        
        # Create some test files
        open(os.path.join(self.temp_dir, 'main.py'), 'w').close()
        open(os.path.join(self.temp_dir, 'utils.py'), 'w').close()
        open(os.path.join(self.temp_dir, 'test_main.py'), 'w').close()

    def tearDown(self):
        for root, dirs, files in os.walk(self.temp_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.temp_dir)

    def test_get_file_order(self):
        order = get_file_order(self.temp_dir)
        self.assertEqual(len(order), 3)
        self.assertTrue(order[0].endswith('main.py'))
        self.assertTrue(order[-1].endswith('test_main.py'))

    def test_analyze_dependencies(self):
        with open(os.path.join(self.temp_dir, 'main.py'), 'w') as f:
            f.write("import os\nfrom utils import helper")
        
        deps = analyze_dependencies(self.temp_dir)
        self.assertIn('os', deps)
        self.assertIn('utils', deps)

    def test_get_project_structure(self):
        structure = get_project_structure(self.temp_dir)
        self.assertIn('main.py', structure)
        self.assertIn('utils.py', structure)
        self.assertIn('test_main.py', structure)

if __name__ == '__main__':
    unittest.main()