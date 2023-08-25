def factorial1(x):
    a=1
    for i in range(x):
        a=a*(i+1)
    return a

if __name__=="__main__":
    a=factorial1(5)
    print(f'resultado {a}')