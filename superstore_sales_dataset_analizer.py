# sector-1,data understanding
total_data_row=0
count=0
seen=set()
unique_data=[]
# earning and sels,sector-2
total_sales_amount=0
total_profit=0 
catagory_wise_sales={}
max_catagory=""
max_sales_of_catagory=0
# Basic analysis ,sector-3
year_wise_sales={}
best_year_of_sales=""
max_sales_of_year=0
# for month
month_wise_sales={}
best_month_of_sales=""
max_sales_of_month=0
# business insights ,sector-4
catagory_wise_profit={}
max_profit=0
best_catagory_profit=""
region_wise_sales={}
max_region_sales=0
best_region=""
with open("superstore.csv","r",encoding="latin-1") as file:
    header=file.readline()
    next(file)
    
    for i,line in enumerate(file):
                 
        total_data_row+=1
        data=line.strip().split(",")
        row_tuple=tuple(data)
        if row_tuple not in seen:
              seen.add(row_tuple)
              unique_data.append(data)
        try:
            sales=float(data[17])
            total_sales_amount+=sales
        except:
            pass
        #  total_profit
        try:
            profit=float(data[20])
            total_profit+=profit
        except:
            pass
        catagory=data[14]
        try:
           sales=float(data[17])
           if catagory in catagory_wise_sales:
               catagory_wise_sales[catagory]+=sales
           else:
               catagory_wise_sales[catagory]=sales
        except:
            pass
        for c in catagory_wise_sales:
            if catagory_wise_sales[c]>max_sales_of_catagory:
                max_sales=catagory_wise_sales[c]
                max_catagory=c
        order_data=data[2]
        year=order_data.split("/")[-1]
        try:
            sales=float(data[17])

            if year in year_wise_sales:
                year_wise_sales[year]+=sales
            else:
                year_wise_sales[year]=sales
        except:
            pass
        for y in year_wise_sales:
            year_wise_sales[y]>max_sales_of_year
            max_sales_of_year=year_wise_sales[y]
            best_year_of_sales=y
        order_data=data[2]
        month=order_data.split("/")[0]
        # calculating of months
        try:
            sales=float(data[17])
            if month in month_wise_sales:
                month_wise_sales[month]+=sales
            else:
                month_wise_sales[month]=sales
        except:
             pass
        for m in month_wise_sales:
           if month_wise_sales[m]>max_sales_of_month:
              max_sales_of_month=month_wise_sales[m]
              best_month_of_sales=m
        # catagory wise profit
        catagory=data[14]
        try:
            profit=float(data[20])
            if catagory in catagory_wise_profit:
                catagory_wise_profit[catagory]+=profit
            else:
                catagory_wise_profit[catagory]=profit
        except:
            pass
        for c in catagory_wise_profit:
            catagory_wise_profit[c]>max_profit
            max_profit=catagory_wise_profit[c]
            best_catagory_profit=c
        region=data[9]
        try:
            sales=float(data[17])
            if region in region_wise_sales:
                region_wise_sales[region]+=sales
            else:
                region_wise_sales[region]=sales
        except:
            pass
        for r in region_wise_sales:
            if region_wise_sales[r]>max_region_sales:
                max_region_sales=region_wise_sales[r]
                best_region=r

                       
print("=======Understanding the overall data=======")
print(header)
print(f"total row of the datasets are {total_data_row}")
print(f"total clean rows are{len(unique_data)}")
print("=======Understanding earning and sales data=======")
print(f"total amount of earning {round(total_sales_amount,2)}")
print(f"total amount of profit {round(total_profit,2)}")
for c in catagory_wise_sales:
    print(c,int(catagory_wise_sales[c]))
print(f"top catagory is :{max_catagory} ")
print(f"top sales is :{round(max_sales,2)} ")
print("=======Basic analysis =======")
print("sales of every year===")
for y in year_wise_sales:
    print(y,int(year_wise_sales[y]))
print("Max sales year===")
print(f"best year of sales is : {best_year_of_sales}")
print(f"max sales of year is : {max_sales_of_year}")
for m in month_wise_sales:
    print(m,int(month_wise_sales[m]))
print("Max sales month===")
print(f"best month of sales is : {best_month_of_sales}")
print(f"max sales of month is : {round(max_sales_of_month,2)}")
print("======= Bussiness insight =======")
print(f"most profitable catagory is: {best_catagory_profit}")
print(f"max profit is :{round(max_profit,2)}")
print(f"most sales region is: {best_region}")
print(f"max sales is :{round(max_region_sales,2)}")

