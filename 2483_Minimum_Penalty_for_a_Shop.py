from collections import Counter
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        present=minimum=Counter(customers)['Y']
        previous=None
        answer=0
        for i in range(1,len(customers)+1):
            previous=present
            if customers[i-1]=="Y":
                present=previous-1
                if minimum>present:
                    minimum=present
                    answer=i
            else:
                present=previous+1

        return answer

if __name__=="__main__":
    customers = "YYNY"
    print(Solution().bestClosingTime(customers=customers))