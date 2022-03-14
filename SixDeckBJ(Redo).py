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
        self.splitHolding = []
        
    def draw(self,deck):
        card = deck.draw()
        self.hand.append(card)   
            
    def splitHoldReset(self):
        self.splitHolding.clear()  
        
    def display(self):
        for c in self.splitHolding:
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
    def splitToHolding(self):
        self.splitHolding.append(self.hand.pop(0))
    
    def holdingDraw(self):
        self.hand.append(self.splitHolding.pop(0))
    
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
        
    def splitHoldReset(self):
        self.splitHolding.clear()                                   
                               
                
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
        self.splitHolding = []
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
        elif(self.hand[0].val >= 10 and self.hand[1].val >= 10):
            return True        
        return False
    
    def chipCount(self):
        return self.chips
    
    def splitToHolding(self):
        self.splitHolding.append(self.hand.pop(1))
    
    def drawHolding(self):
        self.hand.append(self.splitHolding.pop(0))
        
    def splitHand(self):
        self.splitHand1.append(self.hand.pop(0))
        self.splitHand2.append(self.hand.pop(0))
    def splitHoldReset(self):
        self.splitHolding.clear()     
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

class ValueTooSmallError(Exception):
    pass
class SideBetTooSmall(Exception):
    pass
class bettoobig(Exception):
    pass
class sumtoobig(Exception):
    pass
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
        nextSplitButton_List = []
        splitResultsButton_List = []
        seeDealerTurnButton_List = []
        plus3Vals = []
        plus3Suits = []
        changeBet_List = []
        changePlus3_List = []
        changeTop3_List = []
        rebuy_List = []
        rebuyButton_List = []
        
        splitScores = []
        splitDoubles = []
        splitBJ = []
        
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
        
        global plus3bet
        plus3bet = 0
        global top3bet
        plus3bet = 0
        global playerCardTracker 
        playerCardTracker =0
        
        global dealerCardTracker
        dealerCardTracker =0
        
        global downCardIndex
        downCardIndex = 0
        
        global doubleBool
        doubleBool = False
        
        global splitBool 
        splitBool = False
        
        
        
        def over21check(splitScores,val):
            return(all(x > val for x in splitScores))
        
        def plus3Straight(v,s):
            v.sort()
            for i in range (0,len(v)-1):
                if((v[i] + 1) == v[i+1]):
                    straight = True
                else:
                    return False
            return True
        
        def plus3Flush(s):
            return all(x == s[0] for x in s)
        
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
        
        def betExceptions():
            try:
                entry = float(buyInEntry.get())
                betEntry2 = float(betEntry.get())
                if(len(plus3Entry.get())==0):
                    plus3 = 0
                else:
                    plus3 = float(plus3Entry.get())
                if(len(top3Entry.get()) == 0):
                    top3 = 0
                else:
                    top3 = float(top3Entry.get())
                if(entry <= 0 or betEntry2 <=0):

                    raise ValueTooSmallError 
                elif(plus3 <0 or top3 <0):
                    raise SideBetTooSmall
                elif(entry <betEntry2 or entry < plus3 or entry < top3):
                    raise bettoobig
                elif(entry < betEntry2 + plus3 + top3):
                    raise sumtoobig
                else:
                    return False            
            except ValueError:
                Label(frame_List[0], text = "Buy In and Bet Size must be a number greater than 0",font=("Arial", 15)).place(x=220, y = 550)
                return True
            except ValueTooSmallError:
                Label(frame_List[0], text = "Buy In and Bet Size must be a number greater than 0",font=("Arial", 15)).place(x=220, y = 550)
                return True
            except SideBetTooSmall:
                Label(frame_List[0], text = "Side Bets can be 0 or greater than",font=("Arial", 15)).place(x=220, y = 650)
                return True
            except bettoobig:
                Label(frame_List[0], text = "Bets cannot be greater than buy in",font=("Arial", 15)).place(x=220, y = 700)
                return True
            except sumtoobig:
                Label(frame_List[0], text = " Sum of Bets cannot be greater than buy in",font=("Arial", 15)).place(x=220, y = 750)
                return True
            
        def rebuy():
            try:
                rebuy = float(rebuy_List[globals()['frameCount']].get())
                if(len(changeBet_List[globals()['frameCount']].get()) == 0):
                    changebet = 0
                else:
                    changebet = 0
                if(len(changePlus3_List[globals()['frameCount']].get())==0):
                    changePlus = 0
                else:
                    changePlus = float(changePlus3_List[globals()['frameCount']].get())
                if(len(changeTop3_List[globals()['frameCount']].get()) == 0):
                    changeTop = 0
                else:
                    changeTop = float(changeTop3_List[globals()['frameCount']].get())
                if(changebet < 0 or rebuy <=0):
                    raise ValueTooSmallError 
                elif(changePlus <0 or changeTop <0):
                    raise SideBetTooSmall
                elif(p1.chipCount() < (changebet + changePlus + changeTop)):
                    print(changebet)
                    raise bettoobig
                else:
                    return False                    
            except ValueError:
   
                Label(frame_List[globals()['frameCount']], text = "Must Enter Rebuy Amount",font=("Arial", 15)).place(x=1250, y = 50)
                return True
            except ValueTooSmallError:
       
                Label(frame_List[globals()['frameCount']], text = "Buy In and bet must be a number greater than 0",font=("Arial", 15)).place(x=650, y = 50)
                return True
            except SideBetTooSmall:
                Label(frame_List[globals()['frameCount']], text = "Side Bets can be 0 or greater than",font=("Arial", 15)).place(x=650, y = 50)
                return True
            except bettoobig:
      
                Label(frame_List[globals()['frameCount']], text = "Bets cannot exceed chipcount",font=("Arial", 15)).place(x=650, y = 50)
                return True

            
        def start():
            
            errorCheck = True
            while(errorCheck == True):
                errorCheck = betExceptions()
                if(errorCheck == True):
                    return 
                
            p1.addChips(float(buyInEntry.get()))
            globals()['betSize'] = float(betEntry.get())
            if(len(plus3Entry.get()) == 0):
                globals()['plus3bet'] = 0
            else:
                globals()['plus3bet'] = float(plus3Entry.get())
            if(len(top3Entry.get()) == 0):
                globals()['top3bet'] = 0
            else:
                globals()['top3bet'] = float(plus3Entry.get())  
            deal()
            
        def deal():
            if(len(changeBet_List[globals()['frameCount']].get()) > 0):
                globals()['betSize'] = float(changeBet_List[globals()['frameCount']].get())
            if(len(changePlus3_List[globals()['frameCount']].get()) > 0):
                globals()['plus3bet'] = float(changePlus3_List[globals()['frameCount']].get())
            plus3Vals.clear()
            plus3Suits.clear()           
            clearFrame()
            splitScores.clear()
            splitDoubles.clear()
            splitBJ.clear()
            
            
            p1.splitHoldReset()
            d.splitHoldReset()
            globals()['frameCount'] += 1
            frame_List[globals()['frameCount']].pack(padx = 1, pady = 1)
                      
            p1.reset()
            d.reset()
            

            if(globals()['doubleBool'] == True and globals()['splitBool']==False):
                globals()['betSize'] = globals()['betSize']/2
                globals()['doubleBool'] = False

            globals()['splitBool'] = False
                
            p1.loseChips(globals()['betSize'])
           
            globals()['playerCardTracker'] = 0
            globals()['dealerCardTracker'] = 0
            
            p1.draw(deck)
            getCardString(p1.getSuit(),p1.getVal())
            plus3Vals.append(p1.getVal())
            plus3Suits.append(p1.getSuit())
            Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x = 300 + globals()['playerCardTracker'], y = 500)
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
            plus3Vals.append(p1.getVal())
            plus3Suits.append(p1.getSuit())
            Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x = 300 + globals()['playerCardTracker'], y = 500)
            globals()['imageCount'] += 1
            globals()['playerCardTracker'] += 100

            d.draw(deck)    
            getCardString(d.getSuit(),d.getVal())
            plus3Vals.append(d.getVal())
            plus3Suits.append(d.getSuit())
            Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x = 300 + globals()['dealerCardTracker'] , y = 100)
            globals()['dealerCardTracker'] += 100
            globals()['imageCount'] += 1
            
            Label(frame_List[globals()['frameCount']], text = str(p1.score()),width = 7, font = ("Arial", 25)).place(x = 330, y = 680)  
              
            hitButton_List[globals()['frameCount']].place(x = 300, y = 400)
            standButton_List[globals()['frameCount']].place(x = 375, y = 400)
            
            if(globals()['betSize'] <= p1.chipCount()):
                doubleButton_List[globals()['frameCount']].place(x = 450, y = 400)
            
            if(p1.splitCheck() == True and globals()['betSize'] <= p1.chipCount()):
                splitButton_List[globals()['frameCount']].place(x = 525, y = 400)
    
            Label(frame_List[globals()['frameCount']],width = 15, text = "Plus 3 Bet", font = ("Arial",22)).place(x = 700, y = 370)
            Label(frame_List[globals()['frameCount']],width = 4, text = str(globals()['plus3bet']), font = ("Arial",22)).place(x = 750, y = 310)
            
            Label(frame_List[globals()['frameCount']],width = 15, text = "Top 3 Bet", font = ("Arial",22)).place(x = 700, y = 570)
            Label(frame_List[globals()['frameCount']],width = 4, text = str(globals()['top3bet']), font = ("Arial",22)).place(x = 750, y = 510)

            if(plus3Straight(plus3Vals,plus3Suits) == True or plus3Flush(plus3Suits) == True or plus3Flush(plus3Vals) == True):
                win = str(globals()['plus3bet'] * 9)
                p1.addChips(globals()['plus3bet'] * 10)
                Label(frame_List[globals()['frameCount']],width = 7, text = "+" + win, font = ("Arial",22),fg = 'Green').place(x = 840, y = 310)
                if(plus3Straight(plus3Vals,plus3Suits) == True):
                    Label(frame_List[globals()['frameCount']],width = 10, text = "Straight!" , font = ("Arial",25),fg = 'Green').place(x = 1040, y = 310)
                elif(plus3Flush(plus3Suits) == True):
                    Label(frame_List[globals()['frameCount']],width = 10, text = "Flush!" , font = ("Arial",25),fg = 'Green').place(x = 1040, y = 310)
                else:
                    Label(frame_List[globals()['frameCount']],width = 10, text = "3 of a Kind" , font = ("Arial",25),fg = 'Green').place(x = 1040, y = 310)

            else:
                p1.loseChips(globals()['plus3bet'])
                Label(frame_List[globals()['frameCount']],width = 7, text = "-" + str(globals()['plus3bet']), font = ("Arial",22),fg = 'red').place(x = 840, y = 310)
            
            if(plus3Flush(plus3Vals) == True and plus3Flush(plus3Suits)):
                win = str(globals()['top3bet'] * 270)
                p1.addChips(globals()['top3bet'] * 271)
                Label(frame_List[globals()['frameCount']],width = 7, text = "+" + win, font = ("Arial",22),fg = 'Green').place(x = 840, y = 510)
                Label(frame_List[globals()['frameCount']],width = 10, text = "3 of a Kind Suited!!!" + win, font = ("Arial",25),fg = 'Green').place(x = 1040, y = 510)

            elif(plus3Straight(plus3Vals,plus3Suits) == True and plus3Flush(plus3Suits)):
                win = str(globals()['top3bet'] * 180)
                p1.addChips(globals()['top3bet'] * 181)
                Label(frame_List[globals()['frameCount']],width = 7, text = "+" + win, font = ("Arial",22),fg = 'Green').place(x = 840, y = 510)
                Label(frame_List[globals()['frameCount']],width = 10, text = "Straight Flush!!" + win, font = ("Arial",25),fg = 'Green').place(x = 1040, y = 510)

            elif(plus3Flush(plus3Vals)):
                win = str(globals()['top3bet'] * 180)
                p1.addChips(globals()['top3bet'] * 181)
                Label(frame_List[globals()['frameCount']],width = 7, text = "+" + win, font = ("Arial",22),fg = 'Green').place(x = 840, y = 510)
                Label(frame_List[globals()['frameCount']],width = 10, text = "3 of a kind!" + win, font = ("Arial",25),fg = 'Green').place(x = 1040, y = 510)

            else:
                p1.loseChips(globals()['top3bet'])
                Label(frame_List[globals()['frameCount']],width = 7, text = "-" + str(globals()['top3bet']), font = ("Arial",22),fg = 'red').place(x = 840, y = 510)
                
            Label(frame_List[globals()['frameCount']], width = 15, text = "Chips $" + str(p1.chipCount()), font = ("Arial", 22)).place(x = 280, y = 750)
            Label(frame_List[globals()['frameCount']], image = idpc).place(x=700, y = 310)
            Label(frame_List[globals()['frameCount']], image = idpc).place(x=700, y = 510)
            Label(frame_List[globals()['frameCount']], image = idpc).place(x=50, y = 400)
            Label(frame_List[globals()['frameCount']], text = str(globals()['betSize']),width = 7, font = ("Arial", 20)).place(x = 100, y =400)  

            plus3Straight(plus3Vals,plus3Suits)
            plus3Flush(plus3Suits)
            plus3Flush(plus3Vals)

            
            playerBJCheck()
            dealerBJCheck()
    
        def hit():
            doubleButton_List[globals()['frameCount']].destroy()
            splitButton_List[globals()['frameCount']].destroy()
            p1.draw(deck)
            getCardString(p1.getSuit(),p1.getVal())
            Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x = 300 + globals()['playerCardTracker'], y = 500)
            globals()['imageCount'] += 1
            globals()['playerCardTracker'] += 100
            Label(frame_List[globals()['frameCount']], text = str(p1.score()),width = 7, font = ("Arial", 25)).place(x = 330, y = 680)  
            if(p1.score() > 21):
                if(len(p1.splitHolding) > 0):
                    hitButton_List[globals()['frameCount']].destroy()
                    standButton_List[globals()['frameCount']].destroy()
                    nextSplitButton_List[globals()['frameCount']].place(x = 300, y = 400)
                    splitScores.append(p1.score())
                elif(globals()['splitBool'] == True):
                    hitButton_List[globals()['frameCount']].destroy()
                    standButton_List[globals()['frameCount']].destroy()
                    if(over21check(splitScores, 21)):
                        splitScores.append(p1.score())
                        splitResultsButton_List[globals()['frameCount']].place(x = 300, y = 400)
                    else:
                        seeDealerTurnButton_List[globals()['frameCount']].place(x = 300, y = 400)
                else:
                    changeBet_List[globals()['frameCount']].place(x = 300, y = 325)
                    changePlus3_List[globals()['frameCount']].place(x = 780, y = 440)
                    Label(frame_List[globals()['frameCount']], text = "Change Plus3 Bet", width = 16, font = ("Arial", 15)).place(x = 585, y = 440)
                    Label(frame_List[globals()['frameCount']], text = "Change Bet", width = 10, font = ("Arial",15)).place(x=175,y=325)
                    Label(frame_List[globals()['frameCount']], image = image_List[globals()['downCardIndex']]).place(x = 300, y = 100)
                    changeTop3_List[globals()['frameCount']].place(x = 820, y = 640)
                    Label(frame_List[globals()['frameCount']], text = "Change Top3 Bet", width = 16, font = ("Arial", 15)).place(x = 625, y = 640)
                    hitButton_List[globals()['frameCount']].destroy()
                    standButton_List[globals()['frameCount']].destroy()
                    playAgainButton_List[globals()['frameCount']].place(x = 300, y = 400)
                    colorUpButton_List[globals()['frameCount']].place(x = 420, y = 400)
                    Label(frame_List[globals()['frameCount']], text = "Player Busted", width = 12, font = ("Arial", 25)).place(x = 330, y = 680)
                    Label(frame_List[globals()['frameCount']], text = "-" + str(globals()['betSize']), width = 6, fg = 'red', font = ("Arial", 25)).place(x = 150, y = 550)
                    if(p1.chipCount() == 0):  
                        playAgainButton_List[globals()['frameCount']].destroy()
                        rebuy_List[globals()['frameCount']].place(x = 1225, y = 450)
                        Label(frame_List[globals()['frameCount']], text = "Enter Rebuy Chips", width = 15, font = ("Arial", 24)).place(x = 1225, y = 400)
                        rebuyButton_List[globals()['frameCount']].place(x = 280, y = 400)               
                        errorCheck = True
                        rebuyCheck()
                                  
                    elif(p1.chipCount() < (globals()['betSize']+globals()['top3bet'] +globals()['plus3bet'])):
                        rebuy_List[globals()['frameCount']].place(x = 1225, y = 450)
                        Label(frame_List[globals()['frameCount']], text = "Enter Rebuy Chips", width = 15, font = ("Arial", 24)).place(x = 1225, y = 400)
                        playAgainButton_List[globals()['frameCount']].destroy()
                        rebuyButton_List[globals()['frameCount']].place(x =280, y = 400)
                        errorCheck = True               
                        rebuyCheck()

        def dealersTurn():
            seeDealerTurnButton_List[globals()['frameCount']].destroy()
            if(len(p1.splitHolding) > 0):
                splitScores.append(p1.score())
                splitDeal()
            else:
                Label(frame_List[globals()['frameCount']], image = image_List[globals()['downCardIndex']]).place(x = 300, y = 100)
                while(d.score() < 17):
                    d.draw(deck)
                    getCardString(d.getSuit(),d.getVal())
                    Label(frame_List[globals()['frameCount']], image=image_List[imageCount]).place(x = 300 + globals()['dealerCardTracker'], y = 100)
                    globals()['imageCount'] += 1
                    globals()['dealerCardTracker'] += 100
                    
                Label(frame_List[globals()['frameCount']], text = str(d.score()),width = 7, font = ("Arial", 25)).place(x = 330, y = 50)  
       
                if(d.score() > 21):
                    if(globals()['splitBool'] == True):
                        splitScores.append(p1.score())
                        hitButton_List[globals()['frameCount']].destroy()
                        standButton_List[globals()['frameCount']].destroy()
                        splitResults()
                    else:
                        hitButton_List[globals()['frameCount']].destroy()
                        standButton_List[globals()['frameCount']].destroy()
                        splitButton_List[globals()['frameCount']].destroy()
                        Label(frame_List[globals()['frameCount']], text = "Change Bet", width = 10, font = ("Arial",15)).place(x=175,y=325)
                        Label(frame_List[globals()['frameCount']], text = "Change Plus3 Bet", width = 16, font = ("Arial", 15)).place(x = 585, y = 440)
                        changeBet_List[globals()['frameCount']].place(x = 300, y = 325)
                        changePlus3_List[globals()['frameCount']].place(x = 780, y = 440)
                        changeTop3_List[globals()['frameCount']].place(x = 820, y = 640)
                        Label(frame_List[globals()['frameCount']], text = "Change Top3 Bet", width = 16, font = ("Arial", 15)).place(x = 625, y = 640)
                        playAgainButton_List[globals()['frameCount']].place(x = 300, y = 400)
                        colorUpButton_List[globals()['frameCount']].place(x = 420, y = 400)
                        p1.addChips(globals()['betSize']*2)

                        Label(frame_List[globals()['frameCount']], text = "Dealer Busted", width = 12, font = ("Arial", 25)).place(x = 330, y = 680)
                        Label(frame_List[globals()['frameCount']], text = "+" + str(globals()['betSize']), width = 6, fg = 'green', font = ("Arial", 25)).place(x = 150, y = 550)
                else:
                    if(globals()['splitBool'] == True):
                        splitScores.append(p1.score())
                        splitResults()
                    else:
                        checkWin()

        def double():
            globals()['doubleBool'] = True
            doubleButton_List[globals()['frameCount']].destroy()
            splitButton_List[globals()['frameCount']].destroy()
            globals()['betSize'] = globals()['betSize'] * 2
            p1.loseChips(globals()['betSize'])
            Label(frame_List[globals()['frameCount']], width = 15, text = "Chips $" + str(p1.chipCount()), font = ("Arial", 22)).place(x = 280, y = 750)
            p1.draw(deck)
            getCardString(p1.getSuit(),p1.getVal())
            Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x = 300 + globals()['playerCardTracker'], y = 500)
            globals()['imageCount'] += 1
            globals()['playerCardTracker'] += 100
            Label(frame_List[globals()['frameCount']], text = str(p1.score()),width = 7, font = ("Arial", 25)).place(x = 330, y = 680)  
            if(p1.score() > 21):
                if(len(p1.splitHolding) > 0):
                    splitDoubles.append(p1.score())
                    globals()['betSize'] = globals()['betSize'] / 2
                    nextSplitButton_List[globals()['frameCount']].place(x = 300, y = 400)
                elif(globals()['splitBool'] == True):
                    splitDoubles.append(p1.score())
                    globals()['betSize'] = globals()['betSize'] / 2
                    seeDealerTurnButton_List[globals()['frameCount']].place(x = 300, y = 400)
                else:
                    Label(frame_List[globals()['frameCount']], image = image_List[globals()['downCardIndex']]).place(x = 300, y = 100)
                    hitButton_List[globals()['frameCount']].destroy()
                    standButton_List[globals()['frameCount']].destroy()
                    playAgainButton_List[globals()['frameCount']].place(x = 300, y = 400)
                    colorUpButton_List[globals()['frameCount']].place(x = 420, y = 400)
                    Label(frame_List[globals()['frameCount']], text = "Player Busted", width = 12, font = ("Arial", 25)).place(x = 330, y = 680)
                    Label(frame_List[globals()['frameCount']], text = "-" + str(globals()['betSize']), width = 6, fg = 'red', font = ("Arial", 25)).place(x = 150, y = 550)
                    if(p1.chipCount() == 0):  
                        playAgainButton_List[globals()['frameCount']].destroy()
                        rebuy_List[globals()['frameCount']].place(x = 1225, y = 450)
                        Label(frame_List[globals()['frameCount']], text = "Enter Rebuy Chips", width = 15, font = ("Arial", 24)).place(x = 1225, y = 400)
                        rebuyButton_List[globals()['frameCount']].place(x = 280, y = 400)               
                        errorCheck = True
                        rebuyCheck()
                                  
                    elif(p1.chipCount() < (globals()['betSize']/2+globals()['top3bet'] +globals()['plus3bet'])):
                        rebuy_List[globals()['frameCount']].place(x = 1225, y = 450)
                        Label(frame_List[globals()['frameCount']], text = "Enter Rebuy Chips", width = 15, font = ("Arial", 24)).place(x = 1225, y = 400)
                        playAgainButton_List[globals()['frameCount']].destroy()
                        rebuyButton_List[globals()['frameCount']].place(x =280, y = 400)
                        errorCheck = True               
                        rebuyCheck()
            else:
                if(len(p1.splitHolding) > 0):
                    globals()['betSize'] = globals()['betSize'] / 2
                    splitDoubles.append(p1.score())
                    nextSplitButton_List[globals()['frameCount']].place(x = 300, y = 400)
                elif(globals()['splitBool'] == True):
                    globals()['betSize'] = globals()['betSize'] / 2
                    splitDoubles.append(p1.score())
                    seeDealerTurnButton_List[globals()['frameCount']].place(x = 300, y = 400)
                else:    
                    dealersTurn()
                
        def split():
            p1.loseChips(globals()['betSize'] )
            globals()['playerCardTracker'] = 0
            getCardString(p1.getSuit(),p1.getVal())
            Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x = 300 + globals()['playerCardTracker'], y = 500)
            globals()['imageCount'] += 1
            if(globals()['splitBool']==False):
                d.splitToHolding()
                d.splitToHolding()
            globals()['splitBool']=True

            p1.splitToHolding()
            globals()['playerCardTracker'] = 100
            p1.draw(deck)
            getCardString(p1.getSuit(),p1.getVal())
            Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x = 300 + globals()['playerCardTracker'], y = 500)
            globals()['imageCount'] += 1
            globals()['playerCardTracker'] += 100
            Label(frame_List[globals()['frameCount']], text = str(p1.score()),width = 7, font = ("Arial", 25)).place(x = 330, y = 680)  
            Label(frame_List[globals()['frameCount']], width = 25, text = "Split Hand 1", font = ("Arial", 22)).place(x = 280, y = 850)

            
            if(p1.splitCheck() == False and p1.chipCount() > globals()['betSize']):
                splitButton_List[globals()['frameCount']].destroy()
            
            playerBJCheck()

            
        def splitDeal():

            clearFrame()
            globals()['frameCount'] += 1
            frame_List[globals()['frameCount']].pack(padx = 1, pady = 1)
            p1.reset()
            globals()['playerCardTracker'] = 0
            globals()['dealerCardTracker'] = 0
            
            p1.drawHolding()
            getCardString(p1.getSuit(),p1.getVal())
            Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x = 300 + globals()['playerCardTracker'], y = 500)
            globals()['imageCount'] += 1
            globals()['playerCardTracker'] += 100
            
            d.holdingDraw()
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
            
            d.holdingDraw()
            getCardString(d.getSuit(),d.getVal())
            Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x = 300 + globals()['dealerCardTracker'] , y = 100)
            globals()['dealerCardTracker'] += 100
            globals()['imageCount'] += 1
            
            Label(frame_List[globals()['frameCount']], text = str(p1.score()),width = 7, font = ("Arial", 25)).place(x = 330, y = 680)  
              
            hitButton_List[globals()['frameCount']].place(x = 300, y = 400)
            standButton_List[globals()['frameCount']].place(x = 375, y = 400)
            doubleButton_List[globals()['frameCount']].place(x = 450, y = 400)
            if(p1.splitCheck() == True):
                splitButton_List[globals()['frameCount']].place(x = 525, y = 400)
            
            Label(frame_List[globals()['frameCount']], width = 15, text = "Chips $" + str(p1.chipCount()), font = ("Arial", 22)).place(x = 280, y = 750)
            Label(frame_List[globals()['frameCount']], width = 18, text = "Split Hand Continued", font = ("Arial", 22)).place(x = 280, y = 850)
            playerBJCheck()
            dealerBJCheck()
    
            
            
        def playerBJCheck():
            if(p1.score() == 21):
                hitButton_List[globals()['frameCount']].destroy()
                standButton_List[globals()['frameCount']].destroy()
                doubleButton_List[globals()['frameCount']].destroy()
                splitButton_List[globals()['frameCount']].destroy()
                Label(frame_List[globals()['frameCount']], text = "BLACKJACK!", width = 12, font = ("Arial", 25)).place(x = 330, y = 680)
                if(len(p1.splitHolding) > 0):
                    splitBJ.append(p1.score())
                    nextSplitButton_List[globals()['frameCount']].place(x = 300, y = 400)
                elif(globals()['splitBool'] == True):
                    splitBJ.append(p1.score())
                    seeDealerTurnButton_List[globals()['frameCount']].place(x = 300, y = 400)
                else:
                    playAgainButton_List[globals()['frameCount']].place(x = 300, y = 400)
                    colorUpButton_List[globals()['frameCount']].place(x = 420, y = 400)
                    p1.addChips(globals()['betSize']*2.5)
                    Label(frame_List[globals()['frameCount']], text = "+" + str(globals()['betSize']*1.5), width = 6, fg = 'green', font = ("Arial", 25)).place(x = 150, y = 550)
                
        def dealerBJCheck():
            if(d.score() == 21):
                Label(frame_List[globals()['frameCount']], image = image_List[globals()['downCardIndex']]).place(x = 300, y = 100)
                hitButton_List[globals()['frameCount']].destroy()
                standButton_List[globals()['frameCount']].destroy()
                doubleButton_List[globals()['frameCount']].destroy()
                splitButton_List[globals()['frameCount']].destroy()
                playAgainButton_List[globals()['frameCount']].place(x = 300, y = 400)
                colorUpButton_List[globals()['frameCount']].place(x = 420, y = 400)
                Label(frame_List[globals()['frameCount']], text = "Dealer BlackJack", width = 15, font = ("Arial", 25)).place(x = 310, y = 680)
                Label(frame_List[globals()['frameCount']], text = "-" + str(globals()['betSize']), width = 6, fg = 'red', font = ("Arial", 25)).place(x = 150, y = 550)             
                if(p1.chipCount() <= 0):  
                    playAgainButton_List[globals()['frameCount']].destroy()
                    rebuy_List[globals()['frameCount']].place(x = 1225, y = 450)
                    Label(frame_List[globals()['frameCount']], text = "Enter Rebuy Chips", width = 15, font = ("Arial", 24)).place(x = 1225, y = 400)
                    rebuyButton_List[globals()['frameCount']].place(x = 280, y = 400)               
                    errorCheck = True
                    rebuyCheck()
                                  
                elif(p1.chipCount() < (globals()['betSize']+globals()['top3bet'] +globals()['plus3bet'])):
                    rebuy_List[globals()['frameCount']].place(x = 1225, y = 450)
                    Label(frame_List[globals()['frameCount']], text = "Enter Rebuy Chips", width = 15, font = ("Arial", 24)).place(x = 1225, y = 400)
                    playAgainButton_List[globals()['frameCount']].destroy()
                    rebuyButton_List[globals()['frameCount']].place(x =280, y = 400)
                    errorCheck = Trure               
                    rebuyCheck()
        def checkWin():
            hitButton_List[globals()['frameCount']].destroy()
            splitButton_List[globals()['frameCount']].destroy()
            standButton_List[globals()['frameCount']].destroy()
            playAgainButton_List[globals()['frameCount']].place(x = 300, y = 400)
            colorUpButton_List[globals()['frameCount']].place(x = 420, y = 400)
            changeBet_List[globals()['frameCount']].place(x = 300, y = 325)
            changePlus3_List[globals()['frameCount']].place(x = 780, y = 440)
            Label(frame_List[globals()['frameCount']], text = "Change Plus3 Bet", width = 16, font = ("Arial", 15)).place(x = 585, y = 440)
            Label(frame_List[globals()['frameCount']], text = "Change Bet", width = 10, font = ("Arial",15)).place(x=175,y=325)
            changeTop3_List[globals()['frameCount']].place(x = 820, y = 640)
            Label(frame_List[globals()['frameCount']], text = "Change Top3 Bet", width = 16, font = ("Arial", 15)).place(x = 625, y = 640)
            if(p1.score() > d.score()):
                p1.addChips(globals()['betSize']*2)
                Label(frame_List[globals()['frameCount']], text = "Player Wins", width = 12, font = ("Arial", 25)).place(x = 330, y = 680)
                Label(frame_List[globals()['frameCount']], text = "+" + str(globals()['betSize']), width = 6, fg = 'green', font = ("Arial", 25)).place(x = 150, y = 550)
            elif(p1.score() == d.score()):
                p1.addChips(globals()['betSize'])
                Label(frame_List[globals()['frameCount']], text = "Bets Pushed", width = 12, font = ("Arial", 25)).place(x = 330, y = 680)
                Label(frame_List[globals()['frameCount']], text = "+0", width = 6, font = ("Arial", 25)).place(x = 150, y = 550)
            else:
                Label(frame_List[globals()['frameCount']], text = "Dealer Wins", width = 12, font = ("Arial", 25)).place(x = 330, y = 680)
                Label(frame_List[globals()['frameCount']], text = "-" + str(globals()['betSize']), width = 6, fg = 'red', font = ("Arial", 25)).place(x = 150, y = 550)
            if(p1.chipCount() <= 0):  
                playAgainButton_List[globals()['frameCount']].destroy()
                rebuy_List[globals()['frameCount']].place(x = 1225, y = 450)
                Label(frame_List[globals()['frameCount']], text = "Enter Rebuy Chips", width = 15, font = ("Arial", 24)).place(x = 1225, y = 400)
                rebuyButton_List[globals()['frameCount']].place(x = 280, y = 400)               
                errorCheck = True
                rebuyCheck()
                              
            elif(p1.chipCount() < (globals()['betSize']+globals()['top3bet'] +globals()['plus3bet'])):
                rebuy_List[globals()['frameCount']].place(x = 1225, y = 450)
                Label(frame_List[globals()['frameCount']], text = "Enter Rebuy Chips", width = 15, font = ("Arial", 24)).place(x = 1225, y = 400)
                playAgainButton_List[globals()['frameCount']].destroy()
                rebuyButton_List[globals()['frameCount']].place(x =280, y = 400)
                errorCheck = True               
                rebuyCheck()
                
        def rebuyCheck():
            errorCheck = True
            while(errorCheck == True):
                errorCheck = rebuy()
                if(errorCheck == True):
                    return 
            p1.addChips(float(rebuy_List[globals()['frameCount']].get()))
            deal()  
            
        def splitResults():

            hitButton_List[globals()['frameCount']].destroy()
            standButton_List[globals()['frameCount']].destroy()
            doubleButton_List[globals()['frameCount']].destroy()
            splitButton_List[globals()['frameCount']].destroy()
            playAgainButton_List[globals()['frameCount']].place(x = 300, y = 400)
            colorUpButton_List[globals()['frameCount']].place(x = 420, y = 400)
            Label(frame_List[globals()['frameCount']], width = 18, text = "Split Hand Results", font = ("Arial", 22)).place(x = 280, y = 850)
            changeBet_List[globals()['frameCount']].place(x = 300, y = 325)
            changePlus3_List[globals()['frameCount']].place(x = 780, y = 440)
            Label(frame_List[globals()['frameCount']], text = "Change Plus3 Bet", width = 16, font = ("Arial", 15)).place(x = 585, y = 440)
            Label(frame_List[globals()['frameCount']], text = "Change Bet", width = 10, font = ("Arial",15)).place(x=175,y=325)
            changeTop3_List[globals()['frameCount']].place(x = 780, y = 640)
            Label(frame_List[globals()['frameCount']], text = "Change Top3 Bet", width = 16, font = ("Arial", 15)).place(x = 585, y = 640)
            moneyCount = 0
            lossCount = 0
            winCount = 0 
            tieCount = 0
            d_winCount = 0
            d_lossCount = 0
            d_tieCount = 0 
            bjCount = 0
            Label(frame_List[globals()['frameCount']], image = idpc).place(x=700, y = 310)
            Label(frame_List[globals()['frameCount']], image = idpc).place(x=700, y = 510)
            Label(frame_List[globals()['frameCount']], image = idpc).place(x=50, y = 400)
            Label(frame_List[globals()['frameCount']],width = 15, text = "Plus 3 Bet", font = ("Arial",22)).place(x = 700, y = 370)
            Label(frame_List[globals()['frameCount']],width = 4, text = str(globals()['plus3bet']), font = ("Arial",22)).place(x = 750, y = 310)
            
            Label(frame_List[globals()['frameCount']],width = 15, text = "Top 3 Bet", font = ("Arial",22)).place(x = 700, y = 570)
            Label(frame_List[globals()['frameCount']],width = 4, text = str(globals()['top3bet']), font = ("Arial",22)).place(x = 750, y = 510)
            Label(frame_List[globals()['frameCount']], text = str(globals()['betSize']),width = 7, font = ("Arial", 20)).place(x = 100, y =400)  

            for i in splitScores:
                if(i >21):
                    moneyCount-=globals()['betSize']
                    lossCount +=1
                elif(d.score() > 21):
                    p1.addChips(globals()['betSize']*2)
                    moneyCount+=globals()['betSize']
                    winCount +=1
                elif(i > d.score()):
                    p1.addChips(globals()['betSize']*2)
                    moneyCount+=globals()['betSize']
                    winCount +=1
                elif(i == d.score()):
                    p1.addChips(globals()['betSize'])
                    tieCount += 1
                else:
                    moneyCount-=globals()['betSize']
                    lossCount +=1
                    
            for i in splitDoubles:
                if(i >21):
                    moneyCount-=globals()['betSize']*2
                    d_lossCount +=1
                elif(d.score() > 21):
                    p1.addChips(globals()['betSize']*4)
                    moneyCount+=globals()['betSize']*2
                    d_winCount +=1
                elif(i > d.score()):
                    p1.addChips(globals()['betSize']*4)
                    moneyCount+=globals()['betSize']*2
                    d_winCount +=1
                elif(i == d.score()):
                    p1.addChips(globals()['betSize']*2)
                    d_tieCount += 1
                else:
                    moneyCount-=globals()['betSize']*2
                    d_lossCount +=1
                    
            for i in splitBJ:
                p1.addChips(globals()['betSize']*2.5)
                bjCount +=1
            
            if((d_winCount > 0 or d_lossCount > 0 or d_tieCount) > 0 and bjCount > 0):
                Label(frame_List[globals()['frameCount']], text = " BlackJacks! " + str(bjCount) + "Win " + str(winCount) + " Lost " + str(lossCount) + " Tied " + str(tieCount) +" Double Wins " + str(d_winCount) + " Double Lost " + str(d_lossCount) + " Double Tie " + str(d_tieCount), width = 80, font = ("Arial", 25)).place(x = 280, y = 680)
            elif(d_winCount > 0 or d_lossCount > 0 or d_tieCount > 0):    
                Label(frame_List[globals()['frameCount']], text = " Win " + str(winCount) + " Lost " + str(lossCount) + " Tied " + str(tieCount) +" Double Wins " + str(d_winCount) + " Double Lost " + str(d_lossCount) + " Double Tie " + str(d_tieCount), width = 80, font = ("Arial", 25)).place(x = 280, y = 680)
            elif(bjCount > 0):
                Label(frame_List[globals()['frameCount']], text = "BlackJacks " + str(bjCount) + "Win " + str(winCount) + " Lost " + str(lossCount) + " Tied " + str(tieCount), width = 50, font = ("Arial", 25)).place(x = 280, y = 680)
            else:
                Label(frame_List[globals()['frameCount']], text = "Win " + str(winCount) + " Lost " + str(lossCount) + " Tied " + str(tieCount), width = 20, font = ("Arial", 25)).place(x = 280, y = 680)
            if(moneyCount >= 0):
                Label(frame_List[globals()['frameCount']], text = "+" + str(moneyCount), width = 6, fg = 'Green', font = ("Arial", 25)).place(x = 150, y = 550)
            else:
                Label(frame_List[globals()['frameCount']], text = str(moneyCount), width = 6, fg = 'red', font = ("Arial", 25)).place(x = 150, y = 550)
      
            if(p1.chipCount() <= 0):  
                playAgainButton_List[globals()['frameCount']].destroy()
                rebuy_List[globals()['frameCount']].place(x = 1225, y = 450)
                Label(frame_List[globals()['frameCount']], text = "Enter Rebuy Chips", width = 15, font = ("Arial", 24)).place(x = 1225, y = 400)
                rebuyButton_List[globals()['frameCount']].place(x = 280, y = 400)               
                errorCheck = True
                rebuyCheck()
                              
            elif(p1.chipCount() < (globals()['betSize']+globals()['top3bet'] +globals()['plus3bet'])):
                rebuy_List[globals()['frameCount']].place(x = 1225, y = 450)
                Label(frame_List[globals()['frameCount']], text = "Enter Rebuy Chips", width = 15, font = ("Arial", 24)).place(x = 1225, y = 400)
                playAgainButton_List[globals()['frameCount']].destroy()
                rebuyButton_List[globals()['frameCount']].place(x =280, y = 400)
                errorCheck = True               
                rebuyCheck()   
                    
            
        for i in range (0,200):
            frame_List.append(LabelFrame(root, width = 2000, height = 2000,background = 'darkgray'))
            hitButton_List.append(Button(frame_List[i],text="Hit",command = hit, height = 2, width = 5, background ='salmon', font = ("Arial", 15)))
            standButton_List.append(Button(frame_List[i],text = "Stand",command = dealersTurn, height = 2, width = 5, background = 'turquoise',font = ("Arial", 15)))
            doubleButton_List.append(Button(frame_List[i], text = "Double", command = double, height = 2, width = 5, background = 'fuchsia', font = ("Arial", 15)))
            splitButton_List.append(Button(frame_List[i], text = "Split", command = split, height = 2, width = 5, background = 'gold',font = ("Arial", 15)))
            playAgainButton_List.append(Button(frame_List[i], text = "Play Again", command = deal, height = 2, width = 8, background = 'aqua', font =("Arial", 15)))
            colorUpButton_List.append(Button(frame_List[i], text = "Color Up", command = clearFrame, width = 8, height = 2, background = 'coral', font =("Arial", 15))) 
            nextSplitButton_List.append(Button(frame_List[i], text = "See Next Split", command = splitDeal, width = 15, height = 2, background = 'khaki', font = ("Arial", 15))) 
            splitResultsButton_List.append(Button(frame_List[i], text = "See Split Results", command = splitResults, width = 15, height = 2, background = 'cyan', font = ("Arial", 15)))
            seeDealerTurnButton_List.append(Button(frame_List[i], text = "See Dealers Turn", command = dealersTurn, width = 15, height = 2, background = 'khaki', font = ("Arial", 15)))
            changeBet_List.append(Entry(frame_List[i], font = ("Arial", 15)))
            changePlus3_List.append(Entry(frame_List[i],font = ("Arial", 15)))
            changeTop3_List.append(Entry(frame_List[i], font = ("Arial", 15)))
            rebuy_List.append(Entry(frame_List[i],font = ("Arial", 15)))
            rebuyButton_List.append(Button(frame_List[i], text = "Rebuy Chips", command = rebuyCheck, height = 2, width = 10, background = 'gold', font = ("Arial", 15)))
            
            
        frame_List[0].pack()
        Button(frame_List[0], text = "Play BlackJack", command = start, height = 10, width = 25,background = 'salmon',font = ("Arial",25)).place(x=700,y=100)
        buyInEntry = Entry(frame_List[0], font = ("Arial", 15))
        buyInLabel = Label(frame_List[0], font =("Arial", 15), text ="Chips Buy In $: ")
        betEntry = Entry(frame_List[0],font = ("Arial", 15))
        betLabel = Label(frame_List[0], font =("Arial", 15), text ="Intial Bet Size $: ")
        plus3Entry = Entry(frame_List[0], font = ("Arial", 15))
        plus3Label = Label(frame_List[0], font =("Arial", 15), text ="Plus 3 Bet Size $: ")
        top3Entry = Entry(frame_List[0], font = ("Arial",15))
        top3Label = Label(frame_List[0], font = ("Arial", 15), text = "Top 3 Bet Size$: ")
        buyInLabel.place(x=700, y = 550)
        buyInEntry.place(x = 870, y = 550)
        betLabel.place(x=700, y = 650)
        betEntry.place(x = 870, y = 650)
        plus3Label.place(x=700, y = 750)
        plus3Entry.place(x = 870, y = 750)
        top3Entry.place(x=870, y = 850)
        top3Label.place(x=700, y = 850)
        bc = Image.open('blue.png')
        dbc = bc.resize((95,145), Image.ANTIALIAS)
        imbc = ImageTk.PhotoImage(dbc)
        
        pc = Image.open('pokerchip.png')
        dpc = pc.resize((40, 40), Image.ANTIALIAS)
        idpc = ImageTk.PhotoImage(dpc)
        
        root.mainloop()

SixDeck.sixDeckGame()