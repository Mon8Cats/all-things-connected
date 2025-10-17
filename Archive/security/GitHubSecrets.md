# Storing API Keys and Secrets in GitHub Secrets and Using Them in ASP.NET Core

Since storing API keys, secrets, or sensitive information in appsettings.json is not secure, a better approach is to store them in GitHub Secrets and access them in your application using environment variables.

## Step 1: Store Secrets in GitHub Repository Settings

- Go to your GitHub Repository.
- Navigate to:
   - Settings → Secrets and variables → Actions → New repository secret
- Add secrets (e.g., API_KEY, DATABASE_PASSWORD).
    - Secret Name: API_KEY
    - Secret Value: your-secret-api-key
    - Secret Name: DATABASE_PASSWORD
    - Secret Value: SuperSecretPassword123!

## Step 2: Modify ASP.NET Core Code to Read Secrets

Instead of storing secrets in appsettings.json, retrieve them using environment variables.

### Modify Configuration Class

Create a class to store your secrets.

```csharp
public class ApiSettings
{
    public string ApiKey { get; set; }
    public string DatabasePassword { get; set; }
}
```

### Modify Program.cs to Read Environment Variables

Update Program.cs to read secrets from environment variables.

```csharp
var builder = WebApplication.CreateBuilder(args);

// Bind secrets from environment variables
builder.Services.Configure<ApiSettings>(options =>
{
    options.ApiKey = Environment.GetEnvironmentVariable("API_KEY") ?? "DefaultApiKey";
    options.DatabasePassword = Environment.GetEnvironmentVariable("DATABASE_PASSWORD") ?? "DefaultPassword";
});

var app = builder.Build();
app.UseAuthorization();
app.MapControllers();
app.Run();

```

### Use Secrets in a Controller

Inject IOptions<ApiSettings> and access the API key.

```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Options;

public class HomeController : Controller
{
    private readonly ApiSettings _apiSettings;

    public HomeController(IOptions<ApiSettings> options)
    {
        _apiSettings = options.Value;
    }

    public IActionResult Index()
    {
        return Content($"API Key: {_apiSettings.ApiKey}, Database Password: {_apiSettings.DatabasePassword}");
    }
}
```

## Step 3: Inject Secrets into GitHub Actions

If you deploy your ASP.NET Core app using GitHub Actions, you need to pass secrets as environment variables.

### GitHub Actions Example (.github/workflows/deploy.yml)

Modify your GitHub Actions workflow to pass secrets.

```yaml
name: Deploy ASP.NET Core App

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Set up .NET
        uses: actions/setup-dotnet@v3
        with:
          dotnet-version: '8.0'

      - name: Build and Publish
        run: |
          dotnet restore
          dotnet build --configuration Release
          dotnet publish -c Release -o publish

      - name: Run ASP.NET Core App
        env:
          API_KEY: ${{ secrets.API_KEY }}
          DATABASE_PASSWORD: ${{ secrets.DATABASE_PASSWORD }}
        run: |
          dotnet publish/MyApp.dll
```

## Step 4: Run Locally with Environment Variables

To test locally, set environment variables before running the app.

### On Windows (PowerShell)

```powershell
$env:API_KEY="your-secret-api-key"
$env:DATABASE_PASSWORD="SuperSecretPassword123!"
dotnet run

```

### On macOS/Linux (Terminal)

```sh
export API_KEY="your-secret-api-key"
export DATABASE_PASSWORD="SuperSecretPassword123!"
dotnet run

```

## Summary

|Task|Action|
|:---:|:---:|
|Store secrets securely|Use GitHub Secrets (Settings > Secrets > Actions)|
|Access secrets in ASP.NET Core|Use Environment.GetEnvironmentVariable("SECRET_NAME")|
|Inject secrets into services|Use IOptions<ApiSettings>|
|Pass secrets in GitHub Actions|Use ${{ secrets.SECRET_NAME }} in workflow|

This approach keeps your secrets secure while allowing your app to retrieve them dynamically.
