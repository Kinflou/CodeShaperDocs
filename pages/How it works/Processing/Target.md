# Target

## Parsing Visual Studio Solution

Starts by loading the solution file (.sln) and parses its projects (.vcxproj)
location and names using regex, for example:

```xml
Project("{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}") = "ExampleCLI", "projects\ExampleCLI.vcxproj", "{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}"
EndProject
Project("{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}") = "ExampleLib", "projects\ExampleLIB.vcxproj", "{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}"
EndProject
...
```

will result in `ExampleCLI` and `ExampleLib` data and then proceeds to parse its project files


## Parsing Visual Studio Project

Starts by loading each given project file (vcxproj) and parses its modules (.cpp)
and headers (.h) using regex, for example: 

```xml
  <ItemGroup>
    <ClInclude Include="..\source\ExampleCLI\CLI.h"/>
    <ClInclude Include="..\source\ExampleCLI\Menu.h"/>
  </ItemGroup>
  <ItemGroup>
    <ClCompile Include="..\source\ExampleCLI\CLI.cpp"/>
    <ClCompile Include="..\source\ExampleCLI\Menu.cpp"/>
  </ItemGroup>
  ...
```

will result in the files array and then proceeds to parse each module:
```
..\source\ExampleCLI\CLI.cpp
..\source\ExampleCLI\Menu.cpp
..\source\ExampleCLI\CLI.h
..\source\ExampleCLI\Menu.h
```

