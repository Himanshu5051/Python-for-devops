import random

lucky_num = random.randint(1,51)


while True:
 num = int(input("Guess a number b/w 1 to 50: "))
    
 if num==lucky_num:
  print("!!Congratulation You Guess the Correct Number!! ",)
  break
    
     
 elif num>lucky_num:
  print("Your Number is to High")

 elif num<lucky_num:
  print("Your Number is to less")

print("                         ")
print("The Number is:",lucky_num)
print("                         ")
print("-----Game is Over-----")
    
    


   

  
    
    