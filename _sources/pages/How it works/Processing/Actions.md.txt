# Actions

When shaping starts, the following is occurs:
 - Parsing of Shape Project data (settings, shapers...)
 - Parsing of Visual Studio Solution and its Projects (sln and vcxproj)
 - Parsing of Project's modules (cpp and header) with Antlr
 - Shaping of Module () with a CPP Visitor



## Building the builders

Think of a Builder like a Tree, it has its Root and Branches (children actions), and the leafs
are its BRASS (in this case only keep Builders in mind)

When processing of builders starts, all Root level builders are called
and its active builder its processed, the active builder is always the Root builder,

A builder can have its own Actions(BRRAS) and these will be triggered when
a builder is set as active (except Builders which will only build when the last builder on its branch is reach)


### Marking a builder as active
To set a builder as active, some conditions have to occur:
 - The location of the builder has to be equal to the current visitor location
 - (optional) The location reference had to have been previously visited
 - (optional) When location reference is set, the reference expression has to match the reference location context text



### Building the result

When the last builder (leaf) of a Branch is visited, all the builders in the branch
will build its results, using **Actions Expressions** (check [Expressions Documentation](https://github.com/OriDevTeam/CodeShaper/blob/main/Documentation/Expressions.md))
