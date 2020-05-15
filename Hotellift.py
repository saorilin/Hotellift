'''2018.03.06.          11              3              0
    idopont[0]     kartyaszam[1]     indulo[2]     celszint[3]
'''
with open('lift.txt','r') as f:
    lift = []
    for each in f:
        lift.append(each.strip('\n').split(' '))
length = len(lift)
#3.feladat
print('3. feladat: Osszes lifthasznalat:',length)

#4.feladat
oldest_datum = lift[0][0]
newest_datum = lift[length-1][0]
print('4. feladat: Idoszak: %s - %s' % (oldest_datum,newest_datum))

#5.feladat
max_celszint = '0'
for each in lift:
    if each[3] > max_celszint:
        max_celszint = each[3]
print('5. feladat: Celszint max: %s' % max_celszint)

#6.feladat
print('6. feladat:')
try:
    karszamInt = int(input('\tKartyaszam:'))
    celszintInt = int(input('\tCelszint:'))
    karszamStr = str(karszamInt) 
    celszintStr = str(celszintInt)
except:
    karszamStr = '5'
    celszintStr = '5'
    print('\tbad type entered')
    
#7.feladat
flag = 0
print('7. feladat',end='')
for each in lift:
    if each[1] == karszamStr and each[3] == celszintStr:
        flag = 1
        break
if flag:
    print('A(z) %s.Kartyaval utaztak a(z) %s. emeletre' % (karszamStr,celszintStr))
else:
    print('A(z) %s.Kartyaval nem utaztak a(z) %s. emeletre' % (karszamStr,celszintStr))
    
#8.feladat
Statisztika = {}
for each in lift:
    Statisztika.setdefault(each[0],0)
for each in lift:
    Statisztika[each[0]] += 1
print('8. feladat:Statiszika')
for each in Statisztika:
    print('\t%s - %sx' % (each,Statisztika[each]))
    
    
    
    
    
    
    
    
    
    
    
    