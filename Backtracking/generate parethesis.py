def generateparenthesis(n):
    if n==0:
        return []
    if n==1:
        return ["()"]
    res=[]
    def generate(s,open,close):
        open='('
        close=')'
