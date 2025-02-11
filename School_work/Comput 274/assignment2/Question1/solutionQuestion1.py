# Name: Antony Feng
# ccid: zfeng8
# studentId: 1802829
# operating system: windows 10
# python version: 3.12

def fractal_eval(expr):
    expr_string = str(expr)

    sqrleft = expr_string.rfind("[")
    sqrright = expr_string.find("]")


    expr_string = expr_string[:sqrleft] + " " + expr_string[sqrleft+1:]
    expr_string = expr_string.replace(expr_string[sqrright], " ", 1)

    calculate_str = str((eval(expr_string[sqrleft + 1:sqrright]))**2)
    expr_string_left = expr_string[:sqrleft]
    expr_string_right = expr_string[sqrright:]
    expr_string = expr_string_left + calculate_str + expr_string_right


    if expr_string.count("[") >= 1 :
        return fractal_eval(expr_string)
    else:
        return eval(expr_string)

def main():

    exp = input()
    print(round(fractal_eval(exp)))

if __name__ == "__main__":
    main()
