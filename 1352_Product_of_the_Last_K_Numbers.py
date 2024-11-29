# VVI
class ProductOfNumbers:

    def __init__(self):
        # Initialize 1 even before adding any non existant number
        self.lst=[1]
        

    def add(self, num: int) -> None:
        if num!=0:
            # The value will contain the last product of the last multiplication
            # The First index value will always contain 1 for a non-existant number
            self.lst.append(self.lst[-1]*num)
        else:
            # If Zero arrives, it's back to 1
            self.lst=[1]
        return None
        

    def getProduct(self, k: int) -> int:
        # what if the last k is greater than the total added value
        # gt because the first value will contain 1 for a non-existant number
        if k>=len(self.lst):
            return 0
        else:
            # divide by the so far multiplication by the multiplication value
            # position we don't need
            return self.lst[-1]//self.lst[-k-1]

if __name__=="__main__":
    m=ProductOfNumbers()
    print(m.add(num=3))
    print(m.add(num=0))
    print(m.add(num=2))
    print(m.add(num=5))
    print(m.add(num=4))
    print(m.getProduct(k=2))
    print(m.getProduct(k=3))
    print(m.getProduct(k=4))
    print(m.add(num=8))
    print(m.getProduct(k=2))