def is_palindrome(num):
    return str(num) == str(num)[::-1]

def closest_palindrome(target):
    smaller = target - 1
    larger = target + 1

    while True:
        if is_palindrome(smaller) and is_palindrome(larger):
            return [smaller, larger ]
        elif is_palindrome(smaller):
            return smaller
        elif is_palindrome(larger):
            return larger 
        
        smaller -= 1
        larger += 1

# Example usage:
given_number = int(input())
res = closest_palindrome(given_number)
if type(res) == list:
    print(*res)
else:
    print(res)
