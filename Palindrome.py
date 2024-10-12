
def check_palindrome(n):
    reverse = 0
   temp = n
    while temp != 0:
        reverse = reverse * 10 + temp % 10
        temp = temp // 10
       return reverse == n
 # Sample Input
n = 12321
if check_palindrome(n):
      print("Yes")
else:
      print("No")
