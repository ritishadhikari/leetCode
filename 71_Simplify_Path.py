class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        last=None
        sentenceContinued=False
        firstDotInclude=True
        for i,k in enumerate(path):
            if k=="/":
                firstDotInclude=True
                if last==k or (last=="." and stack[-1]!="."):
                    last=k
                    continue
                else:
                    stack.append("/")
                last=k
            
            elif k==".":
                    if last==k:
                        if (len(path)-1>=i+1 and path[i+1]!="/") or sentenceContinued:
                            if (len(path)-1>=i+1 and path[i+1]!="/"):
                                if firstDotInclude:
                                    stack.append(last)
                                    firstDotInclude=False
                                stack.append(k)
                                sentenceContinued=True
                            elif sentenceContinued:
                                stack.append(k)
                                sentenceContinued=False
                        elif stack[-1]==".":  # if the last . is a continuation with the sentences
                            stack.append(k)
                        elif len(stack)>1 and stack[-1]=="/":  # go back to the parent directory
                            stack.pop()
                            while stack[-1]!="/":
                                stack.pop()
                        elif last!=".":  # . is accompanied by other characters
                            stack.append(k)
                    elif last!="/":  # ex /f/j.
                        stack.append(k)
                        firstDotInclude=False
                    last=k
            else:
                if stack:  # not for situations when the letters starts before /
                    if last=="." and firstDotInclude:
                        stack.append(last)  
                        firstDotInclude=False
                    stack.append(k)
                last=k

        if len(stack)>1:
            return "".join(stack[:-1]) if stack[-1]=="/" else "".join(stack)
        else:
            return stack[-1]


if __name__=="__main__":
    # path =  "/a//b////c/d//././/.."
    path="/...."
    path="/hello../world"
    # path="/..aa/...hidden...sweet"
    # path='/...'
    # path="/a/./b/../../c/"
    path="/../..ga/b/.f..d/..../e.baaeeh./.a"

    print(Solution().simplifyPath(path=path))