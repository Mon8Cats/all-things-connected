# Injecting Values into Controller or Services

## Injecting Values from appsettings.json into Controllers or Services in ASP.NET Core

You can inject configuration values from appsettings.json into controllers, services, or any other constructors using dependency injection (DI) in ASP.NET Core.

## Method 1: Injecting a Single Value from appsettings.json Using IConfiguration

If you have a simple key-value pair in appsettings.json, you can retrieve it using IConfiguration.

### Step 1: Define a Value in appsettings.json

```csharp
{
  "AppSettings": {
    "ApiKey": "12345-abcde",
    "MaxItems": 50
  }
}
```

### Step 2: Inject IConfiguration into the Controller

```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;

public class HomeController : Controller
{
    private readonly string _apiKey;
    private readonly int _maxItems;

    public HomeController(IConfiguration configuration)
    {
        _apiKey = configuration["AppSettings:ApiKey"];
        _maxItems = int.Parse(configuration["AppSettings:MaxItems"]);
    }

    public IActionResult Index()
    {
        return Content($"API Key: {_apiKey}, Max Items: {_maxItems}");
    }
}

```

configuration["AppSettings:ApiKey"] accesses the value using the section and key name.

## Method 2: Using Strongly Typed Configuration (Recommended)

Instead of manually retrieving values using IConfiguration, you can bind them to a strongly typed class.

### Step 1: Create a Configuration Class

```csharp
public class AppSettings
{
    public string ApiKey { get; set; }
    public int MaxItems { get; set; }
}

```

### Step 2: Bind the Configuration in Program.cs

```csharp
var builder = WebApplication.CreateBuilder(args);

// Bind the configuration section to a class
builder.Services.Configure<AppSettings>(builder.Configuration.GetSection("AppSettings"));

var app = builder.Build();
app.UseAuthorization();
app.MapControllers();
app.Run();

```

### Step 3: Inject IOptions<AppSettings> in the Controller

```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Options;

public class HomeController : Controller
{
    private readonly AppSettings _appSettings;

    public HomeController(IOptions<AppSettings> options)
    {
        _appSettings = options.Value;
    }

    public IActionResult Index()
    {
        return Content($"API Key: {_appSettings.ApiKey}, Max Items: {_appSettings.MaxItems}");
    }
}

```

Benefits of this approach:

- Strong typing instead of string-based access.
- Automatic binding of multiple values at once.
- Easier unit testing since you can inject a fake configuration.

## Method 3: Using IOptionsSnapshot for Reloadable Configuration

If your configuration values change at runtime, you can use IOptionsSnapshot, which refreshes on every request.

```csharp
public class HomeController : Controller
{
    private readonly AppSettings _appSettings;

    public HomeController(IOptionsSnapshot<AppSettings> options)
    {
        _appSettings = options.Value;
    }

    public IActionResult Index()
    {
        return Content($"API Key: {_appSettings.ApiKey}, Max Items: {_appSettings.MaxItems}");
    }
}

```

Use IOptionsSnapshot<T> when you need per-request updates (e.g., settings that change dynamically but don't require application restart).

## Method 4: Using IOptionsMonitor for Real-Time Updates

If you want the configuration to update without restarting the app, use IOptionsMonitor.

```csharp
public class HomeController : Controller
{
    private readonly IOptionsMonitor<AppSettings> _optionsMonitor;

    public HomeController(IOptionsMonitor<AppSettings> optionsMonitor)
    {
        _optionsMonitor = optionsMonitor;
    }

    public IActionResult Index()
    {
        var settings = _optionsMonitor.CurrentValue;
        return Content($"API Key: {settings.ApiKey}, Max Items: {settings.MaxItems}");
    }
}

```

Use IOptionsMonitor<T> for real-time updates (e.g., settings read from an external configuration provider).

## Method 5: Injecting Configuration into Services

If you have a service that requires configuration, inject the settings into the service constructor.

### Step 1: Create a Service

```csharp
public class MyService
{
    private readonly AppSettings _appSettings;

    public MyService(IOptions<AppSettings> options)
    {
        _appSettings = options.Value;
    }

    public string GetApiKey()
    {
        return _appSettings.ApiKey;
    }
}

```

### Step 2: Register the Service in Program.cs

```csharp
builder.Services.AddSingleton<MyService>();

```

### Step 3: Inject the Service into the Controller

```csharp
public class HomeController : Controller
{
    private readonly MyService _myService;

    public HomeController(MyService myService)
    {
        _myService = myService;
    }

    public IActionResult Index()
    {
        return Content($"API Key from service: {_myService.GetApiKey()}");
    }
}


```

## Summary of Methods

| Approach| Use Case |
| :---: | :---: |
|IConfiguration|Quick access, but string-based (not strongly typed).|
|IOptions<T>|Recommended for static settings (loaded once at startup).|
|IOptionsSnapshot<T>|Reloads settings per request (useful in web apps).|
|IOptionsMonitor<T>|Updates in real-time without restarting the app.|
|Injecting into Services|Use when settings are needed in services instead of controllers.|

## Naming Conventions for IOptions<T> Classes in ASP.NET Core

When naming classes for configuration binding with IOptions<T>, follow these best practices:

- Use <Feature>Settings format.
- The name should reflect the configuration section in appsettings.json.
- Use PascalCase.
- Keep the name plural (e.g., LoggingSettings, DatabaseSettings).

### Examples

|Configuration Section (appsettings.json)|IOptions<T> Class Name|
|:---:|:---:|
|"Database"|DatabaseSettings|
|"JwtConfig"|JwtSettings|
|"Email"|EmailSettings|
|"Logging"|LoggingSettings|
|"Cache"|CacheSettings|

## Conclusion

- If you just need a single value, use IConfiguration.
- If you want strongly typed settings, use IOptions<T>.
- If your settings change per request, use IOptionsSnapshot<T>.
- If your settings should update without restarting, use IOptionsMonitor<T>.