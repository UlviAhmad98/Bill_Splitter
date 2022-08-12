# finish the function
def find_the_parent(child):

    for parent in (Drinks, Pastry, Sweets):
        if issubclass(child, parent) is True:
            print(parent.__name__)
