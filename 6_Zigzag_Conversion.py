class Solution:
    def convert(self, s: str, numRows: int) -> str:
        start=1
        hashMap={f"list{start}":[""]*numRows}
        FULL=True

        index=0
        for i,string in enumerate(s):
            if FULL and index<numRows:
                hashMap[f"list{start}"][index]=string
                if index==numRows-1:
                    start+=1
                    if index in [0,1]:
                        index=0
                        FULL=True
                        hashMap[f"list{start}"]=[""]*numRows
                    else:
                        index-=1
                        FULL=False 
                else:
                    index+=1
            elif not FULL:
                hashMap[f"list{start}"]=[""]*numRows
                if index>0:
                    hashMap[f"list{start}"][index]=string
                    index-=1
                    start+=1
                    if index==0:
                        FULL=True
                        hashMap[f"list{start}"]=[""]*numRows
        
        finalString=""
        for j in range(numRows):
            for k in hashMap.keys():
                if hashMap[k][j]:
                    finalString+=hashMap[k][j]

        return finalString


if __name__=="__main__":
    s="ABC"
    s="PAYPALISHIRING"
    numRows=3
    print(Solution().convert(s=s,numRows=numRows))