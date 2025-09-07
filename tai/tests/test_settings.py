"""
Tests for Settings Module
"""

import unittest
import tempfile
import os
from pathlib import Path

from ..config.settings import Settings


class TestSettings(unittest.TestCase):
    """Test cases for Settings class."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.env_file = self.temp_dir / '.env'
        self.settings = Settings(str(self.env_file))

    def tearDown(self):
        """Clean up test fixtures."""
        # Remove temp directory
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_initialization(self):
        """Test settings initialization."""
        self.assertIsInstance(self.settings._config, dict)
        self.assertTrue(len(self.settings._config) > 0)

    def test_get_method(self):
        """Test getting configuration values."""
        # Test existing key
        self.assertIsNotNone(self.settings.get('openai_model'))

        # Test non-existent key
        self.assertIsNone(self.settings.get('nonexistent'))

        # Test default value
        self.assertEqual(self.settings.get('nonexistent', 'default'), 'default')

    def test_set_method(self):
        """Test setting configuration values."""
        self.settings.set('test_key', 'test_value')
        self.assertEqual(self.settings.get('test_key'), 'test_value')

    def test_api_key_methods(self):
        """Test API key specific methods."""
        # Initially no API key
        self.assertIsNone(self.settings.get_openai_api_key())
        self.assertFalse(self.settings.is_ai_enabled())

        # Set API key
        self.settings.set_openai_api_key('sk-test-key')
        self.assertEqual(self.settings.get_openai_api_key(), 'sk-test-key')
        self.assertTrue(self.settings.is_ai_enabled())

    def test_save_and_load(self):
        """Test saving and loading configuration."""
        # Set some values
        self.settings.set('test_key', 'test_value')
        self.settings.set_openai_api_key('sk-test-key')

        # Save configuration
        self.assertTrue(self.settings.save())

        # Create new settings instance
        new_settings = Settings(str(self.env_file))

        # Check if values were loaded
        self.assertEqual(new_settings.get('test_key'), 'test_value')
        self.assertEqual(new_settings.get_openai_api_key(), 'sk-test-key')

    def test_ai_config(self):
        """Test AI configuration retrieval."""
        self.settings.set_openai_api_key('sk-test-key')
        ai_config = self.settings.get_ai_config()

        self.assertIsInstance(ai_config, dict)
        self.assertIn('api_key', ai_config)
        self.assertIn('model', ai_config)
        self.assertIn('max_tokens', ai_config)

    def test_to_dict(self):
        """Test conversion to dictionary."""
        config_dict = self.settings.to_dict()
        self.assertIsInstance(config_dict, dict)
        self.assertTrue(len(config_dict) > 0)

    def test_reset_to_defaults(self):
        """Test resetting to defaults."""
        # Modify some settings
        self.settings.set('test_key', 'test_value')
        self.settings.set_openai_api_key('sk-test-key')

        # Reset
        self.settings.reset_to_defaults()

        # Check if reset worked
        self.assertIsNone(self.settings.get('test_key'))
        self.assertIsNone(self.settings.get_openai_api_key())


if __name__ == '__main__':
    unittest.main()
