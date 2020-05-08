

binaryTree = ["start","E","T","I","A","N","M","S","U","R","W","D","K","G","O","H","V","F"
              ,"N/A","L"," ","P","J","B","X","C","Y","Z","Q","N/A","N/A","5","4","$","3",
              "?","-",".","2",",",":","+",";","*","%","#","1","6","=","/","N/A","N/A",
              "N/A","&","8","7","9","0"]





def EnigmaDecoder(morseCode):
    cur = 1
    output = ""
    
    for i in range(len(morseCode)):

        if( morseCode[i] == "."):
            cur = cur * 2
            #output = output + binaryTree[cur]
        elif ( morseCode[i] == "-"):
            cur = (cur * 2) + 1
            #output = output + binaryTree[cur]
        elif ( morseCode[i] == " "):
            output = output + binaryTree[cur-1]
            cur = 1
        #print(output)

        if( i == len(morseCode)-1):
            output = output + binaryTree[cur-1]
            cur = 1
    return output




print("Default Morse Code: ")
morseCode = ".-- .. - .... .-.- -- -.-- .-.- -... . ... - .-.- .-- .. ... .... . ..."

string1 = EnigmaDecoder(morseCode)
print(string1)

print("\n")

print("Other examples: ")
morseCode2 = ".... . -.-- .-.- - .... . .-. ."
string2 = EnigmaDecoder(morseCode2)
print(string2)

