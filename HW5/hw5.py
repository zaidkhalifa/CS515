import re

def pequod(f):
    text = open(f).read()
    pattern = r'\bwhite\s+whale(?:\'s)?\b'
    matches = re.findall(pattern, text.lower())
    return len(matches)

def find_dotcoms(s):
    pattern = r'(?:^|\s)(?:www\d*\.)?(?:[a-zA-Z0-9-]+\.)*([a-zA-Z0-9-]+)\.com(?!\.[a-zA-Z])'
    matches = re.findall(pattern, s)
    return matches

def palindrome_re(n):
    if n <= 0:
        return r""
    
    pattern = r"^"
    
    for i in range(n // 2):
        pattern += f"(.)"

    if n % 2 == 1:
        pattern += r"."

    for i in range(n // 2, 0, -1):
        pattern += f"\\{i}"

    pattern += r"$"
    return pattern

def palindrome_direct(s):
    return s == s[::-1]