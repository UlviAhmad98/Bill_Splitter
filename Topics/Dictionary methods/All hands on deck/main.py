rank = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
input_1 = input()
input_2 = input()
input_3 = input()
input_4 = input()
input_5 = input()
input_6 = input()
input_list = [input_1, input_2, input_3, input_4, input_5, input_6]

total = 0

for x in input_list:
    if x in rank:
        total += rank[x]
    else:
        total += int(x)

print(total / 6)
