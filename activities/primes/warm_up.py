from glob import glob

from nltk import word_tokenize

# A prime number is a whole number greater than 1 whose only factors are 1 and
# itself.

# Write a function called `is_prime` that returns True for primes and False
# for non-primes.


def is_prime(n):
    """Everything is prime!!!"""
    return True


if __name__ == '__main__':
    test = int(input('Enter a number to see if it is prime: '))
    if is_prime(test):
        print(f'{test} is prime!')
    else:
        print(f"{test} is not prime, but I'm sure you're a good person.")
    print('Iterating over files in this directory...')
    for each in sorted(glob('*.txt')):
        with open(each) as the_file:
            if is_prime(len(word_tokenize(the_file.read()))):
                print(each)
