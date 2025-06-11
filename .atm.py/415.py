class Leetcode:
    def addString(self,num1,num2):
        first = len(num1) - 1
        second = len(num2) - 1
        carry = 0 
        result = []
        while first >=0  or second>=0 or carry:
           d1 = ord(num1[first])-ord('0') if first>=0 else 0
           d2 = ord(num2[second])-ord('0') if second>=0 else 0
           sum = (d1+d2+carry)%10
           carry = (d1+d2 +carry)//10
           result.append(str(sum))
           first -=1
           second -=1
           
        return ''.join(reversed(result))
    
check  = Solution()
print(check.addStrings("123", "4567"))  

