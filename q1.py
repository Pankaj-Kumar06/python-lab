import math
def factorial(n):
    if n<0:
        print("undifined")
        return None 
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def is_prime(n):
    if n < 2 :
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    else:
        return True
def fabno(n):
    if n<0:
        return 0
    elif n==1:
        return 1
    else:
        return fabno(n-2) + fabno(n-1)
def main():
    n = int(input("enter a number:"))
    print(is_prime(n))
    print(factorial(n))
    print(fabno(n))
if __name__ == "__main__":
    main()