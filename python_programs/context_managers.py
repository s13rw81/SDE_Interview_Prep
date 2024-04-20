import contextlib

@contextlib.contextmanager
def my_context_manager(n = 0):
    # Setup code
    print("Entering the context")
    try:
        # This line indicates where the context manager should enter
        value = n
        yield f"Hello, World! - {value}"  # Any value yielded here can be accessed in the 'as' clause
        value += 1
    finally:
        # Teardown code
        print("Exiting the context")

# Using the context manager with the 'with' statement
for i in range(10):
    with my_context_manager(i) as value:
        print(value)  # Output: Hello, World!
