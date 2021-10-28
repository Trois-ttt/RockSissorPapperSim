import random
win = 0
lose = 0
draw = 0
winstr = 0
losestr = 0
hiwin = 0
hilos = 0
def winning():
    print("승리했습니다")
    global win
    global winstr
    global losestr
    win += 1
    winstr += 1
    losestr = 0
def losing():
    print("패배했습니다")
    global lose
    global losestr
    global winstr
    lose += 1
    losestr += 1
    winstr = 0
def RCP(i):
    global win
    global lose
    global draw
    global winstr
    global losestr
    AIt = ["가위", "바위", "보"]
    player = i
    random.shuffle(AIt)
    AI = AIt[0]
    if player not in AIt:
        print("잘못된 입력입니다")
    print(player, "vs", AI)
    if player == AI:
        print("무승부입니다")
        winstr = 0
        losestr = 0
        draw += 1
    elif player == "가위":
        if AI == "보":
            winning()
        else:
            losing()
    elif player == "바위":
        if AI == "가위":
            winning()
        else:
            losing()
    elif player == "보":
        if AI == "바위":
            winning()
        else:
            losing()
    print("승", win)
    print("패", lose)
    print("무", draw)
    if winstr != 0:
        print("{}연승중입니다".format(winstr))
    if losestr != 0:
        print("{}연패중입니다".format(losestr))

play = 0
while True:
    playert = ["가위", "바위", "보"]
    random.shuffle(playert)
    print(playert[0])
    RCP(playert[0])
    play += 1
    if winstr > hiwin:
        hiwin = winstr
    if losestr > hilos:
        hilos = losestr
    if hilos >= 7 and hiwin >= 7:
        break
print("\n최고기록\n{}연패\n{}연승".format(hilos, hiwin))
print("\n{}회 시행했습니다".format(play))