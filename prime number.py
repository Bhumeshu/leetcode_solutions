def prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print("not prime")
                return False
            else:
                print("prime")
                return True


prime(2098765437)



