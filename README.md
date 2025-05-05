# BookBot

**BookBot** is a simple Python program that analyzes a `.txt` file (book) and provides statistics about its contents, such as word counts and character usage.

This project is part of the [Boot.dev](https://www.boot.dev) Python course.

## Features

- Counts the total number of words in a book.
- Counts the number of times each character (a-z) appears.
- Sorts characters by frequency (most to least used).
- Simple and readable console output.

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/goncalofgalmeida/bookbot.git
   cd bookbot

2. Add your .txt book file to the project folder.

3. Run the program:
   ```bash
   python3 main.py your/book/file/path.txt

## Example Output
```bash
$ python3 main.py books/frankenstein.txt
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ===============
