# XenonPy/ai

A collection of AI examples and implementations.

## Examples

1. [Linear Regression](#linear-regression)
2. [Polynomial Regression](#polynomial-regression)
3. [POS Tagging](#pos-tagging)
4. [Named Entity Detection](#named-entity-detection)

## `headless.py` VS `main.py`

The headless version is lighter weight, and doesn't require matplotlib to be installed. However, unlike the main version, it doesn't show an informative plot detailing a bit more about how the model works.

### Installation for datasets/libraries

Any examples that work with human language need a dataset installed. They are written to use `en_web_core_sm`. In addition, most examples depend on common libraries to work. You can install everything like this:

```shell
$ pip3 install -r requirements.txt
$ python3 -m spacy download en_core_web_sm
```

### Linear Regression

This example takes in an x-array and a y-array and correlates them with a linear regression. This example is debatably machine _learning_ in and of itself, but if not it's certainly a close neighbor and predecessor.A linear regression works well with data that follows a relatively linear path.

### Polynomial Regression

This example takes in an x-array and a y-array and correlates them with a polynomial regression. This example is debatably machine _learning_ in and of itself, but if not it's certainly a close neighbor and predecessor. A polynomial regression works like a linear one, but is capable of fitting more complex nonlinear data.

### POS Tagging

This example classifies parts of speech into their categories, like nouns, verbs, and adjectives. This can be useful for other, more complex NLP tasks.

### Named Entity Detection

This example detects named entities like countries, people, organizations or money.
