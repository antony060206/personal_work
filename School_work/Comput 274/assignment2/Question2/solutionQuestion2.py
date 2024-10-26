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
                    groups.append(x)



            if x == ".":
                dots.append('.')
                if len(dots) == 2:
                    dots.clear()
                    # for n in range(2):
                    #     for item in groups[::-1]:
                    #         if item
                    # del groups[copy_groups.rfind(" ")+1:copy_groups.rfind(" ", copy_groups.find(" "))]



            location += 1
            first_slash = False
            #if len(groups) != 0 and grou
        print(slashes_loc)
        print(groups)


        current.append(groups)

























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
