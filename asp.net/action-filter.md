# Action Filter

## What is an Action Filter in ASP.NET Core MVC?

An Action Filter in ASP.NET Core MVC is an attribute that allows you to execute logic before and/or after an action method executes. It is part of the filter pipeline in MVC, and it can be used to handle cross-cutting concerns such as logging, authentication, validation, exception handling, performance tracking, and more.

## When to Use an Action Filter?

You should use action filters when you need to:

- Run logic before or after a controller action executes.
- Apply cross-cutting concerns (e.g., logging, caching, security).
- Modify the action result before returning it to the client.
- Short-circuit an action execution (e.g., return an error response without executing the action).

## How to Use an Action Filter?

You can create an action filter in ASP.NET Core MVC by implementing IActionFilter or IAsyncActionFilter, or by deriving from ActionFilterAttribute.

## Example 1: Creating a Custom Action Filter for Logging 

Here’s a simple example of an action filter that logs before and after the execution of an action.

### Step 1: Create a Custom Action Filter

```csharp
using Microsoft.AspNetCore.Mvc.Filters;
using Microsoft.Extensions.Logging;
using System;

public class LogActionFilter : IActionFilter
{
    private readonly ILogger<LogActionFilter> _logger;

    public LogActionFilter(ILogger<LogActionFilter> logger)
    {
        _logger = logger;
    }

    // Executed before the action method executes
    public void OnActionExecuting(ActionExecutingContext context)
    {
        _logger.LogInformation($"Executing action: {context.ActionDescriptor.DisplayName} at {DateTime.UtcNow}");
    }

    // Executed after the action method executes
    public void OnActionExecuted(ActionExecutedContext context)
    {
        _logger.LogInformation($"Executed action: {context.ActionDescriptor.DisplayName} at {DateTime.UtcNow}");
    }
}
```

### Step 2: Register the Filter in Startup (Program.cs)

Add the filter globally so that it applies to all controllers and actions.

```csharp
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews(options =>
{
    options.Filters.Add<LogActionFilter>(); // Register globally
});

var app = builder.Build();

app.UseAuthorization();
app.MapControllers();
app.Run();

```

### Step 3: Apply to a Specific Controller or Action

If you don’t want to register the filter globally, you can apply it to a specific controller or action:

```csharp
using Microsoft.AspNetCore.Mvc;

[ServiceFilter(typeof(LogActionFilter))] // Apply filter to this controller
public class HomeController : Controller
{
    public IActionResult Index()
    {
        return View();
    }
}
// Alternatively, you can apply it to a single action:
public class HomeController : Controller
{
    [ServiceFilter(typeof(LogActionFilter))] // Apply only to this action
    public IActionResult Index()
    {
        return View();
    }
}
```

## Example 2: Action Filter for Timing Execution

This filter calculates the execution time of an action method.

### Step 1: Create the Execution Time Filter

```csharp
using Microsoft.AspNetCore.Mvc.Filters;
using Microsoft.Extensions.Logging;
using System;

public class LogActionFilter : IActionFilter
{
    private readonly ILogger<LogActionFilter> _logger;

    public LogActionFilter(ILogger<LogActionFilter> logger)
    {
        _logger = logger;
    }

    // Executed before the action method executes
    public void OnActionExecuting(ActionExecutingContext context)
    {
        _logger.LogInformation($"Executing action: {context.ActionDescriptor.DisplayName} at {DateTime.UtcNow}");
    }

    // Executed after the action method executes
    public void OnActionExecuted(ActionExecutedContext context)
    {
        _logger.LogInformation($"Executed action: {context.ActionDescriptor.DisplayName} at {DateTime.UtcNow}");
    }
}

```

### Step 2: Apply the Filter

```csharp
[ServiceFilter(typeof(ExecutionTimeFilter))]
public IActionResult About()
{
    return View();
}

```

## Example 3: Custom Authorization Filter Using Action Filter

This example ensures that only users with an API Key can access an action.

### Step 1: Create the API Key Filter

```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Filters;
using Microsoft.Extensions.Configuration;
using System;

public class ApiKeyAuthFilter : IActionFilter
{
    private readonly IConfiguration _configuration;

    public ApiKeyAuthFilter(IConfiguration configuration)
    {
        _configuration = configuration;
    }

    public void OnActionExecuting(ActionExecutingContext context)
    {
        var request = context.HttpContext.Request;
        if (!request.Headers.TryGetValue("X-API-KEY", out var apiKey) || apiKey != _configuration["ApiKey"])
        {
            context.Result = new UnauthorizedResult(); // Return 401 Unauthorized
        }
    }

    public void OnActionExecuted(ActionExecutedContext context) { }
}

```

### Step 2: Register the Filter

```csharp
builder.Services.AddControllersWithViews(options =>
{
    options.Filters.Add<ApiKeyAuthFilter>(); // Apply globally
});

```

### Step 3: Use the Filter

```csharp
[ServiceFilter(typeof(ApiKeyAuthFilter))]
public IActionResult SecureData()
{
    return Content("Secure data accessed successfully.");
}

```

## When to Use IActionFilter vs. IAsyncActionFilter?

- IActionFilter: Use it for synchronous logic.
- IAsyncActionFilter: Use it for asynchronous logic (e.g., calling a database or external API before/after an action executes).
  
Example of asynchronous action filter:

```csharp
using Microsoft.AspNetCore.Mvc.Filters;
using Microsoft.Extensions.Logging;
using System.Diagnostics;
using System.Threading.Tasks;

public class AsyncExecutionTimeFilter : IAsyncActionFilter
{
    private readonly ILogger<AsyncExecutionTimeFilter> _logger;

    public AsyncExecutionTimeFilter(ILogger<AsyncExecutionTimeFilter> logger)
    {
        _logger = logger;
    }

    public async Task OnActionExecutionAsync(ActionExecutingContext context, ActionExecutionDelegate next)
    {
        var stopwatch = Stopwatch.StartNew();
        await next(); // Continue with the action execution
        stopwatch.Stop();

        _logger.LogInformation($"Action {context.ActionDescriptor.DisplayName} executed in {stopwatch.ElapsedMilliseconds} ms");
    }
}

```

## Conclusion

- Action Filters are powerful for pre-processing and post-processing requests in ASP.NET Core MVC.
- You can use them for logging, authentication, validation, performance tracking, caching, exception handling, etc.
- You can apply them globally, at the controller level, or action level.
- Use IActionFilter for synchronous logic and IAsyncActionFilter for asynchronous logic.