#import decoratorsdemo
#@showmessage
def decodePin4mString(sentence):
    words= sentence.split(' ')
    print(words)
    no=0
    for word in words:
        no= no + len(word)
    print(no)
    pin=0
    while no :
        rem= no%10
        pin+=rem
        no=no//10

    print(pin)

decodePin4mString("virtual training")