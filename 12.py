
money=eval(input("請輸入你的本金:"))
rate = (eval(input("請輸入你的年利率(如 1.23 = 1.23%):")) / 100)
year = eval(input("請入期數(年):"))
if (money > 0) and (rate > 0) and (year > 0) :
for i in range(1,year+1) :
   total = money * ((1 + rate)**i)
   print("你第 {0} 年的本利和為: {1:.2f}".format(i,total))
else :
   print("☢☢☢ 輸入有誤,無法計算 ☢☢☢")
if money <= 0 :
   print("你本金輸入 {0} 錯誤!".format(money))
if rate <= 0 :
   print("你年利率輸入 {0} 錯誤!".format(rate*100))
if year <= 0 :
   print("你期數輸入 {0} 錯誤!".format(year))
