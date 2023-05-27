def generate_sequence(input_string):
    vowels = set('aeiou')
    output_string = ''
    input_string = input_string.lower()
    prev_char = ''
    prev_char_type = ''
    
    for char in input_string:
        char_type = 'V' if char in vowels else 'C'
        if char_type == prev_char_type:
            continue
        output_string += char_type
        prev_char = char
        prev_char_type = char_type
    
    return output_string.upper()
    
print(generate_sequence(input()))