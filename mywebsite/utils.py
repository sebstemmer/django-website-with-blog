from itertools import zip_longest


def grouper(n, iterable, padvalue=None):
    return list(zip_longest(*[iter(iterable)]*n, fillvalue=padvalue))


def is_iterable(some_object):
    try:
        some_object_iterator = iter(some_object)
        print('is iterable')
    except TypeError as te:
        print(some_object, 'is not iterable')
