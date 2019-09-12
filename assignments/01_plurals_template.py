"""Template for Assignment 1."""

from assignment_01_eval import evaluate


def pluralize(sg):
    """Return list of plural form(s) of input_word.

    Building this function is the purpose of Assignment 1.
    The most basic case is already provided.
    """
    return sg + 's'


if __name__ == '__main__':
    evaluate(pluralize)
