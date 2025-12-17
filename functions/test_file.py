def add_numbers(a, b):
    return a + b


def test_file(config, **inp_obj):
    number1 = inp_obj.get("num1", 20)
    number2 = inp_obj.get("num2", 30)

    retrun add_numbers(number1, number2)