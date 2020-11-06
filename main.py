
class FuncAdd:
    func_list = []

    def __init__(self, func):
        self.name = func.__name__
        FuncAdd.func_list.append(func)

    def __call__(self, *args, **kwargs):
        result = tuple(func(*args, **kwargs) for func in FuncAdd.func_list if func.__name__ == self.name)
        if len(result) > 0:
            return result
        else:
            raise NameError

    @staticmethod
    def delete(func):
        index = 0
        length = len(FuncAdd.func_list)
        while index < length:
            if FuncAdd.func_list[index].__name__ == func.name:
                del FuncAdd.func_list[index]
                length -= 1
                continue
            else:
                index += 1

    @staticmethod
    def clear():
        FuncAdd.func_list.clear()


@FuncAdd
def foo():
    return 'Hello'


@FuncAdd
def foo():
    return 'World'


@FuncAdd
def foo2():
    return 'Bye'


@FuncAdd
def foo2():
    return 'Earth'


print(foo())
FuncAdd.delete(foo)
print(foo2())
FuncAdd.clear()
print(foo2())
