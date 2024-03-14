import sys,getopt,random
 
def sanityChecks(mockeryLevel):
    if mockeryLevel < 0:
        print('negative mockery???')
        quit()
    elif mockeryLevel == 0:
        print('What do you need me for???')
        quit()
    elif mockeryLevel > 6:
        print('☣️ mockery level is hazardous')
        quit()

def main():
    options,_ = getopt.getopt(sys.argv[1:],"m:t:h")

    mockeryLevel,textIndex = None,None

    for index,item in enumerate(options):
        if item[0] == '-m':
            mockeryLevel = int(item[1])
        elif item[0] == '-t':
            textIndex = index
        elif item[0] == '-h':
            print('-h: Displays what you see here')
            print('-m: Mockery Level [1,6]')
            print('-t: <inputText>; Input text that needs to be mocked')
            quit()

    if mockeryLevel == None:
        mockeryLevel = 1

    sanityChecks(mockeryLevel)
    

    if textIndex == None:
        print('Expected arg -t with text')
        print('Example: mockery -t "Hello World"')
        quit()

    new = ''
    c = [False,False,False,False]+[True]*mockeryLevel
    
    for char in options[textIndex][1]:
        if char == 'o': new += char.upper()

        elif random.choice(c): new += char.upper()

        else: new += char.lower()

    print(new)