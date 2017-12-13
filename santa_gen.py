"""Santa Clause IS real."""
from random import randint


class Node(object):
    """Will represent a child."""

    def __init__(self, address, has_mean_dog, provides_cookies, naughty):
        """Creates an instance of a Node class object."""
        self.nice = True
        self.address = address
        self.present_wish = 'Pony'
        self.provides_cookies = None
        self.has_mean_dog = None
        self.naughty = None
        if has_mean_dog == 1:
            self.has_mean_dog = True
        else:
            self.has_mean_dog = False
        if provides_cookies == 1:
            self.provides_cookies = True
        else:
            self.provides_cookies = False
        if naughty == 1:
            self.naughty = True
            self.nice = False
        else:
            self.naughty = False


def build_children_iterable():
    """Function that serves to build a randomize list of children, from which
    Santa will judge harshly."""
    return [Node(randint(0, 1000), randint(0, 1), randint(0, 1), randint(0, 1)) for x in range(101)]


class SantaClause(object):
    """Will represent the big red man himself."""

    def __init__(self, children=None):
        self.children = children
        self.nice_list = []
        self.naughty_list = []
        if children:
            for child in children:
                if child.nice:
                    self.nice_list.append(child)
                if child.naughty:
                    self.naughty_list.append(child)

    def deliver_presents(self):
        """The day has come."""
        children_homes = [[]] * 1000
        for good_child in self.nice_list:
            if good_child.provides_cookies and not good_child.has_mean_dog:
                children_homes[good_child.address].append(good_child.present_wish)
            else:
                children_homes[good_child.address].append('Slinky')
        for bad_child in self.nice_list:
            if bad_child.provides_cookies and not bad_child.has_mean_dog:
                children_homes[bad_child.address].append('Lead-based Paint')
            else:
                children_homes[bad_child.address].append('Coal')
