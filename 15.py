for i in range(0,12,1):
    angle1=(90-0*30+(i*30)-(i*2.5))
    print(angle1%360)
print()
for i in range(0,12,1):
    angle1=(90-1*30+(i*30)-(i*2.5))
    print(angle1%360)
print()
for i in range(0,12,1):
    angle1=(90-2*30+(i*30)-(i*2.5))
    print(angle1%360)
print()


''' the changes:
90
60
30
(90,0,-30) = i value

0
30
60
(0, 90, +30)

0
1
2

(0,3,1)'''

