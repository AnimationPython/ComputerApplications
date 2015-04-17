print 'Hi'
Teachers = [ 'Rikki' , 'Yvonne' , 'Jain' , 'Jonny' , 'Tom' , 'Pla' , 'Priyanka' , 'Will' ]
print Teachers
print len(Teachers)
print Teachers[0:2]
Teachers.append('Chris')
print Teachers
print Teachers.index('Tom')
Teachers.insert(2,'John')
print Teachers
Teachers.remove('Rikki')

# print Teachers
# print Teachers[0] + ' is a good teacher'
# print Teachers[1] + ' is a good teacher'
# print Teachers[2] + ' is a good teacher'
# print Teachers[3] + ' is a good teacher'

for Teacher in Teachers:
    print Teacher + ' is a great teacher'
for x in range(101):
    print str(x) + ' when multiplied by 5 =' + str(5*x)
 
