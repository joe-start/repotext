import unittest
from repotext.compressor import compress_text, decompress_text

class TestCompressor(unittest.TestCase):

    def test_compression_decompression(self):
        original_text = "This is a test string for compression and decompression."
        compressed = compress_text(original_text)
        decompressed = decompress_text(compressed)
        
        self.assertNotEqual(original_text, compressed)
        self.assertEqual(original_text, decompressed)

    def test_compression_reduces_size(self):
        long_text = "This is a long string " * 1000
        compressed = compress_text(long_text)
        
        self.assertLess(len(compressed), len(long_text))

if __name__ == '__main__':
    unittest.main()