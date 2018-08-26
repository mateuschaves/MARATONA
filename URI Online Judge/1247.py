import math

while True:
    try:
        data = input().split()
        data = [ int(i) for i in data ]
        df, vf, vg = data
        dg = math.sqrt( 144 + df**2 )
        if ( dg / vg ) > ( 12 / vf ):
            print('N')
        else:
            print('S')
    except EOFError:
        break
