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
        current = []
        path_length = 0

        for char in path:
            path_length += 1

            if char == '/':
                if len(current) != 0:
                    parts = ''.join(current)
                    if parts == "..":
                        if len(groups) != 0:
                            groups.pop()
                    elif parts != ".":
                        groups.append(parts)
                    current.clear()
            else:
                current.append(char)

        if len(current) != 0:
                parts = ''.join(current)
                if parts == "..":
                    groups.pop()
                elif parts != ".":
                    groups.append(parts)

    if path_length == len(path):
        return "/" + "/".join(groups)
    else:
        return "Invalid Path"
    
def main():
    # Takes Unix path as input
    path = input()

    # Simplify the path
    print(simplify_path(path))

if __name__ == "__main__":
    main()
