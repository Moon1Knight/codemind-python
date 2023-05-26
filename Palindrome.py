def is_palindrome(num):
    return str(num) == str(num)[::-1]

num = int(input())
k = is_palindrome(num)
print(k)