class Solution:
    def calculate(self, s: str) -> int:
        lastAdd,lastSub,lastMul,lastDiv=[False for i in range(4)]
        multiplier=1
        lst=[]
        for char in s:
            # If the Character corresponds to a number
            if ord(char)>=48 and ord(char)<=57:
                # if it's a new number
                if (not lastAdd and not lastSub and not lastMul and not lastDiv and multiplier==1):
                    lst.append(int(char))
                # if it's a continued number
                elif (not lastAdd and not lastSub and not lastMul and not lastDiv and multiplier==10):
                    num=lst.pop()
                    if num>=0: lst.append(num*multiplier+int(char))
                    else: lst.append(num*multiplier-int(char))
                # if last operation was an addition
                elif lastAdd:
                    # if it is the first number
                    if multiplier==1:   num=int(char)*1
                    # if the subtracted number continues
                    else: num=num*multiplier+int(char)
                # if last operation was a subtraction
                elif lastSub:
                    # if it is the first number
                    if multiplier==1:   num=int(char)*-1
                    # if the to be subtracted number continues
                    else: num=num*multiplier-int(char)
                # if last operation was a division
                elif lastDiv:
                    # if it is the first number
                    if multiplier==1:   num=int(char)
                    # if the to be divided number continues
                    else:  num=num*multiplier+int(char)
                # if last operation was a multiplication
                elif lastMul:
                    # if it is the first number
                    if multiplier==1:   num=int(char)
                    # if the to be multiplied number continues
                    else: num=num*multiplier+int(char)
                multiplier=10
            # If the Character corresponds to +,-,/ or +
            elif ord(char)==43 or ord(char)==45 or ord(char)==47 or ord(char)==42: 
                if lastAdd: lastAdd=False; lst.append(num)
                elif lastSub: lastSub=False; lst.append(num)
                elif lastMul: lastNum=lst.pop();  lst.append(lastNum*num); lastMul=False
                elif lastDiv: lastNum=lst.pop(); lst.append(-1*((-1*lastNum)//num)) if lastNum<0 else lst.append(lastNum//num);lastDiv=False
                multiplier=1
                if ord(char)==43: lastAdd=True  # If the Character corresponds to addition
                elif ord(char)==45: lastSub=True  # If the Character corresponds to subtraction
                elif ord(char)==47: lastDiv=True  # If the Character corresponds to division  
                elif ord(char)==42: lastMul=True  # If the Character corresponds to multiplication

        if lastAdd: lastAdd=False; lst.append(num)
        elif lastSub: lastSub=False; lst.append(num)
        elif lastMul: lastNum=lst.pop();  lst.append(lastNum*num)
        elif lastDiv: lastNum=lst.pop(); lst.append(-1*((-1*lastNum)//num)) if lastNum<0 else lst.append(lastNum//num);lastDiv=False
        return sum(lst)

if __name__=="__main__":
    s = "8*5-45+65/3"
    print(Solution().calculate(s=s))

