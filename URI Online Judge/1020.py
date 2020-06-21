# -*- coding: utf-8 -*-

daysAmount = int(input())

years = int(daysAmount / 365)

mounths = int(( daysAmount % 365 ) / 30)

days = int( ( daysAmount % 365 ) % 30 )

print('{} ano(s)'.format(years))
print('{} mes(es)'.format(mounths))
print('{} dia(s)'.format(days))