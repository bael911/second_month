def palindrome(string):
    n = str(string)
    if n == n[::-1]:
        return True
    else:
        return False

b = input("Введите число :")
print(palindrome(b))