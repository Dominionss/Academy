class MyOpen:
    def __init__(self, file_name, mode="r", encoding="utf-8"):
        self.file_name = file_name
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        return False


if __name__ == "__main__":
    with MyOpen("text.txt", "w") as file:
        file.write("Hello, World!")

    with MyOpen("test.txt", "r") as file:
        print(file.read())
