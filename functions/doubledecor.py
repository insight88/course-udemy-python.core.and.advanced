def decorfun(fun):
    def inner():
        result = fun()
        return result*2
    return inner


@decorfun
# ? return값이 자동으로 at decorfun의 parameter로 지정됨
def num():
  # ? decorfun에 parameter로 제공되는 function
    return 5


print(num())
