import random
def entry_check(first_input):
    flag = True
    a=""
    if first_input == "1":
        a="1"
    elif first_input == "2":
        a = "2"
    else:
        while flag:
            a=input("Input should be '1' or '2' : ")
            if a == "1":
                a = "1"
                break
            elif a == "2":
                a ="2"
                break

    return a
def string_in(m):
    flag=True

    for i in n:
        while flag:
            l=""
            if not m in n:
                l = input("Please write a number: ")
            if l in n:
                break
            if m in n:
                l = m
                break
        return l

flag1 = True
while flag1:
    a, b, c, d, e, f, g, h, j = (" ", " ", " ", " ", " ", " ", " ", " ", " ")
    n = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    x = f"----------------------------\n    {a}    |    {b}    |   {c}    \n----------------------------\n    {d}    |    {e}    |   {f}    \n----------------------------\n    {g}    |    {h}    |   {j}    \n----------------------------"

    game_type=input("Choose the game type:\n1-Multiplayer\n2-Single Player")
    y=entry_check(game_type)
    print(x)
    p=1
    liste=[]
    flag=True
    if y =="1":
        for i in range(9):

            if p%2==1:
                t = input("Enter the number of box that you want to sign 'X': ")
                t =string_in(t)
                while flag:
                    if t in liste:
                        t = input(f"Box {t} is signed please choose another box: ")
                        print(liste)
                        t = string_in(t)
                    if not t in liste:
                        break
                liste.append(t)
                if t=="1":
                    a="X"
                elif t=="2":
                    b="X"
                elif t=="3":
                    c="X"
                elif t=="4":
                    d="X"
                elif t=="5":
                    e="X"
                elif t=="6":
                    f="X"
                elif t=="7":
                    g="X"
                elif t=="8":
                    h="X"
                elif t=="9":
                    j="X"
                x = f"----------------------------\n    {a}    |    {b}    |   {c}    \n----------------------------\n    {d}    |    {e}    |   {f}    \n----------------------------\n    {g}    |    {h}    |   {j}    \n----------------------------"

                # if c == "X" and f == "X" and j == "X":
                if a == b == c =="X" :
                    print(x)
                    print("X WON!")
                    break
                if d == e == f=="X":
                    print(x)
                    print("X WON!")
                    break
                if g == h == j=="X":
                    print(x)
                    print("X WON!")
                    break
                if a == d == g =="X" :
                    print(x)
                    print("X WON!")
                    break
                if b == e == h=="X":
                    print(x)
                    print("X WON!")
                    break
                if c == f == j=="X":
                    print(x)
                    print("X WON!")
                    break
                if a == e == j =="X" :
                    print(x)
                    print("X WON!")
                    break
                if c == e == g=="X":
                    print(x)
                    print("X WON!")
                    break

            if p%2==0:
                t = input("Enter the number of box that you want to sign 'O': ")
                t = string_in(t)
                while flag:
                    if t in liste:
                        t = input(f"Box {t} is signed please choose another box: ")
                        print(liste)
                        t = string_in(t)
                    if not t in liste:
                        break
                liste.append(t)
                if t=="1":
                    a="O"
                elif t=="2":
                    b="O"
                elif t=="3":
                    c="O"
                elif t=="4":
                    d="O"
                elif t=="5":
                    e="O"
                elif t=="6":
                    f="O"
                elif t=="7":
                    g="O"
                elif t=="8":
                    h="O"
                elif t=="9":
                    j="O"
                x = f"----------------------------\n    {a}    |    {b}    |   {c}    \n----------------------------\n    {d}    |    {e}    |   {f}    \n----------------------------\n    {g}    |    {h}    |   {j}    \n----------------------------"
                if a == b == c =="O" :
                    print(x)
                    print("O WON!")
                    break
                if d == e == f=="O":
                    print(x)
                    print("O WON!")
                    break
                if g == h == j=="O":
                    print(x)
                    print("O WON!")
                    break
                if a == d == g =="O" :
                    print(x)
                    print("O WON!")
                    break
                if b == e == h=="O":
                    print(x)
                    print("O WON!")
                    break
                if c == f == j=="O":
                    print(x)
                    print("O WON!")
                    break
                if a == e == j =="O" :
                    print(x)
                    print("O WON!")
                    break
                if c == e == g=="O":
                    print(x)
                    print("O WON!")
                    break
            p += 1

            print(x)

        commandd = input("\n 1-Continue.. \n 2-End Game..\n")
        ff = entry_check(commandd)
        if ff == "2":
            flag1 = False

    if y =="2":
        v=["a","b","c","d","e","f","g","h","j"]
        for i in range(5):

            t = input("Enter the number of box that you want to sign: ")
            t =string_in(t)
            while flag:
                if t in liste:
                    t = input(f"Box {t} is signed please choose another box: ")
                    print(liste)
                    t = string_in(t)
                if not t in liste:
                    break
            liste.append(t)
            if t=="1":
                a="X"
                v.remove("a")
            elif t=="2":
                b="X"
                v.remove("b")
            elif t=="3":
                c="X"
                v.remove("c")
            elif t=="4":
                d="X"
                v.remove("d")
            elif t=="5":
                e="X"
                v.remove("e")
            elif t=="6":
                f="X"
                v.remove("f")
            elif t=="7":
                g="X"
                v.remove("g")
            elif t=="8":
                h="X"
                v.remove("h")
            elif t=="9":
                j="X"
                v.remove("j")

            s=random.choice(v)
            v.remove(s)
            exec("%s = %d" % (s, 0))
            x = f"----------------------------\n    {a}    |    {b}    |   {c}    \n----------------------------\n    {d}    |    {e}    |   {f}    \n----------------------------\n    {g}    |    {h}    |   {j}    \n----------------------------"

            # if c == "X" and f == "X" and j == "X":
            if a == b == c =="X" :
                print(x)
                print("YOU WON!")
                break
            if d == e == f=="X":
                print(x)
                print("YOU WON!")
                break
            if g == h == j=="X":
                print(x)
                print("YOU WON!")
                break
            if a == d == g =="X" :
                print(x)
                print("YOU WON!")
                break
            if b == e == h=="X":
                print(x)
                print("YOU WON!")
                break
            if c == f == j=="X":
                print(x)
                print("YOU WON!")
                break
            if a == e == j =="X" :
                print(x)
                print("YOU WON!")
                break
            if c == e == g=="X":
                print(x)
                print("YOU WON!")
                break
            if a == b == c ==0 :
                print(x)
                print("YOU LOST!")
                break
            if d == e == f==0:
                print(x)
                print("YOU LOST!")
                break
            if g == h == j==0:
                print(x)
                print("YOU LOST!")
                break
            if a == d == g ==0 :
                print(x)
                print("YOU LOST!")
                break
            if b == e == h==0:
                print(x)
                print("YOU LOST!")
                break
            if c == f == j==0:
                print(x)
                print("YOU LOST!")
                break
            if a == e == j ==0 :
                print(x)
                print("YOU LOST!")
                break
            if c == e == g==0:
                print(x)
                print("YOU LOST!")
                break
            print(x)
        commandd = input("\n 1-Continue.. \n 2-End Game..\n")
        ff = entry_check(commandd)
        if ff == "2":
            flag1 = False