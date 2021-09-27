'''
Реализовать декоратор, который будет приводить все аргументы функции к определенному типу данных.

@validation(<type of data (int, float, str, typle, list)>)

после чего будет передавать эти значения в функцию.
'''


def validation(iters):
    def actual_decorator(function_to_decorate):
        def wrapper(*args):
            print('Выполняем обёрнутую функцию...')
            a=[]
            print(iters)
            if iters=='str':
                for i in args:
                    a.append(str(i))
            elif iters=='int':
                for i in args:
                    a.append(int(i))
            elif iters=='list':
                for i in args:
                    b=[]
                    b.append(i)
                    a.append(b)

            elif iters=='tuple':
                for i in args:
                    a.append(i)
                
                a=tuple(a)

            elif iters=='float':
                for i in args:
                    a.append(float(i))

                    
            function_to_decorate(a)
            print('Выходим из обёртки')
        return wrapper
    return actual_decorator

@validation(iters='tuple')
def test_fun(*args):
    print(args[0])

test_fun(20,30,2)

