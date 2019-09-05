## Review

1. Write a script called `hello.py` that uses input to prompt a user for their
   name and then welcomes them.

    ```
    Enter your name: Chuck
    Hello Chuck
    ```

1. Write a script called `payday.py` to prompt the user for hours and rate per
   hour to compute gross pay.

    ```
    Enter Hours: 35
    Enter Rate: 2.75
    Pay: 96.25
    ```

    We won’t worry about making sure our pay has exactly two digits after the
    decimal place for now. If you want, you can play with the built-in Python
    `round` function to properly round the resulting pay to two decimal places.


1. Write a script called `CtoF.py` which prompts the user for a Celsius
   temperature, convert the temperature to Fahrenheit, and print out the
   converted temperature.
   * ![equation](http://latex.codecogs.com/svg.latex?(C%20\cdot%20\frac{9}{5})%20+%2032%20=%20F)

    ```
    Enter a temperature in Celsius: 0
    0 C is equal to 32 F
    ```

## Using `help()` 

The built-in `help` function uses the same keys as the command-line tool `less`
to navigate:

* <kbd>q</kbd> quit / exit
* <kbd>f</kbd> forward / page down
* <kbd>b</kbd> backward / page up
* <kbd>&uarr;</kbd> up one line
* <kbd>&darr;</kbd> down one line

To search a document, type <kbd>/</kbd>, the text you are searching for,
<kbd>return</kbd>. Use <kbd>n</kbd> to find the `n`ext instance, and
<kbd>N</kbd> to find the previous instance.

1. Use the `help()` function to learn about the following built-in functions.
   Use them, tinker, break, learn.
   * `len()`
       * Try using `len()` on various types of values (`str`, `int`, `float`,
         `function`, etc.)
   * `abs()`
   * `chr()` / `ord()`
   * `pow()`
   * `round()` 
   * `sorted()`

### A deeper dive into strings (`str`s)

> A "method" is a function that is attached to an object.

1. Use the `help()` function to discover all of the (many!) methods that are
   attached to `str`s. Ignore the double-underscore ("dunder" or "magic")
   methods, which are for behind-the-scenes interactions. You can call them,
   just like any other method, but they are not generally intended for that.
   
   ```python
   >>> 'moby dick'.title()
   'Moby Dick'
   ```

   Start with the following methods and then explore on your own. Use, tinker,
   break, learn.

   * `startswith()` / `endswith()`
   * `isdigit()` / `isnumeric()` / `isdecimal()`
   * `islower()` / `isupper()` / `istitle()`
   * `lower()` / `upper()` / `title()` / `swapcase()`
   * `zfill()`
