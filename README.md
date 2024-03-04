**Functions:**

Functions are blocks of reusable code that perform a specific task. They help organize code into manageable pieces and promote code reuse. In Python, functions are defined using the `def` keyword followed by the function name and parameters (if any). Here's a simple example:

```python
def greet(name):
    print("Hello, " + name + "!")
```

In this example, the `greet()` function takes a parameter `name` and prints a greeting message using that name.

**Conditional Statements:**

Conditional statements allow you to execute certain code blocks based on specific conditions. The commonly used conditional statements in Python are `if`, `elif` (short for "else if"), and `else`. Here's a simple example:

```python
x = 10

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
```

In this example, if `x` is greater than 0, the first print statement executes. If `x` is less than 0, the second print statement executes. Otherwise, if none of the conditions are met, the `else` block executes.

**For Loops:**

For loops are used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects. They repeatedly execute a block of code for each item in the sequence. Here's a simple example:

```python
for i in range(5):
    print(i)
```

This loop will print numbers from 0 to 4.

**While Loops:**

While loops repeatedly execute a block of code as long as a specified condition is true. They are useful when you don't know in advance how many times the loop will run. Here's a simple example:

```python
x = 0
while x < 5:
    print(x)
    x += 1
```

This loop will print numbers from 0 to 4.

**Global and Local Variables:**

Variables in Python can either be global or local. Global variables are defined outside of any function and can be accessed from anywhere in the code. Local variables are defined inside a function and can only be accessed within that function. Here's a simple example:

```python
global_var = 10

def my_function():
    local_var = 20
    print("Global variable:", global_var)
    print("Local variable:", local_var)

my_function()
```

In the example, `global_var` is a global variable, and `local_var` is a local variable.
