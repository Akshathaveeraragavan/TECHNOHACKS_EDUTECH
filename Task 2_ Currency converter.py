#THIS IS A CURRENCY CONVERTER
print('Welcome to our currency converter system')
print('AVAILABLE OPTIONS...\n 1-INDIAN RUPEES TO US DOLLARS\n 2-DOLLARS TO INDIAN RUPEES\n 3-INDIAN RUPEES TO EURO\n 4-EURO TO INDIAN RUPEES\n 5-INDIAN RUPEES TO PAKISTANI RUPEE\n 6-PAKISTANI RUPEE TO INDIAN RUPEE\n 7-INDIAN RUPEE TO OMANI RIAL\n 8-OMANI RIAL TO INDIAN RUPEES\n 9-INDIAN RUPEES TO SINGAPORE DOLLARS\n 10-SINGAPORE DOLLARS TO INDIAN RUPEES\n 11-INDIAN RUPEES TO RUSSIAN RUBLE\n 12-RUSSIAN RUBLE TO INDIAN RUPEES\n 13-INDIAN RUPEES TO NEW TAIWAN DOLLAR\n 14-NEW TAIWAN DOLLARS TO INDIAN RUPEES\n 15-INDIAN RUPEES TO PHILIPINE PESO\n 16-PHILIPINE PESO TO INDIAN RUPEES')
choice=int(input('ENTER AN APPROPRIATE OPTION:'))
if choice==1:
    money=eval(input('Enter the amount to convert'))
    print('INR-',money,'\nUS DOLLARS-',money*0.012)
elif choice==2:
    money=eval(input('Enter the amount to convert'))
    print('US DOLLARS-',money,'\nINR-',money*82.02)
elif choice==3:
    money=eval(input('Enter the amount to convert'))
    print('INR-',money,'\nEURO-',money*0.011)
elif choice==4:
    money=eval(input('Enter the amount to convert'))
    print('EURO-',money,'\nINR-',money*92.17)
elif choice==5:
    money=eval(input('Enter the amount to convert'))
    print('INR-',money,'\nPAKISTANI RUPEE-',money*3.30)
elif choice==6:
    money=eval(input('Enter the amount to convert'))
    print('PAKISTANI RUPEE-',money,'\nINR-',money*0.30)
elif choice==7:
    money=eval(input('Enter the amount to convert'))
    print('INR-',money,'\nOMANI RIAL-',money*0.0047)
elif choice==8:
    money=eval(input('Enter the amount to convert'))
    print('OMANI RIAL-',money,'\nINR-',money*213.04)
elif choice==9:
    money=eval(input('Enter the amount to convert'))
    print('INR-',money,'\nSINGAPORE DOLLARS-',money*0.016)
elif choice==10:
    money=eval(input('Enter the amount to convert'))
    print('SINGAPORE DOLLARS-',money,'\nINR-',money*62.13)
elif choice==11:
    money=eval(input('Enter the amount to convert'))
    print('INR-',money,'\nRUSSIAN RUBLE-',money*1.10)
elif choice==12:
    money=eval(input('Enter the amount to convert'))
    print('RUSSIAN RUBLE-',money,'\nINR-',money*0.91)
elif choice==13:
    money=eval(input('Enter the amount to convert'))
    print('INR-',money,'\nNEW TAIWAN DOLLARS-',money*0.38)
elif choice==14:
    money=eval(input('Enter the amount to convert'))
    print('NEW TAIWAN DOLLARS-',money,'\nINR-',money*2.65)
elif choice==15:
    money=eval(input('Enter the amount to convert'))
    print('INR-',money,'\nPHILIPPINES PESO-',money*0.66)
elif choice==16:
    money=eval(input('Enter the amount to convert'))
    print('PHILIPPINES PESO-',money,'\nINR-',money*0.12)
else:
    print('This is a simple currency converter limited to some currency convertions.\nWe would improve more in the future.\nPlease try something that\'s available in our options')
