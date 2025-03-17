def longest_lines(filename):
    # Read all lines from file
    lines = [line.strip() for line in open(filename).readlines()]
    
    # If file is empty, return empty list
    if not lines:
        return []
    
    # Find max length
    max_length = len(max(lines, key=len))
    
    # Return all lines of that length
    return [line for line in lines if len(line) == max_length]