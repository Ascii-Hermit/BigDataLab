'''
Question 1: 
Make a crypt arithmetic program to solve PAY*MY = MONEY

'''


from itertools import permutations


def getUniqueChars(op1, op2, res):
    chars = set()
    for i in op1:
        chars.add(i)
    for i in op2:    
        chars.add(i)
    for i in res:
        chars.add(i)
    return chars

def checkSol(mapping, op1, op2, res):
    op1_val = 0
    op2_val = 0
    res_val = 0
    for i in op1:
        op1_val = op1_val*10 + mapping[i]
    for i in op2:
        op2_val = op2_val*10 + mapping[i]
    for i in res:
        res_val = res_val*10 + mapping[i]
        
    if op1_val*op2_val == res_val:
        return True
    return False 


def main():
    op1 = "PAY"
    op2 = "MY"
    res = "MONEY"
    solution = []
    chars = getUniqueChars(op1, op2, res)
    digits = [0,1,2,3,4,5,6,7,8,9]

    for perm in permutations(digits, len(chars)):
        mapping = dict(zip(chars, perm))
        if checkSol(mapping, op1, op2 ,res):
            solution.append(mapping)
    for i in solution:
        print(i)
        

if __name__ == "__main__":
    main()