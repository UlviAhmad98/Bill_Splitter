# the list with words from string
# please, do not modify it
some_iterable = input().split()

# use dictionary comprehension to create a new dictionary
some_dict = {some.upper(): some.lower() for some in some_iterable}
print(some_dict)
