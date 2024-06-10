import unittest

from split_blocks import markdown_to_blocks


class TestSplitBlocks(unittest.TestCase):
    def test_split(self):
        block = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        block_tests = markdown_to_blocks(block)
        split_blocks = ['\nThis is **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', '* This is a list\n* with items\n']  

        self.assertEqual(block_tests, split_blocks)      