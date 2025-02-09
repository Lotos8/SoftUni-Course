words = input().split()
palindromes = input()

palindrome_list = [word for word in words if word == word[::-1]]
count_of_special_palindrome = palindrome_list.count(palindromes)
print(palindrome_list)
print(f"Found palindrome {count_of_special_palindrome} times")
