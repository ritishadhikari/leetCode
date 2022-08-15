from collections import defaultdict,deque
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A=0
        B=0
        secretDict=defaultdict(lambda:[])
        for ind,char in enumerate(secret):
            if char!=guess[ind]:
                if char not in secretDict.keys():
                    secretDict[char]=deque([ind])
                else:    
                    secretDict[char].append(ind)
                
        for ind,char in enumerate(guess):
            if char==secret[ind]:
                A+=1
            else:
                if secretDict[char]:
                    secretDict[char].popleft()
                    B+=1

        return f"{A}A{B}B"

if __name__=="__main__":
    secret = "1045545335509558631345133806867219625479089318214875331847060388890241610586383849872176523794752755232498955910250557589908538624239355588517795111014392917276852468645624811776332002397796898975563178443619012579502488588618915436443075951029876193330577558124699837205303900058211529562175535211712318016281429680446271980986785270267527924370851392730174819202906496168499130676382868930632296222054238116318902171700649493886411330274182343857153265954296075878864231173018783255648080850988662006118586672319262998553399871024070631155875518768366536152899686667029733758731517096766599301487904003153800452133835480645253722055515339251760159585743362365765108804734843873874649703908138053844487314996911792702271949041358289441206871371082303363215061116829685559087412255313515536780919128326836868006434385721857904252531494635500086590480901931769480481003848463636943654599650754476324834645902658201455100405966357212724648915004797672559433879041653546077895815788973375525709931265007"
    guess = "7944111028932650517278656591040793189204661375299757743412228994993171347159512637475677286176069210003116624446580250122547903071615202426189941332264927710535887278271315790317684614973945434258797726017098782128280384399634504559698319915396107182768892668200608529576551599567338622598058922144633635167083559555175693037859345011900598567024875850782819874192001771859996700900647477250875024811207206485600913147184908158537008306526928208829675998677675731510630615887394164982351878305594130998547606694376653944581862385250258388877489303675567973772619202961177740546740075553417098899379153777007122298174847357265279746625676670836072538835520709387565995291618011994772375271243665612541383071997076728790178631079407898481858368004020784215173083568810236193842122855247114891967619195885263387723597266755797542700037324377047256335208007033923810464028090038106136434899629609280180888817573114360931907261135392932853593354860959442890959631958285909879113594006278416575494603366515"
    # secret="1123"
    # guess="0111"
    print(Solution().getHint(secret=secret,guess=guess))