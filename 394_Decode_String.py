class Solution:
    def decodeString(self, s: str) -> str:
        es=''
        count=0
        dct={count:{'num':'','let':''}}
        lastChar=[]
        for char in s:
           
            if ord(char)>=48 and ord(char)<58:  # numbers
                if not dct[count]['let'] and lastChar!="[":
                    nc=dct[count]['num']
                    dct[count]['num']=nc+char
                else:
                    count+=1
                    dct[count]={'num':char,'let':''}
            elif ord(char)==91:  # [
                lastChar=char
                continue
            elif ord(char)==93:  # ]
                number=int(dct[count]['num'])
                letter=dct[count]['let']
                letter=number*letter
                del dct[count]
                count=max(0,count-1)
                if dct:
                    dct[count]['let']+=letter
                else:
                    es+=letter
                    dct[count]={'num':'','let':''}
            else:  # characters
                c=dct[count]['let']
                dct[count]['let']=c+char
            lastChar=char
        if dct and dct[count]['let']:
            return es+dct[count]['let']
        else:
            return es
if __name__=="__main__":
    s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    print(Solution().decodeString(s=s))