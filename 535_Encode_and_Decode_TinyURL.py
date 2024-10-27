import random
class Codec:
    def __init__(self):
        self.str2enc={}
        self.enc2str={}
        self.potentialEncoders="abcdefghijklmnopqrstuvwxyz"
    def decode(self,shortUrl:str) ->str:
        # Only take in the 6 letters after https://tinyurl.com/
        # from the enc2str dict and return the same
        return self.enc2str[shortUrl[-6:]] if shortUrl[-6:] in self.enc2str else None
    
    def encode(self,longUrl:str) -> str:
        # Only Enter the Loop only if the string has never been encoded before
        # And Hence encode the string into 6 characters 
        # Eventually append it with https://tinyurl.com/ 
        while longUrl not in self.str2enc:
            # only encode with letters and not any special characters
            # and hence we use self.potentialEncoders and not the 
            # longurl which may consist of special characters
            encoded="".join(random.choices(population=self.potentialEncoders,k=6))
            # the encoded word should not be a duplicate either which has 
            # been used to encode other strings
            if encoded not in self.enc2str:
                self.str2enc[longUrl]=encoded
                self.enc2str[encoded]=longUrl
        return "https://tinyurl.com/"+self.str2enc[longUrl]


if __name__=="__main__":
    codec=Codec()
    
    print("For The Times of India Url")
    decodedLink=codec.encode(longUrl="https://www.timesofindia.com")
    print(decodedLink)
    encodedLink=codec.decode(shortUrl=decodedLink)
    print(encodedLink)
    print("-----------------------------")
    print("For HDFC Bank Url")
    decodedLink2=codec.encode(longUrl="https://www.hdfcbank.com")
    print(decodedLink2)
    encodedLink2=codec.decode(shortUrl=decodedLink2)
    print(encodedLink2)
