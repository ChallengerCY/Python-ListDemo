#一个索引示例
#根据给定的年月日以数字的形式打印出日期
months=["January",
       "February",
       "March",
       "April",
       "May",
       "June",
       "July",
       "August",
       "September",
       "October",
       "November",
       "December"
       ]
#以1~31的数字作为结尾的列表,外历开始时前三天为st nd rd，从21 22 23的后缀也为st nd rd
ending=['st','nd','rd']+17*['th']\
       +['st','nd','rd']+7*['th']\
       +['st']

year=input("Year: ")
month=input("Mounth[1-12]: ")
day=input("Day[1-31]: ")

month_number=int(month)
day_number=int(day)

#记得将月和天数减1，获取正确索引
mounth_name=months[month_number-1]
ordinal=day+ending[day_number-1]

print(mounth_name+" " +ordinal+"."+year)



