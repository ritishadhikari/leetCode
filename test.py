import collections
class WordDictionary(object):
    def __init__(self):
        self.word_dict = collections.defaultdict(list)
        

    def addWord(self, word):
        if word:
            self.word_dict[len(word)].append(word)
    
    def search(self, word):
      if not word:
          return False
          
      if '.' not in word:
          return word in self.word_dict[len(word)]
          
      for w in self.word_dict[len(word)]:
          success = True
          for index, ch in enumerate(word):
              if ch != w[index] and ch != '.':
                  success = False
                  break
              
           if success:
              return True
      return False
    

if __name__=="__main__":
    obj=WordDictionary()
    obj.addWord(word="bad")
    obj.addWord(word="dad")
    obj.addWord(word="mad")
    obj.search(word="pad")
    obj.search(word="bad")
    obj.search(word=".ad")
    obj.search(word="b..")