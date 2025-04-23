#this is a pay rate calculated by amount of the hours * by the rate and after 40 it will add %1.5 to the hrs.

def computepay():
    h = input('enter a number')
    r = input('enter a number')
    hs = float(h)
    rs = float(r)

    if hs > 40:
        ehs = (hs - 40)
        rht = (hs - ehs) * rs
        pr =   ((ehs * rs) * 1.5)
        prt = rht + pr
        return prt
    else:
        return hs * rs

result = computepay()
print('Pay rate', result)









