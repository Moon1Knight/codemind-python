def sort_words(s):
    vowels = 'aeiouAEIOU'
    words = s.split()

    sorted_words = []
    for word in words:
        consonants = ''.join(sorted([char for char in word if char not in vowels]))
        sorted_word = ''
        c_index = 0

        for char in word:
            if char in vowels:
                sorted_word += char
            else:
                sorted_word += consonants[c_index]
                c_index += 1

        sorted_words.append(sorted_word)

    sorted_string = ' '.join(sorted_words)
    return sorted_string

# Example usage
input_string = input()
output_string = sort_words(input_string)
print(output_string)
