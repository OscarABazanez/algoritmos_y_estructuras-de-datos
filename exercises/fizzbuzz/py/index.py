from collections import Counter


def fizzbuzz(n):
    for num in range(n):
        # if i % 15 == 0 :
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

print(fizzbuzz(5))
# print(reverse("apple 1231111"))
