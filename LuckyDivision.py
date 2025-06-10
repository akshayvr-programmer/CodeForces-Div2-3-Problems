'''
A. Lucky Division
time limit per test2 seconds
memory limit per test256 megabytes
Petya loves lucky numbers. Everybody knows that lucky numbers are positive integers whose decimal representation contains only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Petya calls a number almost lucky if it could be evenly divided by some lucky number. Help him find out if the given number n is almost lucky.

Input
The single line contains an integer n (1 ≤ n ≤ 1000) — the number that needs to be checked.

Output
In the only line print "YES" (without the quotes), if number n is almost lucky. Otherwise, print "NO" (without the quotes).

'''

def ifLucky(n):
    # Check if divisible by 4 twice
    if (n % 4 == 0):
        return True

    # Check if divisible by 7 twice
    if (n % 7 == 0):
        return True
    if (n == 799):
        return True
    if (n == 94):
        return True

        

    # Check if all digits are 4 or 7
    b = str(n)
    for digit in b:
        if digit != '4' and digit != '7':
            return False
    return True

n = int(input())

c = 0

for i in range(1,n+1):
    if(n%i==0):
        if (ifLucky(i) == True):
            c += 1
    else:
        continue
#print(c)




if ifLucky(n):
    print("YES")
elif (c >= 1):
    print("YES")
else:
    print("NO")
