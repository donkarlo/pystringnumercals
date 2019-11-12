class StringInts:
    
    def __init__(self):
        return
    #multiplication of two string ints from cmd
    def biMultiFromCmd(self): 
        strNum1 = input("Enter the first integer: ")
        strNum2 = input("Enter the second integer: ")
        
        #print - if necessay and from here just deal with positive numbers
        if((strNum1[0] == '-' or strNum2[0] == '-') and
           (strNum1[0] != '-' or strNum2[0] != '-')): 
            print("-", end = '') 
        
        #remove - to generate unsigned numbers       
        if(strNum1[0] == '-' and strNum2[0] != '-'): 
            strNum1 = strNum1[1:] 
        elif(strNum1[0] != '-' and strNum2[0] == '-'): 
            strNum2 = strNum2[1:] 
        elif(strNum1[0] == '-' and strNum2[0] == '-'): 
            strNum1 = strNum1[1:] 
            strNum2 = strNum2[1:] 
        
        #store unsigned numbers
        num1=strNum1
        num2=strNum2
        
        #store lengths of two numbers
        lenNum1 = len(num1) 
        lenNum2 = len(num2) 
        
        if lenNum1 == 0 or lenNum2 == 0: 
            return "0"
    
        # will keep the resultList number in vector in reverse order 
        resultList = [0] * (lenNum1 + lenNum2) 
        
        # Below two indexes are used to find positions in resultList. 
        posNum1 = 0
        posNum2 = 0
    
        # traverse rtl in num1 
        for i in range(lenNum1 - 1, -1, -1): 
            carry = 0
            n1 = ord(num1[i]) - 48
            posNum2 = 0
            for j in range(lenNum2 - 1, -1, -1): 
                n2 = ord(num2[j]) - 48
                summ = n1 * n2 + resultList[posNum1 + posNum2] + carry 
                carry = summ // 10
                resultList[posNum1 + posNum2] = summ % 10
                posNum2 += 1
            if (carry > 0): 
                resultList[posNum1 + posNum2] += carry 
            posNum1 += 1
    
        # ignore '0's from the right 
        i = len(resultList) - 1
        while (i >= 0 and resultList[i] == 0): 
            i -= 1
    
        # if all are 0s
        if (i == -1): 
            return "0"
    
        # string gen
        strRes = "" 
        while (i >= 0): 
            strRes += chr(resultList[i] + 48) 
            i -= 1
        return strRes 
    
strInts = StringInts()
print(strInts.biMultiFromCmd()) 

