# Template

 The issue you're seeing—where the generated solution wraps everything inside an extra folder (e.g., MyTestSolution/)—is a common behavior when using .NET CLI or dotnet new templates, especially when preferNameDirectory is set to true.

 ## Option 1: Set preferNameDirectory to false

1. This prevents the template engine from wrapping everything in a folder named after the solution.
1. "preferNameDirectory": false
1. However, this means the user must manually create a folder before running dotnet new.

## Option 2: Adjust your template content structure

1. If you want to keep preferNameDirectory: true (which is more user-friendly), you can move all your template content one level up so that the structure inside your .template.config folder looks like this:

'''bash
IssueDocsTemplate/
  .template.config/
    template.json
  src/
    IssueDocs.WebMVC/
    ...
  tests/
  .gitignore
  README.md
  IssueDocs.sln
'''

## Bonus: Rename solution file dynamically

1. To make the solution file name match the project name, use the sourceName token in your .sln file name:
   1. IssueDocs.sln →  __IssueDocs.sln
1. Then rename it in the template to:
   1. "sourceName": "IssueDocs"
1. his will rename IssueDocs.sln to MyTestSolution.sln during instantiation.

## Folder Structure

```bash
IssueDocsTemplate/
├── .template.config/
│   └── template.json
├── src/
│   ├── IssueDocs.WebMVC/
│   ├── IssueDocs.Infrastructure/
│   ├── IssueDocs.Application/
│   └── IssueDocs.Domain/
├── tests/
├── .gitignore
├── README.md
└── IssueDocs.sln
```

## Template.json

```bash
{
  "$schema": "http://json.schemastore.org/template",
  "author": "Steve Kings",
  "classifications": [ "Web", "ASP.NET", "MVC" ],
  "identity": "IssueDocs",
  "name": "SK MVC Template",
  "shortName": "SkMvcTemplate",
  "sourceName": "IssueDocs",
  "preferNameDirectory": true,
  "tags": {
    "language": "C#",
    "type": "solution"
  }
}
```

## What happes when I run dotnet new SkMvcTemplate -n MyTestSolution

```bash
MyTestSolution/
├── src/
├── tests/
├── .gitignore
├── README.md
└── MyTestSolution.sln   ← renamed from IssueDocs.sln
```

## Template22

```bash
dotnet new -i ./IssueDocsTemplate
dotnet new SkMvcTemplate -n MyTestSolution

```

## PowerShell Script (Windows/macOS/Linux via PowerShell)

```bash
# Navigate to the template root directory
cd ./IssueDocsTemplate

# Pack the template into a NuGet package
dotnet new -i . --force

# Optional: Create a .nupkg file for distribution
dotnet pack -o ../nupkgs

```

## Bash Script (Linux/macOS)

```bash
#!/bin/bash

# Navigate to the template root
cd IssueDocsTemplate

# Install the template locally
dotnet new -i . --force

# Optional: Create a NuGet package (if you have a .csproj for the template)
dotnet pack -o ../nupkgs

```

## Test the template

```bash
dotnet new SkMvcTemplate -n MyTestSolution

```