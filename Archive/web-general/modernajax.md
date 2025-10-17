# AJAX

## Old way -> new way

```code
Uses the $.post(url, data, successCallback).fail(failCallback) syntax.
Uses the modern promise-based $.post(url, data).done(successCallback).fail(failCallback).always(finalCallback) syntax.

Your .post's fail callback handles network errors. Your .post's success callback's else block handles validation errors.
My code uses .done() for successful responses (including validation errors) and a separate .fail() for network errors, which is a cleaner separation of concerns.

You have a toastr.clear and submitBtn.prop call in both the .post callback and the .fail callback.

My code moves the button state logic to the .always() callback, which guarantees it runs whether the AJAX call succeeds or fails. This is more reliable and prevents code duplication.

Your code shows a toastr.error for a general server error and then a toastr.warning for each validation error. This often leads to a "double-toast" effect.
My code simplifies the error handling to either show a general error toast from the server or a warning toast for each specific validation error, but not both.


```


## robust, readable, and less prone to bugs

- Callback Chaining: My code uses the more modern and standard promise-based chaining with .done(), .fail(), and .always(). This clearly separates the logic for a successful HTTP response (handled by .done), a failed HTTP response (handled by .fail), and logic that must execute regardless of the outcome (handled by .always).
- Logic Separation: The .done() block in my code is for successful HTTP requests (status 200). This is where you check the response.success flag to determine if it was a successful form submission or a validation failure. The .fail() block is exclusively for unsuccessful HTTP requests (e.g., 404, 500). Your code handles validation errors within the success callback, which is correct, but the structure is less explicit.
- Code Consistency: Your code duplicates logic by calling toastr.clear and submitBtn.prop('disabled', false) in both the success and failure callbacks. My code places this shared logic in the .always() callback, which is a key feature of the promise-based syntax. This makes your code more concise and less error-prone.