# What is CodeShaper

Ever came across having to make changes to code that Regex (Regular Expressions) can't cover, like
transforming the name of a function and its arguments, or changing a piece of the body
without breaking  nesting? this is where this tool shines and makes it easy!

CodeShaper is a tool that loads a given project or single code file, parses its AST (Abstract Syntax Tree)
so you can transform any code that you wish, going to the very small details

It uses [ANtlr4](https://www.antlr.org/) along the required [Antlr4 Grammars](https://github.com/antlr/grammars-v4/)
to parse the contents of the code file that any type of project is related to

Currently, it only supports these grammars:
 - [CPP14 (C++ 14) Grammar](https://github.com/antlr/grammars-v4/tree/master/cpp)

