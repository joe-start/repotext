import re

def check_for_sensitive_info(content):
    """
    Check for and replace sensitive information in the content.
    """
    # Pattern for potential API keys (alphanumeric string of 32-40 characters)
    api_key_pattern = re.compile(r'\b[A-Za-z0-9]{32,40}\b')
    
    # Pattern for potential passwords (any string following "password = " or "password:")
    password_pattern = re.compile(r'(password\s*[=:]\s*)("[^"]+"|\'[^\']+\'|\S+)')
    
    # Replace API keys
    content = api_key_pattern.sub('[API_KEY_REDACTED]', content)
    
    # Replace passwords
    content = password_pattern.sub(r'\1[PASSWORD_REDACTED]', content)
    
    return content