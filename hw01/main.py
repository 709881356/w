for i in range(1,10):
    for j in range(i,10):
        formula='{0:1}*{1:1}={2:<2}'.format(i,j,i*j)
        print(formula,end=' ')
    print()
    for k in range(0,i):
        print(end='       ')
