
score = int(input('Enter score:'))

if score <= 34:
    print('Your score is '+str(score) + ' you failed!')
elif score>34 and score<= 44:
    print('Your score is '+str(score) + ' you have a Pass!')
elif score > 44 and score <= 49:
    print('Your score is '+str(score) + ' you had fair average')
elif score >49 and score <= 59:
    print('Your score is '+str(score) + ' you did good')
elif score >59 and score <= 69:
    print('Your score is '+ str(score) + ' you did very good')
elif score >69 and score <=100:
    print('Your score is '+str(score)+ 'you did excellently')
else:
    print('Invalid score')
