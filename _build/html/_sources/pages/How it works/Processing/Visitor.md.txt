# Visitor

## Visiting a CPP Module

Starts by first creating an Antrl Input stream, a Visitor and
then uses a CPP Visitor, loads the module and starts visiting
the module, such as its methods, declarations, expressions, etc...

*You can check all the locations it visits in the [Visitor Class](https://github.com/OriDevTeam/CodeShaper/blob/main/CodeShaper/Lib/AST/ANTLR/CPPModuleVisitor.cs)*


## Shaping the module

When any visit occurs, for example a method visit:

```cpp
void Hello ()
{
    // This is a function yes!
}
```

its text its stored in the Module Dictionary giving its location, for example:

```csharp
Module.Dictionary[Location.Method] = context text (the function text above for example)
```

then, processing of Shaping Actions occurs, such as Builders, Resolvers, Replacements, Additions and Subtractions (we will call them BRRAS)
