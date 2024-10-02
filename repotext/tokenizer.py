import re

def count_tokens(text):
    """
    A simple tokenizer that splits on whitespace and punctuation.
    This is a basic implementation and may not accurately represent
    the tokenization used by specific AI models.
    """
    # Split on whitespace and punctuation
    tokens = re.findall(r'\b\w+\b|[^\w\s]', text)
    return len(tokens)