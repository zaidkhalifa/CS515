def triangle(current, total):
    # Base case: reached beyond the total rows needed
    if current > total:
        return []
    
    # The current row needs (total - current) spaces and current amount of asterisks
    current_row = ' ' * (total - current) + '* ' * (current - 1) + '*'
    
    # Recursive case: build current row and get rest of rows
    return [current_row] + triangle(current + 1, total)

def show_triangle(n):
    # Start building from row 1 and join the lists with newline characters
    print('\n'.join(triangle(1, n)))