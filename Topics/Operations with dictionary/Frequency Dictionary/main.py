# put your python code here
sentence = input()
word = sentence.split()

count_dict = {x: sentence.count(x) for x in word}
