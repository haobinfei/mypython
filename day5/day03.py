import random

ran = random.random()
print(ran)

ran = random.randint(0,10)
print(ran)

ran = random.randrange(1,10,3)
print(ran)

list1 = ["学强","菲菲","飞飞"]
ran = random.choice(list1)
print(ran)

random.shuffle(list1)
print(list1)