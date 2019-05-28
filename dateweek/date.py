
import datetime
n = datetime.datetime.now()

monday=1
tuesday=2
wednesday=3
Thursday=4
friday = 5
saturday=6
sunday=7

today = n.isocalendar()[2]

#print(today)
print("내일 day : ", n+datetime.timedelta(days=1))
print("모래 day : ", n+datetime.timedelta(days=2))
#print(n.isocalendar()[0])
print("다음주 요일 : ", n+datetime.timedelta(weeks=1,days=(sunday-today)))
print("week count : ", n.isocalendar()[1])
print("day count : ", n.isocalendar()[2])

