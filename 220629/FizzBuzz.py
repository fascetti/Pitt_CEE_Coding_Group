import utils.fizzbuzz_utils as f


def fizzbuzz(n):
    for i in range(1, n + 1):
        fizz, buzz = f.fizzbuzz_util(i)
        f.fizzbuzz_print(i, fizz, buzz)


fizzbuzz(30)
