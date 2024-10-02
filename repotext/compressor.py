import gzip
import base64

def compress_text(text):
    """
    Compress the given text using gzip and encode it in base64.
    """
    compressed = gzip.compress(text.encode('utf-8'))
    return base64.b64encode(compressed).decode('utf-8')

def decompress_text(compressed_text):
    """
    Decompress the given base64-encoded gzipped text.
    """
    decoded = base64.b64decode(compressed_text.encode('utf-8'))
    return gzip.decompress(decoded).decode('utf-8')