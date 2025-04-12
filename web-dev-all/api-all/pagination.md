# API-pagination

In API pagination, both page offset and cursor-based pagination are techniques used to handle large datasets by returning data in smaller, manageable chunks (pages). However, they differ significantly in how they achieve this, leading to different trade-offs in terms of performance, consistency, and implementation complexity.   

Here's a breakdown of the differences between page offset and cursor-based pagination:

Page Offset Pagination

How it works: This is the more traditional approach. It uses two parameters:
offset (or skip): Specifies the number of items to skip from the beginning of the dataset.   
limit (or size, take): Specifies the maximum number of items to return in the current page.   
To get to a specific page, you calculate the offset as (page_number - 1) * limit. For example, to get the third page with a limit of 10, the offset would be (3 - 1) * 10 = 20.
Pros:
Simplicity: It's relatively easy to understand and implement.
Direct Access: Allows clients to directly jump to a specific page by calculating the offset.
Familiarity: Widely supported and understood by developers.   
Cons:
Performance Issues with Large Offsets: As the offset value increases, the database might need to scan through a large number of records before returning the desired subset, leading to performance degradation.
Inconsistent Results in Dynamic Datasets: If new items are inserted or deleted while a user is paginating, the items on subsequent pages can shift, leading to skipped or duplicated results. The total number of pages can also become inaccurate.   
Cursor-Based Pagination (Also known as Keyset Pagination)

How it works: Instead of using an offset, cursor-based pagination uses a pointer or "cursor" to a specific item in the dataset. Subsequent requests then ask for the next set of items after or before that cursor.
The cursor is usually a unique, sequentially ordered field (like a timestamp, ID, or a combination of fields).   
The server provides the cursor for the next (and sometimes previous) page in the response.   
Pros:
Consistent Results: More stable results in dynamic datasets because it relies on the position relative to a specific item rather than an absolute offset. Insertions or deletions might affect the total number of items, but the sequence of items within the pages remains consistent.   
Better Performance for Large Datasets: Generally more efficient for large datasets because the database can use indexes on the cursor field to directly locate the starting point for the next page, without needing to scan through a large offset.   
Scalability: Performs better as the dataset grows.
Cons:
Complexity: Can be more complex to implement on both the server and client sides, especially when dealing with complex sorting or non-unique cursor fields.   
No Direct Access to Specific Pages: Clients cannot directly jump to an arbitrary page number without traversing through the preceding pages to obtain the necessary cursor.
Sorting Requirement: Typically requires a stable sort order based on the cursor field(s).
Here's a table summarizing the key differences:


Feature	Page Offset Pagination	Cursor-Based Pagination
Pagination Method	Skips a number of items (offset)	Navigates based on a pointer (cursor)
Key Parameters	offset, limit	cursor (after / before), limit
Direct Page Access	Yes	No
Performance (Large Datasets)	Degrades with large offsets	Remains relatively consistent
Data Consistency (Dynamic Datasets)	Can lead to skipped/duplicated items	More consistent results
Implementation Complexity	Simpler	More complex
Sorting Requirement	Less strict	Typically requires stable sorting

When to Use Which:

Page Offset Pagination:
Suitable for relatively small and static datasets where performance with larger offsets is not a major concern.
Appropriate when users need the ability to jump to specific page numbers (e.g., search results with a limited number of pages).
Cursor-Based Pagination:
Ideal for large and frequently updated datasets (e.g., social media feeds, activity streams, infinite scrolling).   
Preferred when data consistency and performance are critical, especially when dealing with many pages.
In modern API design, especially for applications dealing with significant amounts of data, cursor-based pagination is often recommended due to its better performance and consistency as the dataset scales. However, the choice ultimately depends on the specific requirements and constraints of the API and its consumers.   



```c#
using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.EntityFrameworkCore;

// Assuming you have an Entity Framework Core context named 'YourDbContext'
public class YourDbContext : DbContext
{
    public DbSet<Item> Items { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        // Replace with your actual database connection string
        optionsBuilder.UseInMemoryDatabase("YourDatabase");
    }
}

public class Item
{
    public int Id { get; set; }
    public DateTime CreatedAt { get; set; }
    public string Name { get; set; }
    // Add other relevant properties
}

public class PaginationResult<T>
{
    public List<T> Data { get; set; }
    public string NextCursor { get; set; }
    public string PreviousCursor { get; set; }
}

public class ItemService
{
    private readonly YourDbContext _context;

    public ItemService(YourDbContext context)
    {
        _context = context;
    }

    public PaginationResult<Item> GetItemsWithCursor(int pageSize = 10, string afterCursor = null, string beforeCursor = null)
    {
        IQueryable<Item> query = _context.Items.OrderBy(i => i.CreatedAt).ThenBy(i => i.Id); // Ensure stable sorting

        if (!string.IsNullOrEmpty(afterCursor))
        {
            // Decode the cursor (assuming it's a base64 encoded string of "CreatedAt:Id")
            var cursorParts = DecodeCursor(afterCursor);
            if (cursorParts != null)
            {
                DateTime cursorCreatedAt = cursorParts.CreatedAt;
                int cursorId = cursorParts.Id;
                query = query.Where(i => i.CreatedAt > cursorCreatedAt || (i.CreatedAt == cursorCreatedAt && i.Id > cursorId));
            }
        }
        else if (!string.IsNullOrEmpty(beforeCursor))
        {
            // For reverse pagination (optional, but good to illustrate)
            var cursorParts = DecodeCursor(beforeCursor);
            if (cursorParts != null)
            {
                DateTime cursorCreatedAt = cursorParts.CreatedAt;
                int cursorId = cursorParts.Id;
                query = _context.Items.OrderByDescending(i => i.CreatedAt).ThenByDescending(i => i.Id); // Reverse order
                query = query.Where(i => i.CreatedAt < cursorCreatedAt || (i.CreatedAt == cursorCreatedAt && i.Id < cursorId));
            }
        }

        var items = query.Take(pageSize).ToList();
        string nextCursor = null;
        string previousCursor = null;

        if (items.Count == pageSize)
        {
            var lastItem = items.Last();
            nextCursor = EncodeCursor(lastItem.CreatedAt, lastItem.Id);
        }

        if (!string.IsNullOrEmpty(beforeCursor))
        {
            // If we paginated backwards, the first item is the "next" in the original order
            if (items.Any())
            {
                var firstItem = items.First();
                previousCursor = EncodeCursor(firstItem.CreatedAt, firstItem.Id);
            }
            items.Reverse(); // Revert the order for the response
        }
        else if (!string.IsNullOrEmpty(afterCursor))
        {
            // If we paginated forwards, the first item of the current page is the "previous"
            if (items.Any())
            {
                var firstItem = items.First();
                previousCursor = EncodeCursor(firstItem.CreatedAt, firstItem.Id);
            }
        }
        else
        {
            // For the first page, there's no previous cursor
            if (items.Count > 0)
            {
                // To get the "previous" for the next backward navigation, we'd need the first item
                var firstItem = _context.Items.OrderBy(i => i.CreatedAt).ThenBy(i => i.Id).FirstOrDefault();
                if (firstItem != null && items.Any())
                {
                    if (firstItem.CreatedAt != items.First().CreatedAt || firstItem.Id != items.First().Id)
                    {
                        // This logic for the very first page's "previous" is a bit more complex and might not always be needed.
                        // A simpler approach is to only provide a previous cursor on subsequent backward navigations.
                    }
                }
            }
        }

        return new PaginationResult<Item>
        {
            Data = items,
            NextCursor = nextCursor,
            PreviousCursor = previousCursor
        };
    }

    private string EncodeCursor(DateTime createdAt, int id)
    {
        var plainTextBytes = System.Text.Encoding.UTF8.GetBytes($"{createdAt.ToString("o")}:{id}");
        return Convert.ToBase64String(plainTextBytes);
    }

    private (DateTime CreatedAt, int Id)? DecodeCursor(string cursor)
    {
        try
        {
            var base64EncodedBytes = Convert.FromBase64String(cursor);
            var plainText = System.Text.Encoding.UTF8.GetString(base64EncodedBytes);
            var parts = plainText.Split(':');
            if (parts.Length == 2 && DateTime.TryParseExact(parts[0], "o", null, System.Globalization.DateTimeStyles.RoundtripKind, out var createdAt) && int.TryParse(parts[1], out var id))
            {
                return (createdAt, id);
            }
        }
        catch (FormatException)
        {
            // Handle invalid cursor format
        }
        return null;
    }
}

public class Example
{
    public static void Main(string[] args)
    {
        using (var context = new YourDbContext())
        {
            // Seed some data
            if (!context.Items.Any())
            {
                context.Items.AddRange(
                    new Item { CreatedAt = DateTime.UtcNow.AddSeconds(1), Name = "Item A" },
                    new Item { CreatedAt = DateTime.UtcNow.AddSeconds(2), Name = "Item B" },
                    new Item { CreatedAt = DateTime.UtcNow.AddSeconds(2), Name = "Item C" }, // Same CreatedAt, different ID
                    new Item { CreatedAt = DateTime.UtcNow.AddSeconds(3), Name = "Item D" },
                    new Item { CreatedAt = DateTime.UtcNow.AddSeconds(4), Name = "Item E" },
                    new Item { CreatedAt = DateTime.UtcNow.AddSeconds(5), Name = "Item F" },
                    new Item { CreatedAt = DateTime.UtcNow.AddSeconds(6), Name = "Item G" }
                );
                context.SaveChanges();
            }

            var itemService = new ItemService(context);

            Console.WriteLine("--- First Page ---");
            var firstPage = itemService.GetItemsWithCursor(pageSize: 3);
            foreach (var item in firstPage.Data)
            {
                Console.WriteLine($"ID: {item.Id}, CreatedAt: {item.CreatedAt}, Name: {item.Name}");
            }
            Console.WriteLine($"Next Cursor: {firstPage.NextCursor}");
            Console.WriteLine($"Previous Cursor: {firstPage.PreviousCursor}");

            if (!string.IsNullOrEmpty(firstPage.NextCursor))
            {
                Console.WriteLine("\n--- Second Page ---");
                var secondPage = itemService.GetItemsWithCursor(pageSize: 3, afterCursor: firstPage.NextCursor);
                foreach (var item in secondPage.Data)
                {
                    Console.WriteLine($"ID: {item.Id}, CreatedAt: {item.CreatedAt}, Name: {item.Name}");
                }
                Console.WriteLine($"Next Cursor: {secondPage.NextCursor}");
                Console.WriteLine($"Previous Cursor: {secondPage.PreviousCursor}");

                if (!string.IsNullOrEmpty(secondPage.PreviousCursor))
                {
                    Console.WriteLine("\n--- Going back to First Page ---");
                    var previousPage = itemService.GetItemsWithCursor(pageSize: 3, beforeCursor: secondPage.PreviousCursor);
                    foreach (var item in previousPage.Data)
                    {
                        Console.WriteLine($"ID: {item.Id}, CreatedAt: {item.CreatedAt}, Name: {item.Name}");
                    }
                    Console.WriteLine($"Next Cursor: {previousPage.NextCursor}");
                    Console.WriteLine($"Previous Cursor: {previousPage.PreviousCursor}");
                }
            }
        }
    }
}

```

C#

using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.EntityFrameworkCore;

// Assuming you have an Entity Framework Core context named 'YourDbContext'
public class YourDbContext : DbContext
{
    public DbSet<Item> Items { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        // Replace with your actual database connection string
        optionsBuilder.UseInMemoryDatabase("YourDatabase");
    }
}

public class Item
{
    public int Id { get; set; }
    public DateTime CreatedAt { get; set; }
    public string Name { get; set; }
    // Add other relevant properties
}

public class PaginationResult<T>
{
    public List<T> Data { get; set; }
    public string NextCursor { get; set; }
    public string PreviousCursor { get; set; }
}

public class ItemService
{
    private readonly YourDbContext _context;

    public ItemService(YourDbContext context)
    {
        _context = context;
    }

    public PaginationResult<Item> GetItemsWithCursor(int pageSize = 10, string afterCursor = null, string beforeCursor = null)
    {
        IQueryable<Item> query = _context.Items.OrderBy(i => i.CreatedAt).ThenBy(i => i.Id); // Ensure stable sorting

        if (!string.IsNullOrEmpty(afterCursor))
        {
            // Decode the cursor (assuming it's a base64 encoded string of "CreatedAt:Id")
            var cursorParts = DecodeCursor(afterCursor);
            if (cursorParts != null)
            {
                DateTime cursorCreatedAt = cursorParts.CreatedAt;
                int cursorId = cursorParts.Id;
                query = query.Where(i => i.CreatedAt > cursorCreatedAt || (i.CreatedAt == cursorCreatedAt && i.Id > cursorId));
            }
        }
        else if (!string.IsNullOrEmpty(beforeCursor))
        {
            // For reverse pagination (optional, but good to illustrate)
            var cursorParts = DecodeCursor(beforeCursor);
            if (cursorParts != null)
            {
                DateTime cursorCreatedAt = cursorParts.CreatedAt;
                int cursorId = cursorParts.Id;
                query = _context.Items.OrderByDescending(i => i.CreatedAt).ThenByDescending(i => i.Id); // Reverse order
                query = query.Where(i => i.CreatedAt < cursorCreatedAt || (i.CreatedAt == cursorCreatedAt && i.Id < cursorId));
            }
        }

        var items = query.Take(pageSize).ToList();
        string nextCursor = null;
        string previousCursor = null;

        if (items.Count == pageSize)
        {
            var lastItem = items.Last();
            nextCursor = EncodeCursor(lastItem.CreatedAt, lastItem.Id);
        }

        if (!string.IsNullOrEmpty(beforeCursor))
        {
            // If we paginated backwards, the first item is the "next" in the original order
            if (items.Any())
            {
                var firstItem = items.First();
                previousCursor = EncodeCursor(firstItem.CreatedAt, firstItem.Id);
            }
            items.Reverse(); // Revert the order for the response
        }
        else if (!string.IsNullOrEmpty(afterCursor))
        {
            // If we paginated forwards, the first item of the current page is the "previous"
            if (items.Any())
            {
                var firstItem = items.First();
                previousCursor = EncodeCursor(firstItem.CreatedAt, firstItem.Id);
            }
        }
        else
        {
            // For the first page, there's no previous cursor
            if (items.Count > 0)
            {
                // To get the "previous" for the next backward navigation, we'd need the first item
                var firstItem = _context.Items.OrderBy(i => i.CreatedAt).ThenBy(i => i.Id).FirstOrDefault();
                if (firstItem != null && items.Any())
                {
                    if (firstItem.CreatedAt != items.First().CreatedAt || firstItem.Id != items.First().Id)
                    {
                        // This logic for the very first page's "previous" is a bit more complex and might not always be needed.
                        // A simpler approach is to only provide a previous cursor on subsequent backward navigations.
                    }
                }
            }
        }

        return new PaginationResult<Item>
        {
            Data = items,
            NextCursor = nextCursor,
            PreviousCursor = previousCursor
        };
    }

    private string EncodeCursor(DateTime createdAt, int id)
    {
        var plainTextBytes = System.Text.Encoding.UTF8.GetBytes($"{createdAt.ToString("o")}:{id}");
        return Convert.ToBase64String(plainTextBytes);
    }

    private (DateTime CreatedAt, int Id)? DecodeCursor(string cursor)
    {
        try
        {
            var base64EncodedBytes = Convert.FromBase64String(cursor);
            var plainText = System.Text.Encoding.UTF8.GetString(base64EncodedBytes);
            var parts = plainText.Split(':');
            if (parts.Length == 2 && DateTime.TryParseExact(parts[0], "o", null, System.Globalization.DateTimeStyles.RoundtripKind, out var createdAt) && int.TryParse(parts[1], out var id))
            {
                return (createdAt, id);
            }
        }
        catch (FormatException)
        {
            // Handle invalid cursor format
        }
        return null;
    }
}

public class Example
{
    public static void Main(string[] args)
    {
        using (var context = new YourDbContext())
        {
            // Seed some data
            if (!context.Items.Any())
            {
                context.Items.AddRange(
                    new Item { CreatedAt = DateTime.UtcNow.AddSeconds(1), Name = "Item A" },
                    new Item { CreatedAt = DateTime.UtcNow.AddSeconds(2), Name = "Item B" },
                    new Item { CreatedAt = DateTime.UtcNow.AddSeconds(2), Name = "Item C" }, // Same CreatedAt, different ID
                    new Item { CreatedAt = DateTime.UtcNow.AddSeconds(3), Name = "Item D" },
                    new Item { CreatedAt = DateTime.UtcNow.AddSeconds(4), Name = "Item E" },
                    new Item { CreatedAt = DateTime.UtcNow.AddSeconds(5), Name = "Item F" },
                    new Item { CreatedAt = DateTime.UtcNow.AddSeconds(6), Name = "Item G" }
                );
                context.SaveChanges();
            }

            var itemService = new ItemService(context);

            Console.WriteLine("--- First Page ---");
            var firstPage = itemService.GetItemsWithCursor(pageSize: 3);
            foreach (var item in firstPage.Data)
            {
                Console.WriteLine($"ID: {item.Id}, CreatedAt: {item.CreatedAt}, Name: {item.Name}");
            }
            Console.WriteLine($"Next Cursor: {firstPage.NextCursor}");
            Console.WriteLine($"Previous Cursor: {firstPage.PreviousCursor}");

            if (!string.IsNullOrEmpty(firstPage.NextCursor))
            {
                Console.WriteLine("\n--- Second Page ---");
                var secondPage = itemService.GetItemsWithCursor(pageSize: 3, afterCursor: firstPage.NextCursor);
                foreach (var item in secondPage.Data)
                {
                    Console.WriteLine($"ID: {item.Id}, CreatedAt: {item.CreatedAt}, Name: {item.Name}");
                }
                Console.WriteLine($"Next Cursor: {secondPage.NextCursor}");
                Console.WriteLine($"Previous Cursor: {secondPage.PreviousCursor}");

                if (!string.IsNullOrEmpty(secondPage.PreviousCursor))
                {
                    Console.WriteLine("\n--- Going back to First Page ---");
                    var previousPage = itemService.GetItemsWithCursor(pageSize: 3, beforeCursor: secondPage.PreviousCursor);
                    foreach (var item in previousPage.Data)
                    {
                        Console.WriteLine($"ID: {item.Id}, CreatedAt: {item.CreatedAt}, Name: {item.Name}");
                    }
                    Console.WriteLine($"Next Cursor: {previousPage.NextCursor}");
                    Console.WriteLine($"Previous Cursor: {previousPage.PreviousCursor}");
                }
            }
        }
    }
}
Explanation:

Item Entity and YourDbContext:

We define a simple Item entity with Id, CreatedAt, and Name properties.
YourDbContext is a basic Entity Framework Core context, configured to use an in-memory database for this example. In a real application, you'd connect to your actual database.
PaginationResult<T>:

A generic class to hold the paginated data, the NextCursor for fetching the next page, and the PreviousCursor for fetching the previous page (for bidirectional pagination).
ItemService and GetItemsWithCursor Method:

ItemService encapsulates the logic for fetching items with cursor-based pagination.
GetItemsWithCursor takes pageSize, afterCursor, and beforeCursor as parameters.
Stable Sorting: The query always orders the Items by CreatedAt and then by Id. This is crucial for cursor-based pagination to work correctly, especially when there might be items with the same CreatedAt. The cursor needs to uniquely identify a point in the ordered dataset.
Handling Cursors:
If afterCursor is provided:
The cursor is decoded using DecodeCursor to get the CreatedAt and Id of the last item on the previous page.
The query filters for items where CreatedAt is greater than the cursor's CreatedAt, or where CreatedAt is equal but the Id is greater. This ensures we get items strictly after the cursor.
If beforeCursor is provided (for reverse pagination):
The query is ordered in descending order.
The filtering logic is adjusted to get items strictly before the cursor.
Fetching Data: query.Take(pageSize).ToList() fetches the specified number of items.
Generating Next Cursor: If the number of items fetched is equal to pageSize, it means there might be more items. The CreatedAt and Id of the last item in the current page are encoded into the nextCursor.
Generating Previous Cursor:
For backward pagination (beforeCursor is set), the previousCursor is generated from the first item of the current (reversed) page.
For forward pagination (afterCursor is set), the previousCursor is generated from the first item of the current page.
For the very first page, the previousCursor is typically null.
Encoding and Decoding Cursors:
EncodeCursor converts the CreatedAt (formatted as a sortable string) and Id into a base64 encoded string. This is a common way to make the cursor opaque and URL-safe.
DecodeCursor reverses this process to extract the CreatedAt and Id.
EncodeCursor and DecodeCursor:

These helper methods handle the encoding and decoding of the cursor. The cursor in this example is a combination of the CreatedAt and Id, separated by a colon, and then base64 encoded. You can choose a different encoding mechanism if needed.
Example.Main Method:

Sets up an in-memory database and seeds some sample Item data.
Demonstrates how to use the GetItemsWithCursor method to fetch the first page, then the second page using the nextCursor from the first, and then how to go back to the first page using the previousCursor from the second.
Key Concepts for Cursor-Based Pagination:

Stable Sorting: You must have a consistent and deterministic way to order your data. If the order changes between requests, cursor-based pagination will produce incorrect results. Usually, a timestamp or a unique ID (or a combination) is used for sorting.
Opaque Cursors: It's generally a good practice to make your cursors opaque (like the base64 encoded string in the example). This prevents clients from trying to interpret or manipulate the cursor value.
Bidirectional Pagination (Optional but Recommended): Providing both nextCursor and previousCursor allows for more flexible navigation.
Handling Edge Cases: Consider how to handle the beginning and end of the dataset (when nextCursor or previousCursor will be null).
Performance: Ensure that the fields you are using for sorting and filtering (the cursor fields) are properly indexed in your database to optimize query performance.
This C# example provides a basic implementation of cursor-based pagination using Entity Framework Core. You'll need to adapt it to your specific database and data model. Remember to handle potential errors (e.g., invalid cursor format) in a production environment.

