
def permutation(n):
    def generate(current, remainder):
        if len(current) == n:
            print(current)
            return

        for x in remainder:
            new_current = current + [x]
            new_remainder = [y for y in remainder if y != x]
            generate(new_current, new_remainder)

    generate([], list(range(1, n + 1)))

permutation(3)