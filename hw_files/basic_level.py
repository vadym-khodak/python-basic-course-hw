import random


def read_write_file(file_name: str, text: str) -> tuple:
    with open(file_name, "w") as file:
        file.write(text)
    with open(file_name, "a") as file:
        file.write("\n")
        file.write(str(random.randint(1, 10)))
    with open(file_name, "r") as file:
        file_text, number = file.read().split("\n")
    with open(f"new_{file_name}", "w") as file:
        for _ in range(int(number)):
            file.write(file_text)
            file.write("\n")
    with open(f"new_{file_name}", "r") as file:
        file_text = file.read()

    return int(number), file_text


if __name__ == "__main__":
    print(read_write_file("temp.txt", "Hello World!"))
