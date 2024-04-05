import hashlib


def decorator_function(function_to_modify, arg1, arg2):
    arg1 = arg1
    arg2 = arg2
    result = function_to_modify(arg1, arg2)
    result += 1

    return result


def function_to_modify(arg1, arg2):
    sum = arg1 + arg2

    return sum

result1 = function_to_modify(53, 734)
result2 = decorator_function(function_to_modify, 53, 734)


def proxy_function(function_to_proxy, arg1, arg2):
    arg1 = arg1
    arg2 = arg2
    result = function_to_proxy(arg1, arg2)
    result_b = bytearray(result)
    result_md5 = hashlib.md5(result_b, usedforsecurity=True)

    return result_md5

def function_to_proxy(arg1, arg2):
    sum = arg1 + arg2

    return sum

result1 = function_to_proxy(15, 62)
result2 = proxy_function(function_to_proxy, 15, 62)
