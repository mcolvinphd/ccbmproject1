ngames=100000
won=0
from random import shuffle
for i in range(ngames):
    #create and sort deck
    deck=list(range(52))
    shuffle(deck)
    ncards=len(deck)
    cur=0  #Set location of top card
    while ncards-cur>=4:  #Play while you hold 4 or more cards
        if (deck[cur]//13)==(deck[cur+3]//13):  #Check if the suits match
            del(deck[cur+1:cur+3]) #Remove middle two cards
            ncards=ncards-2 #Reduce the count of the number cards left
            cur=max(0,cur-2)  #Set the pointer two cards earlier (testing if there are < 2 cards left)
        elif (deck[cur]%13)==(deck[cur+3]%13): #Check if the faces match
            del(deck[cur:cur+4])  #Remove all 4 cards
            ncards=ncards-4
            cur=max(0,cur-4)
        else:
            cur=cur+1  #If no match go to next card
    if ncards==0:
        won=won+1
print(won/ngames)