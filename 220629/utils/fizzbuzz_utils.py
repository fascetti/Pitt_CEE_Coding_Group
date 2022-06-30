def fizzbuzz_util(i):
    fizz, buzz = False, False
    if i % 3 == 0:
        fizz = True
    if i % 5 == 0:
        buzz = True
    return fizz, buzz


def fizzbuzz_print(i, fizz, buzz):
    if fizz and buzz:
        print(f'{i}: FizzBuzz')
    elif fizz:
        print(f'{i}: Fizz')
    elif buzz:
        print(f'{i}: Buzz')
    else:
        print(i)