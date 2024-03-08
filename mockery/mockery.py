import sys,getopt,random
 
def sanityChecks(sarcasmLevel):
    if sarcasmLevel < 0:
        print('negative mockery???')
        quit()
    elif sarcasmLevel == 0:
        print('What do you need me for???')
        quit()
    elif sarcasmLevel > 6:
        print('☣️ mockery level is hazardous')
        quit()

def main():
    options,_ = getopt.getopt(sys.argv[1:],"s:t:h")

    sarcasmLevel,textIndex = None,None

    for index,item in enumerate(options):
        if item[0] == '-s':
            sarcasmLevel = int(item[1])
        elif item[0] == '-t':
            textIndex = index
        elif item[0] == '-h':
            print('-h: Displays what you see here')
            print('-s: Sarcasm Level [1,6]')
            print('-t: <inputText>; Input text that needs to be sarcasmed')
            quit()

    if sarcasmLevel == None:
        sarcasmLevel = 1

    sanityChecks(sarcasmLevel)
    

    if textIndex == None:
        print('Expected arg -t with text')
        print('Example: sar -t "Hello World"')
        quit()

    new = ''
    c = [False,False,False,False]+[True]*sarcasmLevel
    
    for char in options[textIndex][1]:
        if char == 'o': new += char.upper()

        elif random.choice(c): new += char.upper()

        else: new += char.lower()

    print(new)