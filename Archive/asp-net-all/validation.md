# Validation

## Main Steps

- Add validation attribute to the View Model properties
- Use <spna asp-validation-for"..."> in the view
- Check ModelState.Is Valid in the controller

## Server-Side Validation Flow

When I decorate my ViewModel with attributes:

- ASP.NET core uses Model Binding to populate the ViewModel form the form data.
- Then it runs the Model Validation using the attributes.
- If any validation fails, ModelState.IsValid becomes false, and the errors are stored in ModelState.

## Client-Side Validation Flow

ASP.NET Core MVC uses Unobtrusive Validation powered by jQuery Validation. 

### Tag Helps Generate HTML Attributes. 

These data-val-* attributes are key to client-side validation.
  
```cs
<input asp-for="Username" />
<span asp-validation-for="Username"></span>

<input name="Username" id="Username" data-val="true" data-val-required="Username is required." />
<span class="text-danger field-validation-valid" data-valmsg-for="Username" data-valmsg-replace="true"></span>
```

### JavaScript Libraries Involved

To enable client-side validation, my view must include:

```cs
<script src="~/lib/jquery/dist/jquery.min.js"></script>
<script src="~/lib/jquery-validation/dist/jquery.validate.min.js"></script>
<script src="~/lib/jquery-validation-unobtrusive/jquery.validate.unobtrusive.min.js"></script>
```

- These scripts:
  - Read the data-val-* attributes
  - Hook into form submission
  - Prevent submission if validation fails
  - Display error messages in <span asp-validation-for="...">

### Triggering Validation

- Validation is triggered:
  - On form submission
  - On input change or blur (depending on jQuery Validation settings)

If validation fails, the form is not submitted, and error messages appear next to the fields.

## Custom Validation Attributes and Client-Side Support

If you create a custom attribute (like NoSpecialCharacters), it works only server-side unless you:

- Implement IClientModelValidator in your attribute
- Add a custom jQuery validation method

## The Custom Validation

### Create Validation Attribute

```cs
using System.ComponentModel.DataAnnotations;

public class NoSpecialCharactersAttribute : ValidationAttribute
{
    protected override ValidationResult IsValid(object value, ValidationContext validationContext)
    {
        if (value is string strValue)
        {
            if (System.Text.RegularExpressions.Regex.IsMatch(strValue, @"^[a-zA-Z0-9 ]*$"))
            {
                return ValidationResult.Success;
            }
            else
            {
                return new ValidationResult("The field must not contain special characters.");
            }
        }

        return ValidationResult.Success;
    }
}
```

### Apply the Custom Validator to My Model

```code
public class UserViewModel
{
    [Required]
    [NoSpecialCharacters]
    public string Username { get; set; }
}
```

### Handle Validation in Contoller

```code
[HttpPost]
public IActionResult Create(UserViewModel model)
{
    if (!ModelState.IsValid)
    {
        return View(model);
    }

    // Proceed with valid data
    return RedirectToAction("Success");
}
```

### Client-Side Validation

ASP.NET Core doesn’t automatically support custom client-side validation. To add it:

- Create a custom jQuery validation method.
- Register it using $.validator.addMethod.
- Use data-val attributes or a custom IClientModelValidator.
