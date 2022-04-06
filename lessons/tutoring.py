
def hello_world(n: int) -> str:
    i: int = 0
    out: str = ""
    while i < n:
        out += "hello, world\n"
        i += 1

    return out


def waffle() -> None:
    some_var: int = int(input("Enter a number: "))
    message: str = hello_world(some_var)
    print(message)


waffle()