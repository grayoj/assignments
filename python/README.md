# Python.

This is the section for Python solutions that you may need to reference.

## Solution

These are the solutions currently available:

1. [Collects the names of students and identify the “captain” of the football team.](https://github.com/grayoj/assignments/blob/master/python/captain-of-class.py)
2. [Find the sum and average of student's age.](https://github.com/grayoj/assignments/blob/master/python/sum-of-students-age.py)
3. [Guessing game that ends after three trials.](https://github.com/grayoj/assignments/blob/master/python/guessing-game-3-trials.py)

## Requirements

1. Python3 (All solutions are done in Python 3)
2. Pip to install modules.
3. Git/Svn for version control.
4. Pen and paper, coffee or whatever man ...

## Setup

You would need to clone the repository on your computer using a version control tooling, known as Git. Got your own custom tooling? Hurray.
But if you're sticking with git like me:

1. Clone the project in a nice folder you can access:
   `git clone https://github.com/grayoj/assignments.git`

**I JUST WANT TO CLONE THE SPECIFIC FOLDER.**

If you would prefer cloning a specific working directory and not the entire source code then use **svn**. To install svn, run `sudo apt-get install subversion`. I'm on a Linux machine, to replicate the same for your machine, kindly Google.

Then `svn checkout https://github.com/lodash/lodash/trunk/test`

2. Now we have to set up the latest version of Python:

```
   python --version
   sudo add-apt-repository --remove ppa:fkrull/deadsnakes
   sudo apt-get update
   sudo apt-get remove --purge python2
   sudo apt install python3.10
```

The above example is on a Linux machine. For windows, visit <a href="python.org">Python's official site</a>

For MacOS:
Ensure Xcode command line tools are installed, uninstall and install using brew.

```
xcode --select-install
brew uninstall python
brew install python@3.10
```

Or just try out the custom shell scripts I wrote for Linux, MacOS.
Running the scripts: `shell.sh` for MacOS and `bashrc` for Linux.

3. Now, let's install some nice dependencies: `sudo pip3 install -r requirements.txt`

## Contributing

Feel free to contribute by opening an issue or pull request, with the title being the solution you want to add and the language you used.
For example, "Finding two sum - Haskell" then feel free to elaborate in the description.

## License

The code in this repsoitory is licensed under the MIT license.

## Contact

Send in a mail at [here](mailto:mgeraldoj07@gmail.com).
