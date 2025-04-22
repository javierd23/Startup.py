score = input('enter a number: ')
try:
    sc = float(score)
except:
    print('This is an invalid enter!')
    quit()

if sc >= 0.90:
    print('A')
elif sc >= 0.80:
    print('B')
elif sc >= 0.70:
    print('C')
elif sc >= 0.60:
    print('D')
elif sc < 0.60:
    print('E')