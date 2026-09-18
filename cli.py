def greet(*, name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    import sys
    print(greet(name=sys.argv[1] if len(sys.argv) > 1 else "world"))
