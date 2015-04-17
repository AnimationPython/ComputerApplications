teachers = ["Tom", "Jonny", "Pla", "Priyanka", "Will", "Jian"]

print len(teachers)
print teachers[2]

teachers.append("Ivonne")
print len(teachers)
print teachers

teachers.insert(0, "John")


print len(teachers)
print teachers

teachers.remove("John")

print len(teachers)
print teachers


teachers.pop(3)
print teachers

print "%s is a good teacher!" % teachers[0]
print "%s is a good teacher!" % teachers[1]
print "%s is a good teacher!" % teachers[2]
print "%s is a good teacher!" % teachers[3]
print "%s is a good teacher!" % teachers[4]
print "%s is a good teacher!" % teachers[5]


for n in teachers:
    print "%s is a teacher!" % n

for x in range(999999999):
    print "2 times %d is %d" % (x, x*2)
total = 0
for y in [7,49,210]:
    total = total+y
    total = total+y
    print total
print total
    


    
