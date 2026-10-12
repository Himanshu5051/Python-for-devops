# To Calculate Percentage

 #Select the Number of Subject to be Calculate
op= int(input("Enter The Number of Subejcts(5 or 6): "))

 #condition statement for the option selected b/w 5 or 6
if op==5:
 first_sub = int(input("Enter The marks Of First Subject: "))
 second_sub = int(input("Enter The marks Of Second Subject: "))
 third_sub = int(input("Enter The marks Of Third Subject: "))
 fourth_sub = int(input("Enter The marks Of Fourth Subject: "))
 fivth_sub = int(input("Enter The marks Of Fivth Subject: "))

 sum = first_sub+second_sub+third_sub+fourth_sub+fivth_sub
 percentage = (sum/500)*100

 print("                                ")
 print("Total Marks is:-",sum)
 print("Your Percentage is:-",percentage,"%")
 
elif op==6:
 first_sub = int(input("Enter The marks Of First Subject: "))
 second_sub = int(input("Enter The marks Of Second Subject: "))
 third_sub = int(input("Enter The marks Of Third Subject: "))
 fourth_sub = int(input("Enter The marks Of Fourth Subject: "))
 fivth_sub = int(input("Enter The marks Of Fivth Subject: "))
 sixth_sub = int(input("Enter The marks Of Sixth Subject: "))
 
 sum = first_sub+second_sub+third_sub+fourth_sub+fivth_sub+sixth_sub
 percentage = (sum/600)*100
 
 print("                                ")
 print("Total Marks is:-",sum)
 print("Your Percentage is:-",percentage,"%")

