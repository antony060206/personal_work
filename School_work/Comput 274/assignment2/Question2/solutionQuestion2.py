# Name: Antony Feng
# ccid: zfeng8
# studentId: 1802829
# operating system: windows 10
# python version: 3.12

def simplify_path(path):

    if not path.startswith('/') and len(path) >= 1 and len(path) <= 100:
        return "Invalid Path"

    else:
        groups = []
        dots = []
        slashes_loc = []

        remove_loc = []

        location = 0
        first_slash = False
        for x in path:

            if x != ".": # for if x does not equal to dots
                if x == "/":
                    first_slash = True
                    if first_slash and len(groups) != 0 and groups[-1] == " ":
                        groups.pop()

                    groups.append(" ")
                    slashes_loc.append(location)
                else:
                    print(x)
                    groups.append(x)



            if x == ".":
                dots.append('.')
                if len(dots) == 2:
                    dots.clear()
                    for item_index in range(len(groups)-1,0 , -1):
                        if(len(remove_loc) < 2):
                            if (groups[item_index] == " "):
                                remove_loc.append(item_index)
                    del groups[remove_loc[1]:remove_loc[0]]
                    remove_loc.clear()


            location += 1
            first_slash = False
            print(groups)
        final_string = ''.join(groups)
        final_string = final_string.replace(" ", "/")
        return final_string



    #
    #     for char in path:
    #         path_length += 1
    #
    #         if char == '/':
    #             if len(current) != 0:
    #                 parts = ''.join(current)
    #                 if parts == "..":
    #                     if len(groups) != 0:
    #                         groups.pop()
    #                 elif parts != ".":
    #                     groups.append(parts)
    #                 current.clear()
    #         else:
    #             current.append(char)
    #
    #     if len(current) != 0:
    #             parts = ''.join(current)
    #             if parts == "..":
    #                 groups.pop()
    #             elif parts != ".":
    #                 groups.append(parts)
    #
    # if path_length == len(path):
    #     return "/" + "/".join(groups)
    # else:
    #     return "Invalid Path"
    
def main():
    # Takes Unix path as input
    path = input()

    # Simplify the path
    print(simplify_path(path))

if __name__ == "__main__":
    main()
