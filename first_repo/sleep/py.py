age=int(input("age"))
hrs=int(input("hrs"))
flag=1
if(age==1 or age==2):
    if(hrs==11 or hrs==12 or hrs==13 or hrs==14):
        print("YOU HAVE A HEALTHY AMOUNT OF SLEEP")
    else:
        print('''YOU DO NOT HAVE HEALTHY AMOUNT OF SLEEP
YOU SHOULD HAVE 11 TO 14 HOURS OF SLEEP''')
        flag=0
elif(age==3 or age==4 or age==5):
    if(hrs==10 or hrs==11 or hrs==12 or hrs==13):  
        print("YOU HAVE A HEALTHY AMOUNT OF SLEEP")   
    else:
        print('''YOU DO NOT HAVE A HEALTHY AMOUNT OF SLEEP
YOU SHOULD HAVE 10 TO 13 HOURS OF SLEEP''')
        flag=0
elif(age==6 or age==7 or age==8 or age==9 or age==10 or age==11 or age==12):
    if(hrs==9 or hrs==11 or hrs==12):
         print("YOU HAVE A HEALTHY AMOUNT OF SLEEP")
    else:
        print('''YOU DO NOT HAVE HEALTHY AMOUNT OF SLEEP
YOU SHOULD HAVE 9 TO 12 HOURS SLEEP''')
        flag=0
elif(age==13 or age==14 or age==15 or age==16 or age==17 or age==18):
     if(hrs==9 or hrs==11 or hrs==12):
        print("YOU HAVE A HEALTHY AMOUNT OF SLEEP")
     else:
        print('''YOU DO NOT HAVE HEALTHY AMOUNT OF SLEEP
YOU SHOULD HAVE 9 TO 12 HOURS OF SLEEP''')
        flag=0  
elif(age>18):
    if(hrs==7 or hrs==8):
         print("YOU HAVE A HEALTHY AMOUNT OF SLEEP")
    else:
        flag=0
        print('''YOU DO NOT HAVE HEALTHY AMOUNT OF SLEEP
YOU SHOULD HAVE 7 TO 8 HOURS OF SLEEP''') 
        
if(flag==0): 
    print(''' * * FACTS YOU MUST KNOW**
          1.NOT HAVING SUFFICIENT SLEEP CAN LEAD TO SLEEP DEPRIVATION WHICH EFFECTS 
          DAY TO DAY LIFE.
          2.HAVING MORE THAN 12 HOURS SLEEP CAN BE DANGEROUS CORONARY HEART DISEASE,
          STROKE,DIABETES ARE FEW PROMBELMS WHICH MAY OCCUR'''
         ) 
else:
    print("CONTINUE WITH THE SAME")     

quality=int(input("rating"))
if(quality==0 or quality==1 or quality==2 or quality==3 or quality==4 or quality==5):
    print(''' * * TIPS * *
          1.SIGNS OF INSOMIA.
          2.CONSULTATION OF A DOCTOR IS SUGGESTED''')
elif(quality==6 or quality==7 or quality==8):
    print(''' * * TIPS * *
          1.AVOIDING COFFEE AT NIGHT.
          2.MANAGING STRESS.
          3.SOOTHING SONGS CAN HELP''')   
elif(quality==9 or quality==10):
    print('''QUALITY SLEEP,YOU GET MOST OF THE BENIFITS OF SLEEP ''') 

option=input("sleep disorders?")
if (option=="yes"):
    print(''' * * TIPS * *
          1.MAINTAIN SLEEP HYGIENE
          2.QUIT ALCHOHOL AND SMOKING.
          3.RIGHT MEDICATION WILL HELP TO OVERCOME.
          4.IF CONDITION IS GETTING WORSE CONSULT A DOCTOR
          5.RECORD THE PROGESS FOR SELF EVALUATION''')
else:
    print(''' * * TIPS * *
          ALWAYS HAVE SUFFICIENT SLEEP TO STAY AWAY FROM ANY KINDS OF SLEEP DISORDERS''')  

option2=input("stress?")
if(option2=="yes"):
    print('''*TIPS*
        1.EAT HEALTHY.
        2.MEDIATE AND TRY YOGA.
        3.LIMIT ALCOHOL INTAKE.
        4.LISTEN TO MUSIC.
        5.SEEK OUT SOCIAL SUPPORT.  
                 ''')
else:
    print(''' * * TIPS * *
          ALWAYS TRY TO MANAGE STRESS ''')