scores = [ float(i) for i in input().split() ]
weight = [2, 3, 4, 1]

average = ((scores[0]*weight[0]) + (scores[1]*weight[1]) + (scores[2]*weight[2]) + (scores[3]*weight[3])) / 10
print('Media: {:.1f}'.format(average))
if average >= 7:
    print('Aluno aprovado.')
elif average < 5:
    print('Aluno reprovado.')
elif average >= 5 and average < 7:
    print('Aluno em exame.')
    exam = float(input())
    print('Nota do exame: {:.1f}'.format(exam))
    if (exam + average) / 2 >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format((exam + average) / 2))
