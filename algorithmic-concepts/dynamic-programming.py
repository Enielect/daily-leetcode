# Those who cannot remember the past are condemned to repeat it.

# ways to solve dp: 1. Tabulation (bottom up) 2. Memoization (up down)

######33 First Recursion patterns
    
# sum of first N numbers:
def sum_of_n(n: int, lvl):
    if lvl == n:
        return lvl
    return sum_of_n(n, lvl+1) + lvl

# using parameterization (acc to striver)

def sum_of_n_parameterization(lvl, sum):
    if lvl < 1:
        print(sum)
        return
    sum_of_n_parameterization(lvl - 1, sum + lvl)
    # so we say in this method, tha twe increased the parameter value for the sum variable, and in the end 
    # of the day we printed it.
    
def factorial(n): 
    if n == 1:
        return 1
    return factorial(n - 1) * n

# reversing an array using recursion
# using the swapping technique
def reverse_arr(l, r, arr: list[int]):
    if l == len(arr) // 2: # if l >= r:
        return arr
    left = arr[l]
    arr[l], arr[r] = arr[r], left 
    return reverse_arr(l + 1, r - 1, arr)
    
# improve reverse_arr
def reverse_arr_improved(l, arr: list[int]):
    n = len(arr)
    if l == n // 2:
        return
    left = arr[l]
    arr[l], arr[n - l - 1] = arr[n - l - 1], left
    reverse_arr_improved(l + 1, arr)
    
    
# check if a string is palindrome or not

def check_palindrome(l, s: str):
    n = len(s)
    if l == n // 2:
        return True
    if s[l] != s[n - l - 1]: return False
    return check_palindrome(l + 1, s)


# generating all the subsequences of a list using power set and recursion.
def generate_subsequence(idx, arr, test_arr):
    # take or not take
    if idx >= len(arr):
        print(test_arr)
        return
    test_arr.append(arr[idx])
    generate_subsequence(idx + 1, arr, test_arr)
    if test_arr: test_arr.pop()
    generate_subsequence(idx + 1, arr, test_arr)
    

# return the list of subsequence whose sum == k, only print 1 of this kind of result.
def subsequence_sum_k(idx, arr, test_arr, sum, k):
    if idx >= len(arr):
        if sum == k:
            print(test_arr, 'sum')
            return True
        return False
    test_arr.append(arr[idx])
    sum += arr[idx]
    if (subsequence_sum_k(idx + 1, arr, test_arr, sum, k)):
        return True
    if test_arr: 
        sum -= test_arr.pop()
    if (subsequence_sum_k(idx + 1, arr, test_arr, sum, k)):
        return True
    return False # I am still not sure why this is here.

# Find the number of subsequences with the sum = k
def no_subsequence_sum_k(idx, arr, sum, k):
    if idx >= len(arr):
        if sum == k:
           return 1
        return 0
    sum += arr[idx]
    a = no_subsequence_sum_k(idx + 1, arr, sum, k)
    sum -=arr[idx]
    b = no_subsequence_sum_k(idx + 1, arr, sum, k)
    return a + b

print(sum_of_n_parameterization(10, 0))
print(factorial(5))
print(reverse_arr(0, 2, [1,2,3]))
arr = [1,3,4]
reverse_arr_improved(0, arr)
print(arr)
print(check_palindrome(0, 'abaa'))
generate_subsequence(0, [1,2,3], [])
subsequence_sum_k(0, [1,1,2], [], 0, 2)
print(no_subsequence_sum_k(0, [1,1,2], 0, 2))
# print(sum_of_n(10, 1)) 
