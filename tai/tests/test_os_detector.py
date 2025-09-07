"""
Tests for OS Detector Module
"""

import unittest
from unittest.mock import patch

from ..core.os_detector import OSDetector


class TestOSDetector(unittest.TestCase):
    """Test cases for OSDetector class."""

    def setUp(self):
        """Set up test fixtures."""
        self.detector = OSDetector()

    def test_os_detection(self):
        """Test basic OS detection."""
        # These will vary based on the actual system
        self.assertIsInstance(self.detector.system, str)
        self.assertIsInstance(self.detector.distro, str)
        self.assertIsInstance(self.detector.version, str)
        self.assertIsInstance(self.detector.machine, str)

    def test_get_os_info(self):
        """Test OS info formatting."""
        os_info = self.detector.get_os_info()
        self.assertIsInstance(os_info, str)
        self.assertTrue(len(os_info) > 0)

    def test_get_detailed_info(self):
        """Test detailed OS information."""
        info = self.detector.get_detailed_info()
        self.assertIsInstance(info, dict)
        self.assertIn('system', info)
        self.assertIn('distro', info)
        self.assertIn('version', info)
        self.assertIn('machine', info)
        self.assertIn('display_name', info)

    def test_os_type_checks(self):
        """Test OS type checking methods."""
        # These should be mutually exclusive
        checks = [
            self.detector.is_linux(),
            self.detector.is_macos(),
            self.detector.is_windows()
        ]
        # At least one should be True
        self.assertTrue(any(checks))

    def test_shell_type(self):
        """Test shell type detection."""
        shell = self.detector.get_shell_type()
        self.assertIn(shell, ['bash', 'zsh', 'cmd', 'powershell'])


if __name__ == '__main__':
    unittest.main()
