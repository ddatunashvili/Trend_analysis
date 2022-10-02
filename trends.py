import pandas as pd      
from datetime import date
from pytrends.request import TrendReq

# init
py_trends = TrendReq()

# keyword list  5 is limit

keywords = ["Python","Javascript","Kotlin"]
# keywords = [keywords[-1]]

timeframes = ["today 1-m","today 3-m","today 12-m","today 5-y"]
# timeframes = [timeframes[-1]]



def check_trends(keyword,timeframe):
	
	# keywords, category, time, location,
	py_trends.build_payload(kw_list = [keyword], cat='0', timeframe = timeframe,  geo="GE", gprop="")
	df = py_trends.interest_over_time()

	# საშუალოდ რამდენია ტრენდულობა დროის დიაპაზონში
	average = round(df[keyword].mean(),2)
	
	
	# samples = len(df[keyword])-int(len(df[keyword])/2)
	# samples = -52 და 52 [-52:] [:52]

	# როგორ შეიცვალა ტრენდულობა საშუალო მაჩვენებელთან მიმართებაში
	avg = round(df[-52:][keyword].mean(),2)
	avg2 = round(df[:52][keyword].mean(),2)

	print(keyword," მონაცემების რაოდენობა: ", len(df[keyword]))
	print("-------------")
	print(f"{timeframe} - პერიოდში საშუალო ტრენდულობა  {average}")
	print(f"ტრენდულობა წინა წელს {avg} ")
	print(f"ტრენდულობა ბოლო წელს {avg2} ")
	print("-------------")

	# პროცენტული ცვლილება	

	dif = round(((avg/average)-1)* 100, 2)
	dif2 = round(((avg2/average)-1)* 100, 2)
	dif3 = round(( (avg2-avg)/avg)*100, 2)
	
	if str(dif)[0] != "-" :
		dif = f"+{dif}"
	if str(dif2)[0] != "-":
		dif2 = f"+{dif2}"
	if str(dif3)[0] != "-":
		dif3 = f"+{dif3}"

 	# საშუალო ინდექსის მიხედვით
	print(f"ცვლილება წინა წელს {dif}%")
	print(f"ცვლილება ბოლო წელში {dif2}%")

	# პროცენტული ცვლილება რიცხვების
	print(f"ცვლილება წინა წელთან შედარებით  {dif3}%")
	print("-------------")


print("ტრენდები საქართველოში: \n")
for kw in keywords:
	for timeframe in timeframes:
		try:
			check_trends(kw,timeframe)
		except:
			print(f"'{kw}' - {timeframe} : !no data")
	