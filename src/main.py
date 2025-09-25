def main() -> None:
    """Entry point for the python-project application."""
    print('Hello from python-project!')

    # Pythonic way: use list comprehension or built-in function
    x = list(range(10))  # Most Pythonic - direct conversion
    # Alternative: x = [i for i in range(10)]  # List comprehension
    print(f'Generated list: {x}')


if __name__ == '__main__':
    main()
