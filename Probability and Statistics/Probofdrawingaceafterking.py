def acecard():
    #Total number of Ace card inside a dock 4
    s=0
    tries=0
    for prob in range(1,52):
        if prob < 5:
            s+=1
        tries +=1
    print("Number of Tries Remaining: ",tries)
    print("Number of Ace: ",s)
    print('Probabity of getting ace after Drwaing King 51 tries\n')
    print("Answer = ",float(s)/tries)
acecard()