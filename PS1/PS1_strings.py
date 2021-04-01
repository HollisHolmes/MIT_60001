def count_vowels(letters):
    """Return number of vowels in a string"""
    count = 0
    for letter in letters:
        if letter in 'aeiou':
            count += 1
    return count

def count_bob(letters):
    '''Return number of time string bob occurs in letters'''
    count = 0
    input_len = len(letters)
    for i in range(input_len-2):
        if letters[i:i+3] == 'bob':
            count += 1
    return count

def longest_substring(letters):
    '''Return longest substring in alphabetical order'''
    longest_str = ''
    input_len = len(letters)
    prev = ''
    for i in range(input_len):
        cur = letters[i]
        if cur >= prev[-1:]:
            prev += cur
            if len(prev) > len(longest_str):
                longest_str = prev
        else:
            prev = cur

    return longest_str

        
#q1
# print('Number of vowels: {}'.format(count_vowels(s)))
#q2
# print('Number of times bob occurs is: {}'.format(count_bob(s)))
#q3
# print('Longest substring in alphabetical order is: {}'.format(longest_substring(s)))
