#hangman game
import random
li=[                      
		
			 r"""________      
			    |      |      
			    |      0      
			    |     /|\     
			    |     / \     
			    |             """,
                      r"""________      
			 |      |      
			 |      0      
			 |     /|\     
			 |     /       
			 |             """,
                      r"""________      
			 |      |      
			 |      0      
		         |     /|\     
			 |             
			 |             """,
                      r"""________      
			 |      |      
			 |      0      
			 |     /|      
			 |             
			 |             """,
                       r"""________      
			  |      |      
			  |      0      
			  |     /       
			  |             
			  |   """,
                       r"""________      
			  |      |      
			  |      0
			  |
		          |             
			  |             """,
                          r"""  ________      
			       |    
			       |             
			       |             
			       |             
		               |     """
		
		
		]
print("Let's play Hangman.....!")
print("you have only 6 lives so try to guess the word within 6 attempts !Good Luck....!!")
l=["apple","basket","ant","purple","google","hangman","hangover","love","family","friends","career","responsibility","marraige","output","python","finally"]
word=random.choice(l)
length=len(word)
lives=6
display=[]
b="_"
for i in range(length):
   display.append(b)
print(display)
exit=False
while not exit :
        letter=input("guess a letter:").lower()
        for i in range(length):
           if word[i]==letter:
              display[i]=letter
        print(display)            
        if letter not in word:
           lives=lives-1
           print("you are wrong..!")
           print(f"you have only {lives}chances")
           if lives==0:
            exit=True
         
            print("you lose....!")
        print(li[lives])   
        if "_" not in display:
            exit=True
            print("you won.....!")
