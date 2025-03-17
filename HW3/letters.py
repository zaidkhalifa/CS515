# String of lowercase letters to use with index()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Dictionary for the ordinal cases other than 'th' (only applies for 1-26)
special_cases = {1: 'st', 2: 'nd', 3: 'rd', 21: 'st', 22: 'nd', 23: 'rd'}

try:
    while True:
        user_input = input('Enter a letter: ').lower()
        
        # Check for stop condition
        if user_input == 'stop':
            print('Goodbye.')
            break
        
        # Validate input
        if len(user_input) != 1:
            print('Please enter a single letter.')
            continue
            
        if user_input not in alphabet:
            print('Please enter a letter from the English alphabet.')
            continue
        
        # Get position (adding 1 since index starts at 0)
        position = alphabet.index(user_input) + 1
        print(f"'{user_input}' is the {position}{special_cases.get(position, 'th')} letter of the alphabet.")
        
except KeyboardInterrupt:
    print('\nGoodbye.')
except EOFError:
    print('Goodbye.')