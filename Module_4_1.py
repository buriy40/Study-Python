def Test_function():
    def inner_function():
        print('Я в зоне видимости функции Test_function')
    inner_function()
Test_function()