def decorate_add(func):
    def inner(*args, **kwargs):
        # print(a, b)
        extra_sum = sum(args[1:])
        sum_a = func(args[0], extra_sum)
        return sum_a

    return inner


def paramterised_decorator(multiply=1):
    def wrapper(func):
        def inner(*args, **kwargs):
            extra_sum = sum(args[1:])
            sum_a = func(args[0], extra_sum)
            return sum_a * multiply

        return inner

    return wrapper


# @decorate_add
@paramterised_decorator(multiply=4)
def sum_a(a, b):
    return a + b


print(sum_a(4, 5))

print(sum_a(4, 5, 6, 7))
