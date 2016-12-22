If you got this:

```Python is not installed as a framework.```

I run my script in virtualenv. Python version is 3.5.

Add a line:

`backend: TkAgg`

in file:

`~/.matplotlib/matplotlibrc`

This solved the problem.
