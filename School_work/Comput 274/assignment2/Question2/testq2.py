def simplify_path(path):
    if not path.startswith('/'):
        return "Invalid Path"

    groups = []
    current = []

    for char in path:
        if char == '/':
            if current:  # If there is a current segment being built
                segment = ''.join(current)
                if segment == "..":
                    if groups:  # Move to parent directory if possible
                        groups.pop()
                elif segment and segment != ".":
                    groups.append(segment)  # Only add non-empty, non-dot segments
                current.clear()  # Reset current for the next segment
        else:
            current.append(char)  # Build the current segment

    # Handle any remaining characters in current
    if current:
        segment = ''.join(current)
        if segment == "..":
            if groups:
                groups.pop()
        elif segment and segment != ".":
            groups.append(segment)

    # Join the groups into a final path
    simplified_path = "/" + "/".join(groups)
    return simplified_path if groups else "/"

def main():
    # Takes Unix path as input
    path = input()

    # Simplify the path
    print(simplify_path(path))

if __name__ == "__main__":
    main()