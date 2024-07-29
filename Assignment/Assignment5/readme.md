# Python Class Coding Questions

## Very Easy Questions

1. **Question:** Create a class called `Car` with an `__init__` method that takes a parameter `make` and assigns it to an instance variable. Then, instantiate an object of this class with the make `"Toyota"` and print the make of the car.

   **Expected Output:** 
   Toyota

2. **Question:** Write a class named `Dog` that has a method `bark` which prints `"Woof!"`. Create an instance of `Dog` and call the `bark` method.

   **Expected Output:** 
   Woof!

3. **Question:** Create a class `Rectangle` with attributes `width` and `height`. Add a method `area` that returns the area of the rectangle. Instantiate the class with width 4 and height 5, then print the area.

   **Expected Output:** 
   20

## Easy Questions

1. **Question:** Create a class `Person` with an `__init__` method that takes parameters `name` and `age`. Add a method `introduce` that returns a string `"Hi, my name is <name> and I am <age> years old."`. Instantiate the class and print the introduction.

   **Expected Output:** 
   Hi, my name is Alice and I am 30 years old.

2. **Question:** Define a class `BankAccount` with methods `deposit` and `withdraw`. Initialize the account with a balance of 1000. Deposit 500 and withdraw 200, then print the final balance.

   **Expected Output:** 
   1300

3. **Question:** Write a class `Student` with attributes `name` and `grade`. Add a method `is_passing` that returns `True` if the grade is 60 or above, otherwise returns `False`. Create a `Student` instance with grade 65 and print if the student is passing.

   **Expected Output:** 
   True

4. **Question:** Create a class `Circle` with an `__init__` method that takes a parameter `radius`. Add a method `circumference` that returns the circumference of the circle. Instantiate the class with a radius of 3 and print the circumference.

   **Expected Output:** 
   18.84955592153876

5. **Question:** Define a class `Library` that has a method `add_book` which takes a `title` and adds it to a list of books. Add a method `list_books` that returns the list of books. Instantiate the class, add a few books, and print the list of books.

   **Expected Output:** 
   ['The Great Gatsby', '1984', 'To Kill a Mockingbird']

6. **Question:** Create a class `Rectangle` with methods `perimeter` and `diagonal`. The `perimeter` method should return the perimeter of the rectangle, and the `diagonal` method should return the diagonal length. Instantiate the class with width 6 and height 8 and print both values.

   **Expected Output:** 
   Perimeter: 28 
   Diagonal: 10.0

## Medium Questions

1. **Question:** Create a class `Employee` with attributes `name` and `salary`. Add a method `give_raise` that increases the salary by a specified percentage. Instantiate the class, give a raise, and print the updated salary.

   **Expected Output:** 
   55000

2. **Question:** Write a class `LibraryMember` that has a method `borrow_book` which takes a book title and adds it to a list of borrowed books. Add a method `return_book` which removes a book from the list. Instantiate the class, borrow and return a book, and print the list of borrowed books.

   **Expected Output:** 
   ['Harry Potter', 'The Hobbit']

3. **Question:** Define a class `Point` with methods `distance_to` and `move_by`. The `distance_to` method should calculate the distance between two points. The `move_by` method should change the point's coordinates by given offsets. Instantiate the class and use these methods.

   **Expected Output:** 
   Distance: 5.0 
   New Coordinates: (3, 4)

4. **Question:** Create a class `Account` with methods `deposit` and `withdraw`. Implement a method `transfer` to transfer money between two accounts. Instantiate two accounts, transfer money between them, and print the balances.

   **Expected Output:** 
   Account 1 Balance: 800 
   Account 2 Balance: 1200

5. **Question:** Write a class `Task` with attributes `name` and `status`. Add a method `complete` that changes the status to `"Completed"`. Instantiate the class, mark the task as complete, and print the status.

   **Expected Output:** 
   Completed

6. **Question:** Create a class `Temperature` with methods to convert from Celsius to Fahrenheit and vice versa. Instantiate the class with a temperature in Celsius, convert it to Fahrenheit, and print the result.

   **Expected Output:** 
   86.0

## Hard Questions

1. **Question:** Create a class `Graph` with methods to add nodes and edges. Implement a method `find_shortest_path` that uses Dijkstra's algorithm to find the shortest path between two nodes. Instantiate the class, add nodes and edges, and print the shortest path.

   **Expected Output:** 
   Shortest path from A to D: ['A', 'B', 'D']

2. **Question:** Write a class `Matrix` with methods to add and multiply matrices. Implement a method `transpose` to return the transpose of the matrix. Instantiate the class, perform matrix operations, and print the results.

   **Expected Output:** 
   Added Matrix: [[6, 8], [10, 12]] 
   Multiplied Matrix: [[19, 22], [43, 50]] 
   Transposed Matrix: [[1, 3], [2, 4]]

3. **Question:** Define a class `DataAnalyzer` that can read data from a file, calculate statistics like mean, median, and mode, and print the results. Instantiate the class with a sample dataset and print the calculated statistics.

   **Expected Output:** 
   Mean: 3.0 
   Median: 3 
   Mode: 2

## Very Hard Question

1. **Question:** Create a class `EventManager` that can schedule events with start and end times, and allow for querying events by time range. Implement methods to add, remove, and list events. Instantiate the class, add some events, query events in a specific time range, and print the results.

   **Expected Output:** 
   Events between 9:00 and 12:00: ['Meeting', 'Conference']
