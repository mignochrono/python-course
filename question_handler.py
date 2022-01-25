#question handler test from course
trigger = 1
while trigger==1:
    print('how many cats do you have?')
    numcats = input()
    try:
        if int(numcats) >= 5: #increased number of cats
            print ('thats is a lot of cats.')
            trigger=0
        else:
            print ('that is not  that many cats')
            trigger=0
    except ValueError:
        print ('you did not enter a number')
        trigger = 1
 #banana banana justa dding text to see how to commit changes LALALALA
