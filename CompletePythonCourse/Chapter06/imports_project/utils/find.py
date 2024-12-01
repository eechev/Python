# from .commons.file_operations import save_to_file # relative import which is not a good idea


def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
            return i
    raise NotFoundErr(f"{expected} not found in provided iterable.")



class NotFoundErr(Exception):
    pass


if __name__ == "__main__":
    print(__name__)
    print(find_in(['Rolf', 'Jose', 'Jen'], lambda x: x, 'Jose'))