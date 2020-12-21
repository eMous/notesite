import functools

from django.test import TestCase


class PythonTestCase(TestCase):
    def setUp(self):
        pass

    def test_iterator(self):
        class It:
            times = 0

            def __iter__(self):
                return self

            def __next__(self):
                self.times += 1
                if self.times == 2:
                    raise StopIteration("The iterator can only be iterated once.")
                return self.times

        # use iter() and next(), need to explicitly handle the exception
        it_obj = It()
        it = iter(it_obj)
        val = next(it)
        self.assertEqual(val, 1)
        ret = None
        try:
            ret = next(it)
        except StopIteration as err:
            pass
        self.assertIsNone(ret)

        # use for loop, automatically handle the exception
        it_obj = It()
        container = []
        for x in it_obj:
            container.append(x)
        self.assertEqual(len(container), 1)

        self.assertEqual(1, 1)

    def test_generator(self):

        # use a regular generator
        def generator_loop_once():
            yield 1

        def generator_loop_infinite():
            x = 1
            while True:
                yield x
                x += 1

        generator_once = generator_loop_once()
        val_once = next(generator_once)
        self.assertEqual(val_once, 1)
        generator_once_get_again = False
        try:
            val_once = next(generator_once)
            generator_once_get_again = True
        except StopIteration as err:
            pass
        self.assertFalse(generator_once_get_again)

        generator_once = generator_loop_once()
        container = []
        for x in generator_once:
            container.append(x)
        self.assertEqual(len(container), 1)

        generator_infinity = generator_loop_infinite()
        val_inf = next(generator_infinity)
        self.assertEqual(val_inf, 1)
        val_inf = next(generator_infinity)
        self.assertEqual(val_inf, 2)
        container = []
        for x in generator_infinity:
            if x == 5:
                break
            container.append(x)
        self.assertEqual(container[0], 3)
        self.assertEqual(container[1], 4)

        # use generator expression
        expression1 = (x for x in range(5))
        expression2 = (x for x in generator_infinity)
        self.assertIsInstance(expression1, generator_infinity.__class__)
        self.assertEqual(next(expression1), 0)
        self.assertIsInstance(expression2, generator_infinity.__class__)
        self.assertEqual(next(expression2), 6)

        self.assertEqual(1, 1)

    def test_decorator(self):
        def job():
            print("my job is swiping the floor. I am doing it.")
            return "Success"

        ret = job()
        self.assertEqual(ret, "Success")

        def decorator(function):
            def wrapper(*args, **kw):
                print("Before doing my job.")
                ret = function(*args, **kw)
                print("After doing my job.")
                return ret

            return wrapper

        self.assertTrue(callable(decorator(job)))
        self.assertEqual(decorator(job)(), "Success")

        @decorator
        def job():
            print("my job is swiping the floor. I am doing it.")
            return "Success"

        ret = job()
        self.assertEqual(ret, "Success")

        def high_level_decorator(who):
            def decorator(function):
                # @functools.wraps(function)
                def wrapper(*args, **kw):
                    print(f'Before doing {who}\'s job.')
                    ret = function(*args, **kw)
                    print(f'After doing {who}\'s job.')
                    return ret

                return wrapper

            return decorator

        @high_level_decorator("Tom")
        def job():
            print("my job is swiping the floor. I am doing it.")
            return "Success"

        ret = job()
        self.assertEqual(ret, "Success")
        self.assertEqual(job.__name__, "wrapper")
        self.assertEqual(1, 1)
