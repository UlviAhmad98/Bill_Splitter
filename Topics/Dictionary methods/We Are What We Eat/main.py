# the list "meals" is already defined
# your code here

calories = 0
for x in range(len(meals)):
    calories += meals[x]["kcal"]

print(calories)
