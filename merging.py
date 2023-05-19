# Merging sorted arrays.
def merge_arrays(a, b):
    # "c" will contain the result of merging arrays "a" and "b"
    c = []
    # CHECK that "a" or "b" are not empty
    while a or b:
        # CHECK that "b" is empty, or that "a" and "b" are not empty and compare the elements
        if not b or ((a and b) and a[0] <= b[0]):
            # removing the first element from "a" and adding it to "c"
            c.append(a[0])
            a.pop(0)
        else:
            # removing the first element from "b" and adding it to "c"
            c.append(b[0])
            b.pop(0)
    return c


# Examples
list_1 = [1, 2, 3]
list_2 = [2, 3, 4, 4]
print(merge_arrays(list_1, list_2))
