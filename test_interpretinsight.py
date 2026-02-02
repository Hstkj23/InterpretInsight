# test_interpretinsight.py
"""
Tests for InterpretInsight module.
"""

import unittest
from interpretinsight import InterpretInsight

class TestInterpretInsight(unittest.TestCase):
    """Test cases for InterpretInsight class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InterpretInsight()
        self.assertIsInstance(instance, InterpretInsight)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InterpretInsight()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
