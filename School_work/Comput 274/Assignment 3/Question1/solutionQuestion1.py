# Name: Antony Feng
# ccid: zfeng8
# studentId: 1802829
# operating system: windows 11
# python version: 3.12
from treenode import TreeNode


def read_tree():
    """Construct a tree from standard input

    The first line of standard input will have the format: n d
        - n: The length of the array-based representation of the tree
        - d: The maximum number of children a node can have

    The second line contains n space-separated strings where each string
    represents the value of a TreeNode. A string can be a single character
    (eg. 'W') or a series of characters (eg. 'AA', 'AB'). The dash '-' character
    represents an empty node and should be ignored.

    Returns:
        The root of the tree as a TreeNode object
    """

    numlist = input().split(" ")
    children = (input().split(" "))
    parent_tree = []
    count = 1


    for i in range(0,int(numlist[0])): #start from the root of the tree

        if count <= int(numlist[0]):
            node = TreeNode(children[i])
            parent_tree.append(node)


            for x in range(count,int(numlist[1])+count):
                # print(x, count,int(numlist[1])+count, i, len(parent_tree), count)
                if(x <= int(numlist[0])-1):
                    if (children[x] != "-" and parent_tree[i].get_children() != "-"):
                        child_node = TreeNode(children[x])
                        parent_tree[i].add_child(child_node)
                        # print(parent_tree[i].get_value(), children[x], i, count)
            count += int(numlist[1])

    root = parent_tree[0]
    for y in range(len(parent_tree)-1, -1, -1):
        for parent in range(y-1, -1, -1):
            len_root = 0
            for child in parent_tree[parent].get_children():
                len_root += 1

            for child_len in range(len_root):
                if (parent_tree[parent].get_children()[child_len].get_value().strip() == parent_tree[y].get_value().strip()):
                    parent_tree[parent].get_children()[child_len] = parent_tree[y]

    return root



def main():
    # Do not modify
    read_tree().print_tree()


if __name__ == "__main__":
    main()
