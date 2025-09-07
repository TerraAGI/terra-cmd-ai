"""
Tests for Command Patterns Module
"""

import unittest

from ..commands.patterns import CommandPatterns


class TestCommandPatterns(unittest.TestCase):
    """Test cases for CommandPatterns class."""

    def setUp(self):
        """Set up test fixtures."""
        self.patterns = CommandPatterns()

    def test_initialization(self):
        """Test pattern initialization."""
        self.assertIsInstance(self.patterns._patterns, dict)
        self.assertTrue(len(self.patterns._patterns) > 0)

    def test_get_pattern(self):
        """Test pattern retrieval."""
        # Test known patterns
        self.assertEqual(self.patterns.get_pattern('list files'), 'ls -la')
        self.assertEqual(self.patterns.get_pattern('go home'), 'cd ~')

        # Test unknown pattern
        self.assertEqual(self.patterns.get_pattern('unknown command'), '')

    def test_get_all_patterns(self):
        """Test getting all patterns."""
        all_patterns = self.patterns.get_all_patterns()
        self.assertIsInstance(all_patterns, dict)
        self.assertTrue(len(all_patterns) > 0)

        # Should contain known patterns
        self.assertIn('list files', all_patterns)
        self.assertIn('go home', all_patterns)

    def test_get_pattern_count(self):
        """Test pattern count."""
        count = self.patterns.get_pattern_count()
        self.assertIsInstance(count, int)
        self.assertTrue(count > 0)

    def test_search_patterns(self):
        """Test pattern search."""
        # Search for 'list'
        results = self.patterns.search_patterns('list')
        self.assertIsInstance(results, dict)
        self.assertTrue(len(results) > 0)

        # Should contain list-related commands
        self.assertIn('list files', results)

        # Search for non-existent term
        empty_results = self.patterns.search_patterns('nonexistent')
        self.assertEqual(len(empty_results), 0)


if __name__ == '__main__':
    unittest.main()
