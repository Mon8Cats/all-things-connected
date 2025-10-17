# Page Model

The conventional order for members within a C# class, including an ASP.NET Core Razor Pages PageModel or your custom AuthBasePageModel, emphasizes readability and logical flow.

Here is the widely accepted convention, which generally follows a pattern of Fields, Properties, Constructors, and Methods:

Order,Member Type,Accessibility/Usage,Example
1,Constants and Static Fields,"const, static readonly","private const string Key = ""Data"";"
2,Private Fields (Attributes),private or protected fields (often prefixed with _) that back properties or hold injected services.,private readonly ILogger<T> _logger;
3,Public Properties,"Public properties exposed for the view (.cshtml), often using the [BindProperty] attribute.",public string Message { get; set; }
4,Constructor,Used for dependency injection and initial setup.,public AuthBasePageModel(IUserService service)
5,Lifecycle/Filter Methods,"Implementation of IPageFilter or IAsyncPageFilter methods, ensuring they run before handlers.",public async Task OnPageHandlerExecutionAsync(...)
6,Handler Methods,"The main logic handlers for specific HTTP verbs (OnGet, OnPost, etc.).",public async Task<IActionResult> OnGetAsync()
7,Other Public Methods,Utility methods intended for use by child classes or services.,protected string GetCurrentUserEmail()
8,Other Private Methods,Private utility/helper methods only used within the current class.,private void LogAction(string action)

Example Implementation in AuthBasePageModel
Applying this convention to your base class:

```cs
public abstract class AuthBasePageModel : PageModel, IAsyncPageFilter
{
    // ------------------------------------
    // 2. PRIVATE FIELDS (ATTRIBUTES)
    // ------------------------------------
    private readonly IUserService _userService;
    
    // ------------------------------------
    // 3. PUBLIC PROPERTIES (Including Bindable and Read-Only)
    // ------------------------------------
    // Property to hold the full user information fetched from the DB
    public ApplicationUser CurrentUser { get; private set; } 

    // ------------------------------------
    // 4. CONSTRUCTOR
    // ------------------------------------
    public AuthBasePageModel(IUserService userService)
    {
        _userService = userService;
    }

    // ------------------------------------
    // 5. LIFECYCLE/FILTER METHODS
    // ------------------------------------
    public Task OnPageHandlerSelectionAsync(PageHandlerSelectedContext context)
    {
        // IPageFilter implementation
        return Task.CompletedTask;
    }
    
    public virtual async Task OnPageHandlerExecutionAsync(PageHandlerExecutingContext context, PageHandlerExecutionDelegate next)
    {
        // Logic to fetch CurrentUser before any handler executes
        var userId = User.FindFirst(ClaimTypes.NameIdentifier)?.Value;
        // CurrentUser = await _userService.GetUserByIdAsync(userId); 
        
        await next();
    }

    // ------------------------------------
    // 7. OTHER PUBLIC/PROTECTED METHODS
    // ------------------------------------
    protected bool IsUserAdmin()
    {
        // Helper method using CurrentUser data
        return CurrentUser?.Role == "Admin";
    }
}
```

## Methods

The choice between OnPageHandlerExecutionAsync() and OnGetAsync() depends entirely on whether you need that authentication logic to run only for GET requests or for all requests (GET, POST, PUT, DELETE, etc.) on that page.

Here is the breakdown:

Feature,OnPageHandlerExecutionAsync() (IPageFilter),OnGetAsync() (Handler Method)
When it runs,"Before any specific handler (OnGet, OnPost, OnPut, etc.) executes.",Only when an HTTP GET request is made.
Scope,"Executes for all HTTP verbs on the page (GET, POST, etc.).",Executes for only the GET verb.
Base Class Suitability,Excellent. It applies the logic globally to the page lifecycle in a DRY (Don't Repeat Yourself) way.,"Less Suitable. Only covers GET requests; you'd need to duplicate logic in OnPostAsync(), etc."
Primary Use,"Cross-cutting concerns like global authorization, logging, or setting common data needed regardless of the form action.",Retrieving initial data specifically for the page view.
Recommendation,Recommended for your scenario (fetching user data after auth) to ensure the data is available for both GET (display) and POST (submit) requests.,Only recommended if you only need the data for the initial page load.

Conclusion: Use OnPageHandlerExecutionAsync()
For fetching additional, essential user information from the database that is required for any operation on the page (displaying the page, processing a form submission, etc.), OnPageHandlerExecutionAsync() in your Base PageModel is the superior choice.

Rationale
Completeness: It guarantees the user data is retrieved and available in the CurrentUser property (or whatever you name it) before the code in OnGetAsync(), OnPostAsync(), or any other handler runs.

DRY Principle: You define the user lookup logic once in the base class filter. If you used OnGetAsync(), you would have to remember to call the base OnGetAsync() from the child class's OnGetAsync(), and you would have to duplicate the logic inside OnPostAsync(), OnPutAsync(), etc. to ensure the data is available after a form submission.

Correct Lifecycle Stage: It is the direct equivalent of an action filter's execution stage in MVC, designed for pre-execution tasks that affect the whole page operation.


```cs
// In your AuthBasePageModel.cs
public abstract class AuthBasePageModel : PageModel, IAsyncPageFilter
{
    // ... Service Injection ...

    public async Task OnPageHandlerExecutionAsync(PageHandlerExecutingContext context, PageHandlerExecutionDelegate next)
    {
        // Logic runs for GET, POST, etc. before the handler method executes.
        
        // 1. Fetch user data from DB using User.Identity information
        // CurrentUser = await _userService.GetUserByIdAsync(User.Identity.Name);
        
        // 2. Call next() to proceed to the specific handler (e.g., OnGet, OnPost)
        var resultContext = await next();
        
        // Logic after the handler executes can go here (OnPageHandlerExecuted equivalent)
    }

    public Task OnPageHandlerSelectionAsync(PageHandlerSelectedContext context)
    {
        // Must be implemented for IAsyncPageFilter, but often left empty if no logic needed
        return Task.CompletedTask;
    }
}


using Microsoft.AspNetCore.Mvc.Filters;
using Microsoft.AspNetCore.Mvc.RazorPages;
using System.Threading.Tasks;

// In your AuthBasePageModel.cs
public abstract class AuthBasePageModel : PageModel, IAsyncPageFilter
{
    // ... Properties and constructor ...

    // The asynchronous version of the pre-handler execution method.
    public async Task OnPageHandlerExecutionAsync(PageHandlerExecutingContext context, PageHandlerExecutionDelegate next)
    {
        // 1. Logic BEFORE the Page Handler (e.g., OnGetAsync, OnPostAsync) runs.
        // This is the functional equivalent to OnActionExecuting.
        
        // Example: Go to database and fetch user data (as you wanted).
        var userId = User.FindFirst(ClaimTypes.NameIdentifier)?.Value;
        // CurrentUser = await _userService.GetUserByIdAsync(userId); 
        // Logic to populate CurrentUser property happens here.

        // 2. Call 'next()' to execute the actual Page Handler method (OnGet/OnPost)
        var resultContext = await next();
        
        // 3. Logic AFTER the Page Handler runs (equivalent to OnActionExecuted).

        // You can check resultContext.Result here if needed.
    }

    // You must also implement OnPageHandlerSelectionAsync for IAsyncPageFilter
    public Task OnPageHandlerSelectionAsync(PageHandlerSelectedContext context)
    {
        // This runs earlier than OnPageHandlerExecutionAsync (before model binding).
        return Task.CompletedTask;
    }
}
```

## OnPageHandlerExecuting(PageHandlerExecutingContext)

Razor Page Method,Runs...,Equivalent MVC Filter Method
OnPageHandlerSelected,"After the handler method (e.g., OnGet, OnPost) has been selected, but before model binding occurs.",Closest to Resource Filters
OnPageHandlerExecuting,"Before the handler method executes, and after model binding is complete.",Closely matches OnActionExecuting
OnPageHandlerExecuted,"After the handler method executes, but before the action result (like Page()) is executed.",Closely matches OnActionExecuted

The Recommended Method
For the logic you described (fetching user data from the database), you want the method that runs after the URL routing is complete and before the main handler (OnGet/OnPost) logic begins.

You can use the synchronous or asynchronous version, but OnPageHandlerExecutionAsync is better for database calls:

```cs
using Microsoft.AspNetCore.Mvc.Filters;
using Microsoft.AspNetCore.Mvc.RazorPages;
using System.Threading.Tasks;

// In your AuthBasePageModel.cs
public abstract class AuthBasePageModel : PageModel, IAsyncPageFilter
{
    // ... Properties and constructor ...

    // The asynchronous version of the pre-handler execution method.
    public async Task OnPageHandlerExecutionAsync(PageHandlerExecutingContext context, PageHandlerExecutionDelegate next)
    {
        // 1. Logic BEFORE the Page Handler (e.g., OnGetAsync, OnPostAsync) runs.
        // This is the functional equivalent to OnActionExecuting.
        
        // Example: Go to database and fetch user data (as you wanted).
        var userId = User.FindFirst(ClaimTypes.NameIdentifier)?.Value;
        // CurrentUser = await _userService.GetUserByIdAsync(userId); 
        // Logic to populate CurrentUser property happens here.

        // 2. Call 'next()' to execute the actual Page Handler method (OnGet/OnPost)
        var resultContext = await next();
        
        // 3. Logic AFTER the Page Handler runs (equivalent to OnActionExecuted).

        // You can check resultContext.Result here if needed.
    }

    // You must also implement OnPageHandlerSelectionAsync for IAsyncPageFilter
    public Task OnPageHandlerSelectionAsync(PageHandlerSelectedContext context)
    {
        // This runs earlier than OnPageHandlerExecutionAsync (before model binding).
        return Task.CompletedTask;
    }
}
```

