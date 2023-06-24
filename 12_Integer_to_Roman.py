class Solution:
    def intToRoman(self, num: int) -> str:
        romanStr=""
        while num>0:
            if num>=1 and num<5:
                if num>=1 and num<4:
                    romanStr+=num*"I"
                    num=0
                elif num>=4 and num<5:
                    romanStr+="IV"
                    num=0
            elif num>=5 and num<10:
                if num==5:
                    romanStr+="V"  
                    num=0
                elif num>5 and num<9:
                    romanStr+="V"
                    num%=5
                elif num>=9 and num<10:
                    romanStr+="IX"
                    num=0

            elif num>=10 and num<50:
                if num==10:
                    romanStr+="X"
                    num=0

                elif num>10 and num<40:
                    div=num//10  
                    romanStr+=div*"X"
                    num%=10
                elif num>=40 and num<50:
                    romanStr+="XL"
                    num%=10

            elif num>=50 and num<100:
                if num==50:
                    romanStr+="L"
                    num=0
                elif num>50 and num<90:
                    romanStr+="L"
                    num%=50
                elif num>=90 and num<100:
                    romanStr+="XC"
                    num%=10
            
            elif num>=100 and num<500:
                if num==100:
                    romanStr+="C"
                    num=0
                elif num>100 and num<400:
                    div=num//100
                    romanStr+=div*"C"
                    num%=100
                elif num>=400 and num<500:
                    romanStr+="CD"
                    num%=100
            
            elif num>=500 and num<1000:
                if num==500:
                    romanStr+="D"
                    num=0
                elif num>500 and num<900:
                    romanStr+="D"
                    num%=500
                elif num>=900 and num<1000:
                    romanStr+="CM"
                    num%=100
            
            elif num>=1000:
                div=num//1000
                romanStr+=div*"M"
                if num==1000:
                    num=0
                else:
                    num%=1000
        return romanStr

if __name__=="__main__":
    num=9
    print(Solution().intToRoman(num=num))