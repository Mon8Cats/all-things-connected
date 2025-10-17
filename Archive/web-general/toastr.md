# Toastr

## Toastr.js

Toastr.js is a JavaScript library used to create "toast" notifications. These are small, non-intrusive pop-up messages that appear in a corner of the screen to provide feedback to the user without interrupting their workflow.

## What is it for?

Its primary purpose is to display various types of notifications to the user, such as:

- Success messages: Confirming that an action was completed successfully (e.g., "Item saved!").
- Error messages: Alerting the user to a problem (e.g., "Network error, please try again.").
- Warning messages: Providing a heads-up about a potential issue (e.g., "You are about to delete a file.").
- Informational messages: Giving general updates (e.g., "A new message has arrived.").

Toastr.js is a front-end solution that's easy to integrate into any web application, including those built with ASP.NET Core, and it's highly customizable in terms of appearance, position, and duration.

## Include the files:

- Include the Files: Add the toastr.js and its corresponding CSS files to your project. You can do this by using a CDN (Content Delivery Network), a package manager like npm or yarn, or by manually downloading the files. The easiest way is via a CDN.

```code
<link href="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.css" rel="stylesheet" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.js"></script>
```

- Call Toastr from JavaScript: You can trigger toast notifications from any of your JavaScript code. toastr.js provides simple methods for different types of messages.

```code
// Example: Display a success message
toastr.success('Item added successfully!', 'Success');

// Example: Display an error message
toastr.error('An error occurred.', 'Error');
```

You can also pass in options to customize the appearance and behavior of the toasts.

```code
toastr.options = {
    "closeButton": true,
    "positionClass": "toast-top-right",
    "timeOut": "5000" // 5 seconds
};
toastr.info('This is an info message.');
```

- Integrate with ASP.NET Core MVC (using TempData): A common pattern in MVC is to show notifications after a successful form submission or a redirect. You can use TempData to pass the message from your controller to the view.
  - Controller: Set the TempData values in your controller action.

```code
[HttpPost]
public async Task<IActionResult> Create(MyModel model)
{
    if (ModelState.IsValid)
    {
        // Save to database...
        TempData["SuccessMessage"] = "The item was created successfully!";
        return RedirectToAction("Index");
    }
    // ...handle errors
    return View(model);
}
```

  - View (_Layout.cshtml or a specific view): Add a small JavaScript block to check for and display the TempData messages. Placing this in _Layout.cshtml ensures the toasts appear on every page.

```code
@if (TempData["SuccessMessage"] != null)
{
    <script type="text/javascript">
        $(document).ready(function() {
            toastr.success('@Html.Raw(TempData["SuccessMessage"])');
        });
    </script>
}
```

This approach is simple and effective for displaying notifications after redirects. For AJAX-based form submissions, you should handle the toast directly in your JavaScript success and error callbacks.