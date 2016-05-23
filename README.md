# Conky Util

Simple python package that provides tools for script that aims to run under Conky context.

# Installation

Just use **pip** :

```bash
pip install conkyutil
```

# Usage

A ``ConkyWriter`` instance holds a stream and writes text and Conky command to it. Based
fluent interface pattern, it could be used as following :

```python
from conkyutil.writer import ConkyWriter

writer = ConkyWriter()
writer.voffset(12).offset(12).color('red').write('Hellonky !').newline()
```

# Contribute
