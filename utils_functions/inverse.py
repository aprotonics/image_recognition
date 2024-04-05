def inverse(*args):
    result = None

    match type(args):
        case "":
            result = inv_constant(args)
        case "":
            result = inv_variable(args)
        case "":
            result = inv_constant_variable_multiplication(args)

    return result


def inv_constant(constant):
    constant = constant

    return -constant

def inv_variable(variable):
    variable = variable

    return 1 / variable

def inv_constant_variable_multiplication(constant, variable):
    constant = constant
    variable = variable

    return


