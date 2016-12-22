If you got this error:

```
Python is not installed as a framework. 
The Mac OS X backend will not be able to function correctly if Python is not installed as a framework. 
See the Python documentation for more information on installing Python as a framework on Mac OS X. 
Please either reinstall Python as a framework, or try one of the other backends. 
If you are Working with Matplotlib in a virtual enviroment see 'Working with Matplotlib in Virtual environments' in the Matplotlib FAQ
```

I run my script in virtualenv. Python version is 3.5.

Add a line:

```
backend: TkAgg
```

in file:

```
~/.matplotlib/matplotlibrc
```

This solved the problem.
