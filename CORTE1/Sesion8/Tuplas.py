
def app(a,*args,**kwargs):
    print(args)
    print(kwargs)

if __name__=="__main__":
    app(1,2,5,7,9,x=1,b=2)