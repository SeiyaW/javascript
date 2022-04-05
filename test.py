import random

def judge(x, y):
    score = (x - y + 3) % 3
    if score == 0:
        j = "引き分けです"
    elif score == 1:
        j = "あなたの負けです"
    else:
        j = "あなたの勝ちです"
    print(j)

hand = ["グー","チョキ","パー"]

x = input("手を選んでください\n0:グー,1:チョキ,2:パー\n\n")

x = int(x)

y = random.randint(0,2)

print("\nあなたの手:{}".format(hand[x]))
print("コンピュータの手:{}\n".format(hand[y]))

judge(x,y)