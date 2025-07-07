from src.decorators import hello

if __name__ == "__main__":
    hello()


@log(filename="Сюда пиши да.txt")
@log()
def hello():
    print("Hi!")
