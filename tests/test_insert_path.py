# tests/test_insert_path.py
import unittest
from unittest.mock import patch
from ndpath import Ndpath


class TestInsertPath(unittest.TestCase):
    @patch("builtins.input", side_effect=["/new/path"])
    @patch("os.path.exists", return_value=True)
    def test_insert_path(self, mock_exists, mock_input):
        ndpath = Ndpath()
        ndpath.paths = ["/usr/bin", "/bin"]
        ndpath.selected_index = 0  # Ensure we are selecting the first path
        ndpath.insert_path(False)  # Insert below the selected path
        self.assertIn("/new/path", ndpath.paths, "The new path should be inserted correctly")
        self.assertEqual(
            ndpath.paths[1], "/new/path", "The new path should be at index 1, after '/usr/bin'"
        )


if __name__ == "__main__":
    unittest.main()
