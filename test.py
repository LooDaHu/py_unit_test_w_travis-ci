def set_up():
    print("Start test")


def tear_down():
    print("function teardown")


def test1():
    rt = function1()
    assert rt == 200


def test2():
    rt = function2()
    assert rt == 200


def function1():
    return 1 + 199


def function2():
    return 198 + 2
