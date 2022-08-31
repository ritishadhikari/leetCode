from typing import List
from collections import Counter
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        wu=Counter(words)
        mw=0
        ml=0

        for let in words:
            if let in wu:
                if let==let[::-1]:
                    if wu[let]>=2:
                        mw+=2*len(let)
                        wu[let]-=2
                        if not wu[let]: wu.pop(let)
                    else:
                        ml=max(ml,len(let))
                elif let[::-1] in wu:
                    mw+=2*len(let)
                    wu[let]-=1
                    wu[let[::-1]]-=1
                    if not wu[let]: wu.pop(let)
                    if not wu[let[::-1]]: wu.pop(let[::-1])
                else:
                    wu.pop(let)
            if not wu:
                break
        
        return mw+ml

if __name__=="__main__":
    words = ["cc","ll","xx"]
    words=["ab","ty","yt","lc","cl","ab"]
    print(Solution().longestPalindrome(words=words))

"""
["cbcb","ll","xx",'ll','ccc','bcbc','bcbc']
'cbcbllcccllbcbc'

wu={cbcb:1,'ll':2,"xx":1,'bcbc':2,'ccc':1}
ml=0

mw=0
cbcb
cbcb in wu: True
	cbcb==cbcb[::-1]: False  # First Cond
	cbcb[::-1] in wu:True  # Second Cond
		mw+=2*(len(cbcb))=8
		wu={'ll':2,"xx":1,'bcbc':1,'ccc':1}
ll
ll in wu:True
	ll==ll[::-1]:True  # First Cond
		wu[ll]>=2:True # First First Cond
		mw+=2*(len(ll))=12
		wu={"xx":1,'bcbc':1,'ccc':1}

xx
xx in wu:True
	xx==xx[::-1]:True  # First Cond
		wu[xx]>=2:False  # First First Cond
		else:   # First Second Cond
			ml=max(0,2)=2 # len 2
			wu={'bcbc':1,'ccc':1}
ll
ll in wu:False

ccc
ccc in wu: True
	ccc==ccc[::-1]: True
		wu[ccc]>=2: False
		else:
			sb={xx,ccc}
			wu={'bcbc':1}
			
bcbc
bcbc in wu:
	bcbc==bcbc[::-1]:False
	bcbc[::-1] in wu: False
	wu={}

max(sb)=3

mw=12+3=15

"""