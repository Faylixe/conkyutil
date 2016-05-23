# Conky Util

Simple python package that provides tools for script that aims to run under
Conky context. Most of it has been generated using
[apiwriter.py](https://github.com/Faylixe/conkyutil/blob/master/apiwriter.py)
script, which extracts command from http://conky.sourceforge.net/variables.html
web page.

## Installation

Just use **pip** :

```bash
pip install conkyutil
```

## Usage

A ``ConkyWriter`` instance holds a stream and writes text and Conky command to
it. Based on fluent interface pattern, it could be used as following :

```python
from conkyutil.writer import ConkyWriter

writer = ConkyWriter()
writer.voffset(12).offset(12).color('red').write('Hellonky !').newline()
```

## Contribute

All contributions as suggestion as well are welcome, using this repository
issues page.
