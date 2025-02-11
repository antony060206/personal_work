# DO NOT MODIFY!
class TreeNode:
    """Represents a tree node
    """

    def __init__(self, value):
        self.__value = value
        self.__children = []

    def print_tree(self, recurse=False):
        if len(self.__children) == 0 and not recurse:
            print(str(self.__value))
        else:
            if len(self.__children) != 0:
                children_values = [c.get_value() for c in self.__children]
                print(f"{str(self.__value)} -> {' '.join(children_values)}")
                for c in self.__children:
                    c.print_tree(True)

    def get_value(self):
        return self.__value

    def get_children(self):
        return self.__children

    def add_child(self, child):
        self.__children.append(child)
