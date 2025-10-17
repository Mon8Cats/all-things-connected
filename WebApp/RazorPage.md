# Razor Page

```c#
// Pages/Base/BasePageModel.cs
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

// Apply the Authorize attribute to the base class
[Authorize]
public class BasePageModel : PageModel
{
    // You can add common properties or methods here.
    // For example, a method to check user roles.
    public bool IsAdmin()
    {
        return User.IsInRole("Admin");
    }

    // You can also override OnGet or OnPost to implement
    // common logic before the derived page's methods are called.
    public override void OnPageHandlerExecuting(PageHandlerExecutingContext context)
    {
        // This logic runs before OnGet, OnPost, etc.
        if (!User.Identity.IsAuthenticated)
        {
            // Redirect to login if not authenticated (though [Authorize] handles this)
            // You can add more complex checks here.
        }
        
        base.OnPageHandlerExecuting(context);
    }
}

// Pages/Secret/Index.cshtml.cs
using Microsoft.AspNetCore.Mvc.RazorPages;
using YourProject.Pages.Base; // Or wherever you placed your BasePageModel

public class SecretPageModel : BasePageModel // Inherit here
{
    public void OnGet()
    {
        // This page is now protected by the [Authorize] attribute from the base class.
        // You can also use the IsAdmin() method defined in the base class.
        if (IsAdmin())
        {
            // Do admin-specific stuff
        }
    }
}

// Pages/Admin/Index.cshtml.cs
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Authorization;
using YourProject.Pages.Base;

// This page requires the user to be in the "Admin" role
[Authorize(Roles = "Admin")]
public class AdminPageModel : BasePageModel
{
    public void OnGet()
    {
        // Only authenticated users with the "Admin" role can access this page.
    }
}
```

```c#
// In a file like BasePageModel.cs

public class BasePageModel : PageModel
{
    public override void OnPageHandlerExecuting(PageHandlerExecutingContext context)
    {
        // Add your authorization logic here
        if (!User.Identity.IsAuthenticated)
        {
            // If the user isn't authenticated, redirect them to the login page
            context.Result = RedirectToPage("/Account/Login");
        }

        base.OnPageHandlerExecuting(context);
    }
}

// In a file like Index.cshtml.cs

public class IndexModel : BasePageModel
{
    private readonly ILogger<IndexModel> _logger;

    public IndexModel(ILogger<IndexModel> logger)
    {
        _logger = logger;
    }

    public void OnGet()
    {
        // This code will only run if the user is authenticated
        // thanks to the logic in BasePageModel
    }
}

// In a file like MyAuthorizationFilter.cs

public class MyAuthorizationFilter : IAsyncPageFilter
{
    public async Task OnPageHandlerExecutionAsync(PageHandlerExecutingContext context,
                                                  PageHandlerExecutionDelegate next)
    {
        // Add your authorization logic here
        if (!context.HttpContext.User.Identity.IsAuthenticated)
        {
            context.Result = new RedirectToPageResult("/Account/Login");
            return;
        }

        await next.Invoke();
    }

    public Task OnPageHandlerSelectionAsync(PageHandlerSelectedContext context)
    {
        return Task.CompletedTask;
    }
}

// In a file like Index.cshtml.cs

[MyAuthorizationFilter]
public class IndexModel : PageModel
{
    // ...
}


// Example: In /Filters/MyAuthorizationFilter.cs

public class MyAuthorizationFilter : IAsyncPageFilter
{
    // ... (Filter logic goes here) ...

    public async Task OnPageHandlerExecutionAsync(PageHandlerExecutingContext context, PageHandlerExecutionDelegate next)
    {
        // Example: Check for a claim or role
        if (!context.HttpContext.User.HasClaim(c => c.Type == "CanAccessAdmin" && c.Value == "true"))
        {
            // Redirect to an access denied page
            context.Result = new ForbidResult(); 
            return;
        }

        await next.Invoke();
    }

    public Task OnPageHandlerSelectionAsync(PageHandlerSelectedContext context)
    {
        return Task.CompletedTask;
    }
}

// Example: In /Pages/Admin/ManageUsers.cshtml.cs

[ServiceFilter(typeof(MyAuthorizationFilter))] // Use ServiceFilter if the filter requires Dependency Injection
// OR
// [TypeFilter(typeof(MyAuthorizationFilter))] // Use TypeFilter if the filter does not require DI

public class ManageUsersModel : PageModel
{
    // ...
}

// In Program.cs

builder.Services.AddRazorPages(options =>
{
    // Register the filter globally
    options.Filters.Add(typeof(MyAuthorizationFilter));

    // Alternatively, you can configure it to apply only to certain folders or pages
    // options.Conventions.AddFolderRouteModelConvention("/Admin", model => 
    // {
    //     model.Filters.Add(new MyAuthorizationFilter());
    // });
});

// In /Filters/BasePageFilterAttribute.cs

public class BasePageFilterAttribute : TypeFilterAttribute
{
    public BasePageFilterAttribute() : base(typeof(MyAuthorizationFilter))
    {
    }
}

// In /Common/BasePageModel.cs

[BasePageFilter] // Apply the filter attribute to the base class
public class BasePageModel : PageModel
{
    // No logic needed here, the attribute does the work
}

// In /Pages/Index.cshtml.cs

public class IndexModel : BasePageModel // Inherits the [BasePageFilter] attribute
{
    // ...
}

```