    scores = [ float(input()) for i in range(3) ]
    weight = [2, 3, 5]
    print('MEDIA = {:.1f}'.format(  ( (scores[0] * weight[0]) + (scores[1] * weight[1]) + (scores[2] * weight[2]) ) / sum(weight) ))
