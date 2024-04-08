"""
Imagine that you are running a bookstrore. Below is a list of dictionaries
that contains the title, author, genre, quantity sold in the last year, and the
price sold. You will use this data to create a dataframe, then perform various
analysis to decide what to restock etc.

Reminder: Import pandas before you start!
"""

books_data = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Classic", "quantity_sold": 30, "price": 8.99},
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian", "quantity_sold": 42, "price": 9.99},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic", "quantity_sold": 25, "price": 7.99},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Classic", "quantity_sold": 34, "price": 8.49},
    {"title": "Brave New World", "author": "Aldous Huxley", "genre": "Dystopian", "quantity_sold": 18, "price": 9.49}
]

"""
EXCERCISE 1

Use the data provided to create a dataframe. This is not the only dataframe that
you will be creating so call it df_books.
"""

"""
EXCERCISE 2

We want to create a subset of this data that contains infromation that we can
share with the public e.g. it excludes variables such as quantity sold. 
We want this part of the code to be as flexible as possible so...
 
1. Create a list named "excluded_variables" - it contains only "quantity_sold"
2. Create a dataset named df_public that excludes all variable names in quantity_sold

It is not necessary that df_public be a copy of this list.

Hint: Suppose x is a string and y is a list of strings. Recall that the condition

if x not in y:

will be True if string x is not list y
"""

"""
EXCERCISE 3

Create a new column called revenue that is the product of the quantity and
price. 

Hint: Creating a new series is easy! Let df be the name of your dataframe.
The 'x' and 'y' be the names of two columns that contain integers. 
Then the sum of those can be generated in a series named 'sum' using 

df['sum'] = df['x'] + df['y']
"""

"""
EXCERCISE 4

Find the three most lucrative titles sold and copy those titles and that
list into a new dataframe called df_bestsellers. 

To do so, you can try to figure it out on your own or follow the instructions
below...

1. Sort the dataframe by revenue. Makes sure that the it is in descending order.
Store this in a new dataset called df_books_sorted. Print this to take a look at it

Hint: Each dataframe has a method named sort_values(). So if wanted to sort
the books by cheapest first:

df_books_sorted = df_books.sort_values(by="price", ascending=True)

2. Note that this does NOT change the index numbers! To do that, create a list
of integers and renumber use it to renumber df_books_sorted using df.index = [list_name]

Hint: [x for x in range(3)] generates [0, 1, 2]

3. Create a new dataframe named df_bestsellers using loc that contains 
only the top 3 rows and the columns named title and revenue. Use .copy() to ensure
that this is copy, not a view of the original df_books

"""