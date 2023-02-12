from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # return int(float(-12)/16)
        operators=set(("+","-","*","/"))
        stack=[]

        def operatorService(operator,first,second):
             if operator=="+": return first+second
             elif operator=="-": return first-second
             elif operator=="*": return first*second
             else: return int(first/second)
                #   return 0 if abs(second)>abs(first) else first//second
                  

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                if stack:  second=stack.pop()
                else: second=0

                if stack: first=stack.pop()
                else: first=0

                value=operatorService(operator=t,first=first,second=second)
                stack.append(value)
        
        return stack.pop()
             


if __name__=="__main__":
        tokens=["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
        print(Solution().evalRPN(tokens=tokens))