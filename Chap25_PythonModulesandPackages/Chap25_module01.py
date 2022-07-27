# A module can contain
# • Functions
# • Classes
# • Variables
# • Executable code
# • Attributes associated with the module such as its name.

"""This is a test module"""
print("This is module01")


def printer(some_object):
    print('printer')
    print(some_object)
    print('done')


class Shape:
    def __init__(self, id):
        self._id = id

    def __str__(self):
        return 'Shape - ' + self._id

    @property
    def id(self):
        """ The docstring for the id property """
        print('In id method')
        return self._id

    @id.setter
    def id(self, value):
        print('In set_age method')
        self._id = id


default_shape = Shape('square')
