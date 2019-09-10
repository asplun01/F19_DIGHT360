# Classroom activities for 10 Sep 2019

##  Testing for membership using `in`

You can test whether an object is in a dict, list, set, str, tuple, etc.
using the keyword `in`:

```python
print('T/F: There is an "i" in "team":', 'i' in 'team')
print('T/F: 4 is a prime number:', 4 in [2, 3, 5, 7, 11, 13, 17, 19])
print('T/F: Bob is in The Chipmunks:', 'Bob' in ['Alvin', 'Simon', 'Theodore'])
```

## Replace text in a string using `replace()` method

Strings have a handy method to replace characters.

```python
orig_str = 'I want to hit you!'
print(orig_str, '-->', orig_str.replace('it', 'ug'))
```

`EXTRA:` What if you wanted to only replace the first two instances of the
target string? (How can you find this information?)

## Slicing sequence objects

You can access parts of strings, lists and tuples by 'slicing' them

```python
my_list = list(range(10))
print('my_list', '-->', my_list, sep='\t')
print('my_list[4]', '-->', my_list[4], sep='\t')
print('my_list[-1]', '-->', my_list[-1], sep='\t')
print('my_list[2:4]', '-->', my_list[2:4], sep='\t')
print('my_list[:4]', '-->', my_list[:4], sep='\t')
print('my_list[4:]', '-->', my_list[4:], sep='\t')
print('my_list[4:-1]', '-->', my_list[4:-1], sep='\t')
print('my_list[-3:]', '-->', my_list[-3:], sep='\t')
print("'working'[:4]", '-->', 'working'[:4], sep='\t')
print("'working'[-3:]", '-->', 'working'[-3:], sep='\t')
```


`PRACTICE A:` Write a program that asks the user for a word of at least six
letters in length, then prints back to the user on one line the first three
letters, and then on a second line prints the last three letters.

`PRACTICE B:` Modify the program to print out every other letter.

`PRACTICE C:` Modify the program to print out the word spelled backward.

## Python "standard library"

Python comes with lots of useful tools available in the "standard library".
https://docs.python.org/3/library/index.html

Some very commonly used modules include...
* re - regular expressions
* datetime - basic date and time types
* collections - useful variations on dicts, for example
* pprint - print objects prettily (with readable indentations)
* math
* random - random number generation and random sampling
* statistics
* os - interact with operating system (filesystem)
* pickle - object serialization
* csv - read/write csv data files
* html - HTML
* urllib - URL handling modules (e.g., for web scraping)


## Importing modules (`import`, `from`, and `as`)

The "namespace" is all of the names that have been assigned.
In other words, it is everything that is available to be used.

You can get a standard library module into the namespace by `import`ing it:

```python
import re
print('This is the contents of the `re` module:\n', dir(re))
```

You can also just import part of a module using `from`

```python
print('Let\'s try some math!')
from math import log
from math import e
print('What is the meaning of life, the universe, and everything?',
      log(e ** 42))  # 42
print('The value of e is', e)
```

As you import something, you can assign it a custom name using `as`

```python
print('Let\'s alias something as we import it!')
print('importing e...')
from math import e
print('importing e as wahoo...')
from math import e as wahoo
print('T/F: e and wahoo are equal:', e == wahoo)
```

To summarize, the following three approaches all achieve the exact same thing

```python
# approach 1
import statistics
avg = statistics.mean
print('The average of [1,2,3] is:', avg([1, 2, 3]))
# or...
# print('The average of [1,2,3] is:', statistics.mean([1, 2, 3]))

# approach 2
from statistics import mean
avg = mean
print('The average of [1,2,3] is:', avg([1, 2, 3]))
# or...
# print('The average of [1,2,3] is:', mean([1, 2, 3]))

# approach 3
from statistics import mean as avg
print('The average of [1,2,3] is:', avg([1, 2, 3]))
```

## Debugging

Fix the following code blocks by reading the Error output that the python
interpreter gives you.

```python
print('What could possibly be wrong here?'}
```

```python
a = 1
print('The ' + a + 'st Star Wars movie is the best one!')
```

```python
x = 4
y = 5
if x < y
    print(x, 'is less than', y, '!'

print('done!')
```
