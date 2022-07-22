class Solution:
    def addBinary(self, a:str, b:str) -> str:

        maxLength=max(len(a),len(b))
        c=''
        carry=0
        for i in range(-1,-maxLength-1,-1):
            if -i>len(a):
                aVal=0
            else:
                aVal=int(a[i])
            if -i>len(b):
                bVal=0
            else:
                bVal=int(b[i])
            
            if aVal and bVal:
                addVal=0
                if carry:
                    addVal=1
                carry=1
            elif (not aVal and bVal) or (aVal and not bVal):
                addVal=1
                if carry:
                    addVal=0
                    carry=1
            elif (not aVal and not bVal):
                addVal=0
                if carry:
                    addVal=1
                    carry=0
            
            c=str(addVal)+c
        
        if carry:
            return '1'+c
        else:
            return c
            




if __name__=="__main__":
    a = "1010"
    b = "1011"
    print(Solution().addBinary(a=a,b=b))
