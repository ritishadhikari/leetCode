class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive=timeToLive
        self.tokenDict={}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenDict[tokenId]=currentTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokenDict:
            lastTime=self.tokenDict[tokenId]
            if currentTime-lastTime<self.timeToLive:
                self.tokenDict[tokenId]=currentTime
        

    def countUnexpiredTokens(self, currentTime: int) -> int:  # this one is difficult
        
        fil=filter(lambda l: currentTime-l[1]<self.timeToLive, self.tokenDict.items())
        a=list(fil)
        return len(a)

      
        
if __name__=="__main__":
    obj = AuthenticationManager(timeToLive=5)
    print(obj.renew(tokenId="aaa",currentTime=1))
    print(obj.generate(tokenId="aaa",currentTime=2))
    print(obj.countUnexpiredTokens(currentTime=6))
    print(obj.generate(tokenId="bbb",currentTime=7))
    print(obj.renew(tokenId="aaa",currentTime=8))
    print(obj.renew(tokenId="bbb",currentTime=10))
    print(obj.countUnexpiredTokens(currentTime=15))
    
    