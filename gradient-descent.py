import inspect

# # function for tests
# def test_func(x, y):
#     return (1-x)**2 + 0.1*y - 4*x*y


# # gradient of the above test fucntion
# test_func_grad = (lambda x, y: (-2*(1-x) - 4 * y), lambda x, y: 0.1 - 4 * x)

# function for tests
def test_func(x, y):
    return (1-x)**2 + 100*(y - x**2)**2


# gradient of the above test fucntion
test_func_grad = (lambda x, y: (-2*(1-x) - 400*(y-x**2)),
                  lambda x, y: 200*(y-x**2))


def gradient_descent(func, x0=None, func_grad=None):
    """Ruturns the minimum of the given function

    Parameters:
    func: Function whose minimum needs to be found
    x0 : Initial point -  tuple

    Returns:
    number: the minimum of the function

   """

   # Fist of all get the parameters name of the function
    params = inspect.getfullargspec(func)[0]
    if x0 == None:
        a = [0 for p in params]
    else:
        a = list(x0)

    # step
    s = 0.001
    n = len(a)
    a_1 = a.copy()
    n_iter = 10000
    precision = 0.01
    for k in range(n_iter):

        for i in range(n):
            # calculate the gradient at a
            grad = [0]*n
            for j in range(n):
                grad[j] = func_grad[j](*tuple(a))

            a[i] = a[i] - s*grad[i]
        # print('value : ', func(*tuple(a)), ' for a = ', a)
        if func(*tuple(a)) - func(*tuple(a_1)) > 0:
            print('function increases.')
            return func(*tuple(a_1))

        # if func(*tuple(a_1)) - func(*tuple(a)) < precision:
        #     print('func(*tuple(a_1)) = ', func(*tuple(a_1)))
        #     print('func(*tuple(a)) = ', func(*tuple(a)))
        #     break

        a_1 = a.copy()
    print('a = ', a)
    return func(*tuple(a))


x = gradient_descent(test_func, (0.1, 0.1), test_func_grad)
print(x)
