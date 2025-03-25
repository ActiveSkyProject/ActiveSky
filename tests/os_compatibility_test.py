import unittest
import platform
from website import create_app

class OperatingSystemTest(unittest.TestCase):
    def test_os_compatibility(self):
        """Test if the current operating system is supported"""
        current_os = platform.system()
        supported_os = ['Windows', 'Darwin', 'Linux']  # Darwin is macOS

        self.assertIn(current_os, supported_os, f"Current OS {current_os} is not in the list of supported operating systems")

        # Create a simple app instance to verify it works on the current OS
        test_app = create_app()
        self.assertIsNotNone(test_app, "App could not be created on this operating system")

if __name__ == '__main__':
    unittest.main()