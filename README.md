# HackAssembler

Python implementation of the nand2tetris' Hack Assembler Program. Build for
project 6 of the nand2tetris course on coursera.

## Goal

Develop an assembler that translates programs written in Hack assembly
language into the binary code understood by the Hack hardware platform.

## Requirements

* Parse the Hack Assembly code file (*.asm)  
* Handle whitespaces
* Handle comments:
    1. Line comments
    2. Inline comments
* Must be able to translate two types of instructions:
    1. A-instruction
    2. C-instruction
* Must be able to track symbols and labels
* Write the generated code into a file (*.hack)


## Proposed API

* `Parser` module: Encapsulates access to the input code. Reads an assembly language command, parses it, and provides convenient access to the command’s components
(fields and symbols). In addition, removes all white space and comments.

* `Code` module
* `Main` module
* Use a `HashTable` to handle symbols and labels

## My Thoughts

1. This project is a good programming exercise.
2. I will use it to practice TDD and Unit Testing.
3. I will use `unittest` module of Python.

## Contact

Feel free to contact me for queries:

Email: hussainbhaitech@gmail.com
Instagram: @NagariaHussain
