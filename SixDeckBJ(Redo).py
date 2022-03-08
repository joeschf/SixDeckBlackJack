import random
import sys
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
  
class Card:
    
    def __init__(self,val,suit):
        self.val = val
        self.suit = suit
    
    def display(self):
        if (self.val < 1):
            print("A", self.suit)
        elif (self.val == 11):
            print("J", self.suit)
        elif (self.val == 12):
            print("Q", self.suit) 
        elif (self.val == 13):
            print("K", self.suit) 
        else:
            print(self.val, self.suit)
    
class Dealer:
    
    def __init__(self):
        self.hand = []
   
        
    def draw(self,deck):
        card = deck.draw()
        self.hand.append(card)   
        
    def display(self):
        for c in self.hand:
            if (c.val == 1):
                print("A", c.suit)
            elif (c.val == 11):
                print("J", c.suit)
            elif (c.val == 12):
                print("Q", c.suit) 
            elif (c.val == 13):
                print("K", c.suit) 
            else:
                print(c.val, c.suit)
                
    def aceCheck(self):
        for c in self.hand:
            if (c.val == 1):
                return True
        return False
    
    
    def getSuit(self):
        c = self.hand[len(self.hand)-1]
        return c.suit
    
    def getVal(self):
        c = self.hand[len(self.hand)-1]
        return c.val
        
    def reset(self):
        self.hand = []
    
    def flipCard(self):
        print("\nDealer flips over! ...")
                                         
                               
                                         
        c = self.hand[0]
        if (c.val == 1):
            print("A", c.suit)
        elif (c.val == 11):
            print("J", c.suit)
        elif (c.val == 12):
            print("Q", c.suit) 
        elif (c.val == 13):
            print("K", c.suit) 
        else:
            print(c.val, c.suit)
        
        print("\nThe Dealers Cards are: ")
        for c in self.hand:
            if (c.val == 1):
                print("A", c.suit)
            elif (c.val == 11):
                print("J", c.suit)
            elif (c.val == 12):
                print("Q", c.suit) 
            elif (c.val == 13):
                print("K", c.suit) 
            else:
                print(c.val, c.suit)
                
    def turnCard(self):
        for c in self.hand:
            if (c.val == 1):
                print("A", c.suit)
            elif (c.val == 11):
                print("J", c.suit)
            elif (c.val == 12):
                print("Q", c.suit) 
            elif (c.val == 13):
                print("K", c.suit) 
            else:
                print(c.val, c.suit)
             
    def score(self):
        aceHand = False
        sum = 0
        count = 0
        for c in self.hand:
            if (c.val ==1):
                aceCard = self.hand.pop(count)
                aceHand = True 
            count+=1
        if(aceHand == False):
            for c in self.hand: 
                if(c.val == 1):
                    sum += 11
                elif(c.val >= 10):
                    sum += 10
                else:
                    sum += c.val
        else:
            self.hand.append(aceCard)
            for c in self.hand: 
             if(c.val == 1):
                 if(sum < 11):
                     sum += 11
                 else:
                     sum+=1                                     
             elif(c.val >= 10):
                 sum += 10
             else:
                 sum += c.val
        return sum     
        
    def checkBlackJack(self):
        sum = 0
        for c in self.hand: 
            if(c.val == 1):
                sum += 11
            elif(c.val >= 10):
                sum += 10
            else:
                sum += c.val
        if (sum == 21):
            return True 
        
    def getFile(self,k):
       
       if(self.hand[k].val == 1):
           if(self.hand[k].suit == 'Clubs'):
               s = "clubs_ace.png"
           elif(self.hand[k].suit == 'Spades'):
               s = "spades_ace.png"
           elif(self.hand[k].suit == 'Hearts'):
               s = "hearts_ace.png"
           else:
               s = "diamonds_ace.png"
       
       elif(self.hand[k].val == 2):
           if(self.hand[k].suit == 'Clubs'):
               s = "clubs_2.png"
           elif(self.hand[k].suit == 'Spades'):
               s = "spades_2.png"
           elif(self.hand[k].suit == 'Hearts'):
               s = "hearts_2.png"
           else:
               s = "diamonds_2.png"
       
       elif(self.hand[k].val == 3):
           if(self.hand[k].suit == 'Clubs'):
               s = "clubs_3.png"
           elif(self.hand[k].suit == 'Spades'):
               s = "spades_3.png"
           elif(self.hand[k].suit == 'Hearts'):
               s = "hearts_3.png"
           else:
               s = "diamonds_3.png"
       
       elif(self.hand[k].val == 4):
           if(self.hand[k].suit == 'Clubs'):
               s = "clubs_4.png"
           elif(self.hand[k].suit == 'Spades'):
               s = "spades_4.png"
           elif(self.hand[k].suit == 'Hearts'):
               s = "hearts_4.png"
           else:
               s = "diamonds_4.png"
               
       elif(self.hand[k].val == 5):
           if(self.hand[k].suit == 'Clubs'):
               s = "clubs_5.png"
           elif(self.hand[k].suit == 'Spades'):
               s = "spades_5.png"
           elif(self.hand[k].suit == 'Hearts'):
               s = "hearts_5.png"
           else:
               s = "diamonds_5.png"
               
       elif(self.hand[k].val == 6):
           if(self.hand[k].suit == 'Clubs'):
               s = "clubs_6.png"
           elif(self.hand[k].suit == 'Spades'):
               s = "spades_6.png"
           elif(self.hand[k].suit == 'Hearts'):
               s = "hearts_6.png"
           else:
               s = "diamonds_6.png"
               
       elif(self.hand[k].val == 7):
           if(self.hand[k].suit == 'Clubs'):
               s = "clubs_7.png"
           elif(self.hand[k].suit == 'Spades'):
               s = "spades_7.png"
           elif(self.hand[k].suit == 'Hearts'):
               s = "hearts_7.png"
           else:
               s = "diamonds_7.png"
               
       elif(self.hand[k].val == 8):
           if(self.hand[k].suit == 'Clubs'):
               s = "clubs_8.png"
           elif(self.hand[k].suit == 'Spades'):
               s = "spades_8.png"
           elif(self.hand[k].suit == 'Hearts'):
               s = "hearts_8.png"
           else:
               s = "diamonds_8.png"
               
       elif(self.hand[k].val == 9):
           if(self.hand[k].suit == 'Clubs'):
               s = "clubs_9.png"
           elif(self.hand[k].suit == 'Spades'):
               s = "spades_9.png"
           elif(self.hand[k].suit == 'Hearts'):
               s = "hearts_9.png"
           else:
               s = "diamonds_9.png"
               
       elif(self.hand[k].val == 10):
           if(self.hand[k].suit == 'Clubs'):
               s = "clubs_10.png"
           elif(self.hand[k].suit == 'Spades'):
               s = "spades_10.png"
           elif(self.hand[k].suit == 'Hearts'):
               s = "hearts_10.png"
           else:
               s = "diamonds_10.png"  
               
       elif(self.hand[k].val == 11):
           if(self.hand[k].suit == 'Clubs'):
               s = "clubs_jack.png"
           elif(self.hand[k].suit == 'Spades'):
               s = "spades_jack.png"
           elif(self.hand[k].suit == 'Hearts'):
               s = "hearts_jack.png"
           else:
               s = "diamonds_jack.png"   
               
       elif(self.hand[k].val == 12):
           if(self.hand[k].suit == 'Clubs'):
               s = "clubs_queen.png"
           elif(self.hand[k].suit == 'Spades'):
               s = "spades_queen.png"
           elif(self.hand[k].suit == 'Hearts'):
               s = "hearts_queen.png"
           else:
               s = "diamonds_queen.png"                
       else:           
           if(self.hand[k].suit == 'Clubs'):
               s = "clubs_king.png"
           elif(self.hand[k].suit == 'Spades'):
               s = "spades_king.png"
           elif(self.hand[k].suit == 'Hearts'):
               s = "hearts_king.png"
           else:
               s = "diamonds_king.png"   
       return s   

class Player1:
    
    def __init__(self):
        self.hand = []
        self.splitHand1 = []
        self.splitHand2 = []
        self.chips = 0
        sum = 0 
   
    def loseChips(self,v):
        self.chips -= v
    def addChips(self,v):
        self.chips += v 
    def chipSet(self,v):
        self.chips = v
    
    def splitCheck(self):
        if(self.hand[0].val == self.hand[1].val):
            return True
        elif(self.hand[0].val >= 10 and self.hand[1].val > 10):
            return True        
        return False
    
    def chipCount(self):
        return self.chips
    
    def splitHand(self):
        self.splitHand1.append(self.hand.pop(0))
        self.splitHand2.append(self.hand.pop(0))
        
    def getNumVal(self):
        c = self.hand[len(self.hand)-1]
        if(c.val == 10):
            return c.val
        elif(c.val == 1):
            return 11
        else: 
            return c.val

    def draw(self,deck):
        card = deck.draw()
        self.hand.append(card)
        
    def toHand1(self):
        self.splitHand1.append(self.hand.pop(0))
        
    def toHand2(self):
        self.splitHand2.append(self.hand.pop(0))
        
    def getSuit(self):
        c = self.hand[len(self.hand)-1]
        return c.suit
    
    def getVal(self):
        c = self.hand[len(self.hand)-1]
        return c.val

    def reset(self):
        self.hand = []
        self.splitHand1 = []
        self.splitHand2 = []
        
    def peekNextSuit(self,deck):
        suit = deck.peekNextSuit()
        return suit
    
    def peekNextVal(self,deck):
        val = deck.peekNextVal()
        return val
        
    def display(self):
        for c in self.splitHand1:
            if (c.val == 1):
                print("A", c.suit)
            elif (c.val == 11):
                print("J", c.suit)
            elif (c.val == 12):
                print("Q", c.suit) 
            elif (c.val == 13):
                print("K", c.suit) 
            else:
                print(c.val, c.suit)
                
    def getHandString(self):
        s = ""
        for c in self.hand:
            if (c.val == 1):
                s += "A "
                s += c.suit + " "
            elif (c.val == 11):
                s += "J "
                s += c.suit + " "
            elif (c.val == 12):
                s += "Q "
                s += c.suit
            elif (c.val == 13):
                s += "K "
                s += c.suit + " "
            else:
                s += str(c.val) + " " + c.suit + " "
                
        return s
                
    def score(self):
        aceHand = False
        sum = 0
        count = 0
        for c in self.hand:
            if (c.val ==1):
                aceCard = self.hand.pop(count)
                aceHand = True 
            count+=1
        if(aceHand == False):
            for c in self.hand: 
                if(c.val == 1):
                    sum += 11
                elif(c.val >= 10):
                    sum += 10
                else:
                    sum += c.val
        else:
            self.hand.append(aceCard)
            for c in self.hand: 
             if(c.val == 1):
                 if(sum < 11):
                     sum += 11
                 else:
                     sum+=1                                     
             elif(c.val >= 10):
                 sum += 10
             else:
                 sum += c.val
             
        return sum
    

    

    def scoreHand1(self):
        aceHand = False
        sum = 0
        count = 0
        for c in self.splitHand1:
            if (c.val ==1):
                aceCard = self.splitHand1.pop(count)
                aceHand = True 
            count+=1
        if(aceHand == False):
            for c in self.splitHand1: 
                if(c.val == 1):
                    sum += 11
                elif(c.val >= 10):
                    sum += 10
                else:
                    sum += c.val
        else:
            self.splitHand1.append(aceCard)
            for c in self.splitHand1: 
             if(c.val == 1):
                 if(sum < 11):
                     sum += 11
                 else:
                     sum+=1                                     
             elif(c.val >= 10):
                 sum += 10
             else:
                 sum += c.val
             
        return sum
    
    def scoreHand2(self):
        aceHand = False
        sum = 0
        count = 0
        for c in self.splitHand2:
            if (c.val ==1):
                aceCard = self.splitHand2.pop(count)
                aceHand = True 
            count+=1
        if(aceHand == False):
            for c in self.splitHand2: 
                if(c.val == 1):
                    sum += 11
                elif(c.val >= 10):
                    sum += 10
                else:
                    sum += c.val
        else:
            self.splitHand2.append(aceCard)
            for c in self.splitHand2: 
             if(c.val == 1):
                 if(sum < 11):
                     sum += 11
                 else:
                     sum+=1                                     
             elif(c.val >= 10):
                 sum += 10
             else:
                 sum += c.val
             
        return sum
    
    def getFile(self,k):
        
        if(self.hand[k].val == 1):
            if(self.hand[k].suit == 'Clubs'):
                s = "clubs_ace.png"
            elif(self.hand[k].suit == 'Spades'):
                s = "spades_ace.png"
            elif(self.hand[k].suit == 'Hearts'):
                s = "hearts_ace.png"
            else:
                s = "diamonds_ace.png"
        
        elif(self.hand[k].val == 2):
            if(self.hand[k].suit == 'Clubs'):
                s = "clubs_2.png"
            elif(self.hand[k].suit == 'Spades'):
                s = "spades_2.png"
            elif(self.hand[k].suit == 'Hearts'):
                s = "hearts_2.png"
            else:
                s = "diamonds_2.png"
        
        elif(self.hand[k].val == 3):
            if(self.hand[k].suit == 'Clubs'):
                s = "clubs_3.png"
            elif(self.hand[k].suit == 'Spades'):
                s = "spades_3.png"
            elif(self.hand[k].suit == 'Hearts'):
                s = "hearts_3.png"
            else:
                s = "diamonds_3.png"
        
        elif(self.hand[k].val == 4):
            if(self.hand[k].suit == 'Clubs'):
                s = "clubs_4.png"
            elif(self.hand[k].suit == 'Spades'):
                s = "spades_4.png"
            elif(self.hand[k].suit == 'Hearts'):
                s = "hearts_4.png"
            else:
                s = "diamonds_4.png"
                
        elif(self.hand[k].val == 5):
            if(self.hand[k].suit == 'Clubs'):
                s = "clubs_5.png"
            elif(self.hand[k].suit == 'Spades'):
                s = "spades_5.png"
            elif(self.hand[k].suit == 'Hearts'):
                s = "hearts_5.png"
            else:
                s = "diamonds_5.png"
                
        elif(self.hand[k].val == 6):
            if(self.hand[k].suit == 'Clubs'):
                s = "clubs_6.png"
            elif(self.hand[k].suit == 'Spades'):
                s = "spades_6.png"
            elif(self.hand[k].suit == 'Hearts'):
                s = "hearts_6.png"
            else:
                s = "diamonds_6.png"
                
        elif(self.hand[k].val == 7):
            if(self.hand[k].suit == 'Clubs'):
                s = "clubs_7.png"
            elif(self.hand[k].suit == 'Spades'):
                s = "spades_7.png"
            elif(self.hand[k].suit == 'Hearts'):
                s = "hearts_7.png"
            else:
                s = "diamonds_7.png"
                
        elif(self.hand[k].val == 8):
            if(self.hand[k].suit == 'Clubs'):
                s = "clubs_8.png"
            elif(self.hand[k].suit == 'Spades'):
                s = "spades_8.png"
            elif(self.hand[k].suit == 'Hearts'):
                s = "hearts_8.png"
            else:
                s = "diamonds_8.png"
                
        elif(self.hand[k].val == 9):
            if(self.hand[k].suit == 'Clubs'):
                s = "clubs_9.png"
            elif(self.hand[k].suit == 'Spades'):
                s = "spades_9.png"
            elif(self.hand[k].suit == 'Hearts'):
                s = "hearts_9.png"
            else:
                s = "diamonds_9.png"
                
        elif(self.hand[k].val == 10):
            if(self.hand[k].suit == 'Clubs'):
                s = "clubs_10.png"
            elif(self.hand[k].suit == 'Spades'):
                s = "spades_10.png"
            elif(self.hand[k].suit == 'Hearts'):
                s = "hearts_10.png"
            else:
                s = "diamonds_10.png"  
                
        elif(self.hand[k].val == 11):
            if(self.hand[k].suit == 'Clubs'):
                s = "clubs_jack.png"
            elif(self.hand[k].suit == 'Spades'):
                s = "spades_jack.png"
            elif(self.hand[k].suit == 'Hearts'):
                s = "hearts_jack.png"
            else:
                s = "diamonds_jack.png"   
                
        elif(self.hand[k].val == 12):
            if(self.hand[k].suit == 'Clubs'):
                s = "clubs_queen.png"
            elif(self.hand[k].suit == 'Spades'):
                s = "spades_queen.png"
            elif(self.hand[k].suit == 'Hearts'):
                s = "hearts_queen.png"
            else:
                s = "diamonds_queen.png"                
        else:           
            if(self.hand[k].suit == 'Clubs'):
                s = "clubs_king.png"
            elif(self.hand[k].suit == 'Spades'):
                s = "spades_king.png"
            elif(self.hand[k].suit == 'Hearts'):
                s = "hearts_king.png"
            else:
                s = "diamonds_king.png"   
        return s   
    
class SixDeck:
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        self.cards = []
        for i in range (0,6):
            for s in ["Spades", "Clubs", "Hearts", "Diamonds"]:
                for v in range(1,14):
                    self.cards.append(Card(v,s))
    def shuffle(self):
        for i in range(1,15):
            for i in range(len(self.cards) -1, 0, -1):
                r = random.randint(0, i)
                self.cards[i], self.cards[r] = self.cards[r], self.cards[i]  
        
    def draw(self):
        return self.cards.pop()
            
    def display(self):
        for c in self.cards:
            print(c.val, c.suit)  
            
    def peekNextVal(self):
        return self.cards[len(self.cards)-1].val
    
    def cardNum(self):
        count = 0
        for c in self.cards:
            count +=1 
        return count
    
    def sixDeckGame():
        root = tk.Tk() 
         
        frame_List = []
        image_List = []
        hitButton_List = []
        standButton_List = []
        doubleButton_List = []
        splitButton_List = []
        playAgainButton_List = []
        colorUpButton_List = []
        
        
        p1 = Player1()
        d = Dealer()
        deck = SixDeck()
        deck.shuffle()
        
        global frameCount 
        frameCount = 0
        
        global imageCount 
        imageCount = 0
        
        global betSize 
        betSize = 0 
        
        global playerCardTracker 
        playerCardTracker =0
        
        global dealerCardTracker
        dealerCardTracker =0
        
        global downCardIndex
        downCardIndex = 0
        
        def getCardString(s,v):
            if(v == 1):
                valString = "ace"
            elif(v == 11):
                valString = "jack"
            elif(v == 12):
                valString = "queen"
            elif(v == 13):
                valString = "king"
            else:
                valString = str(v)           
            fileName = s.lower() +"_"+valString+".png"
            card = Image.open(fileName)
            cim = card.resize((95,145), Image.ANTIALIAS)
            im_card = ImageTk.PhotoImage(cim) 
            image_List.append(im_card)
            
        def clearFrame():
            for widgets in frame_List[globals()['frameCount']].winfo_children():               
                widgets.destroy()
            frame_List[globals()['frameCount']].destroy()
        
        def start():
            p1.addChips(float(buyInEntry.get()))
            
            deal()
            
        def deal():
            clearFrame()
            globals()['frameCount'] += 1
            print(globals()['frameCount'])
            frame_List[globals()['frameCount']].pack(padx = 1, pady = 1)
            
            
            p1.reset()
            d.reset()
            
            p1.loseChips(globals()['betSize'])
           

            globals()['playerCardTracker'] = 0
            globals()['dealerCardTracker'] = 0
            
            p1.draw(deck)
            getCardString(p1.getSuit(),p1.getVal())
            Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x = 500 + globals()['playerCardTracker'], y = 500)
            globals()['imageCount'] += 1
            globals()['playerCardTracker'] += 100
            

            
            d.draw(deck)    
            getCardString(d.getSuit(),d.getVal())
            globals()['downCardIndex'] = globals()['imageCount']
            Label(frame_List[globals()['frameCount']], image = imbc).place(x = 300 + globals()['dealerCardTracker'] , y = 100)
            globals()['dealerCardTracker'] += 100
            globals()['imageCount'] += 1
           
            p1.draw(deck)
            getCardString(p1.getSuit(),p1.getVal())
            Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x = 300 + globals()['playerCardTracker'], y = 500)
            globals()['imageCount'] += 1
            globals()['playerCardTracker'] += 100

            d.draw(deck)    
            getCardString(d.getSuit(),d.getVal())
            Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x = 300 + globals()['dealerCardTracker'] , y = 100)
            globals()['dealerCardTracker'] += 100
            globals()['imageCount'] += 1
            
            pscore = str(p1.score())
            Label(frame_List[globals()['frameCount']], text = "Players Score: " + pscore).place(x = 300, y = 650)  
              
            hitButton_List[globals()['frameCount']].place(x = 400, y = 450)

            print('hi')
            Label(frame_List[globals()['frameCount']], text = "Player Chip Count: $" + str(p1.chipCount())).place(x = 300, y = 750)
    
        def hit():
            print('hi')
            
        for i in range (0,200):
            frame_List.append(LabelFrame(root, width = 2000, height = 2000,background = 'darkgray'))
            hitButton_List.append(Button(frame_List[i],text="Hit",command = hit, height = 3, width = 3, background ='salmon', font = ("Arial", 15)))
        
        
        frame_List[0].pack()
        Button(frame_List[0], text = "Play BlackJack", command = start, height = 10, width = 25,background = 'salmon',font = ("Arial",25)).place(x=700,y=100)
        buyInEntry = Entry(frame_List[0], font = ("Arial", 15))
        buyInLabel = Label(frame_List[0], font =("Arial", 15), text ="Chips Buy In $: ")
        betEntry = Entry(frame_List[0],font = ("Arial", 15))
        betLabel = Label(frame_List[0], font =("Arial", 15), text ="Intial Bet Size $: ")
        plus3Entry = Entry(frame_List[0], font = ("Arial", 15))
        plus3Label = Label(frame_List[0], font =("Arial", 15), text ="Plus 3 Bet Size $: ")
        buyInLabel.place(x=700, y = 550)
        buyInEntry.place(x = 870, y = 550)
        betLabel.place(x=700, y = 650)
        betEntry.place(x = 870, y = 650)
        plus3Label.place(x=700, y = 750)
        plus3Entry.place(x = 870, y = 750)
        
        bc = Image.open('blue.png')
        dbc = bc.resize((95,145), Image.ANTIALIAS)
        imbc = ImageTk.PhotoImage(dbc)
        
        
        root.mainloop()

SixDeck.sixDeckGame()