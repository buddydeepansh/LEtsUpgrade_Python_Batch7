# prime function using unit testing
import unittest


class sample(unittest.TestCase):
    def test_isPrime(self):
        n = int(input("Enter a number:"))
        bool1 = True
        if n == 0:
            print("Invalid!!!")
            return False
        elif n == 1 or n == 2:
            print("Prime Number")
            return True
        else:
            for i in range(2, n):
                if n % i == 0:
                    bool1 = False
                    break
            if bool1:
                print("Prime Number")
                return True
            else:
                print("Not prime")
                return False



if __name__ == '__main__':
    unittest.main()


# generator object armstrong program
def isArm():
    j = 1
    count = 0
    while j < 1000:

        order = len(str(j))

        sum = 0
        temp = j
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        # display the result
        if j == sum:
            yield j
            count+=1
        j += 1

x = list(isArm())
print(x)