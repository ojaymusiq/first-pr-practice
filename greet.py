def greet(name):
    """Return a friendly greeting for the given name."""
    name = name.strip()
    if not name:
        return "Hello, stranger!"
    return f"Hello, {name}!"


if __name__ == "__main__":
    import sys

    print(greet(" ".join(sys.argv[1:])))
