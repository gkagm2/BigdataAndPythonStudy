def is_prime(value):

    for i in range(2,value):
        if (value % i == 0):
            return False
    return True


value = int(input("정수를 입력하시오: "))


print(is_prime(value))
