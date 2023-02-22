
def print_big(letter):
    patterns = {1:'*',2:'* *',3:'*   *',4:'******',5:'****',6:' *',7:'  *  ',8:'*    *',9:'*  '}
    alphabet = {'A':[7,3,4,8,8],'B':[5,3,8,3,2,1,2,3,8,3,5]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
print_big('a')

