# Developer Environment

```python
def sum(xs):
    count = 0
    for x in xs:
        count += x
    return count
```

## Linter

( **pylint**, pycodestyle, mypy )

Helps you write quality code

Points out bugs or unexpected behavior

Type errors

Catches errors as you're writing them.

We want to be able to focus on the
logic of our program, not boring
stuff like syntax.


## Formatter

( **autopep8**, yapf, black, flake8 )

Makes sure your code
has good style.

PEP8 standard

* Indent by 4 spaces
* No trailing spaces at the end of lines
* Two blank lines between functions
* Max column length is 80 characters

Catches misleading code


## Language Server Protocols (LSPs)

Bundles a linter, formatter, and analyzer

Auto suggestions, auto completion,

Code analysis


# Visual Studio Code

