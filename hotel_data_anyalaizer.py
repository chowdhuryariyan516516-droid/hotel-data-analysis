# sector-1, data cleaning and preparation
children_null=0
agent_null=0
country_null=0
seen=set()
unique_data=[]
# sector-2, Revenue
total_revenue=0
city_revenue=0
resort_revenue=0
total_booking=0
total_cancel=0
# sector-3,
month_wise_booking={}
month_wise_cancel={}
month_wise_cancelation_rate={}
# sector_4, top insight

with open("hotels.csv","r") as file:
    # first_line=file.readline()
    # print(first_line)
    next(file)

    for i,line in enumerate(file):
        data=line.strip().split(",")
        childern=data[10]
        if childern=="" or childern=="NULL":
            children_null+=1
        agent=data[21]
        if agent=="" or agent=="NULL":
            agent_null+=1
        country=data[13]
        if country=="" or country=="NULL":
            country_null+=1
            data[13]="UNKNOWN"
        row_tuple=tuple(data)
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_data.append(data)
            # revenue count
        stays=int(data[8])
        adr=float(data[27])
        revenue=stays*adr
        total_revenue+=revenue
        
        hotel_type=data[0]
        if hotel_type=="City Hotel":
            city_revenue+=revenue
        else:
            resort_revenue+=revenue
        # total booking and cancel
        is_canceled=data[1]
        total_booking+=1
        # if is_canceled=="1":
        #     total_cancel+=1
            # month_wise_booking
        month=data[4]
        if month in month_wise_booking:
            month_wise_booking[month]+=1
        else:
            month_wise_booking[month]=1
            # month_wise_cancel
        if is_canceled=="1":
            total_cancel+=1
            if month in month_wise_cancel:
                 month_wise_cancel[month]+=1
            else:
                 month_wise_cancel[month]=1
        

        

cancelation_rate=(total_cancel/total_booking)*100
max_booking_month=max(month_wise_booking,key=month_wise_booking.get)
max_cancel_month=max(month_wise_cancel,key=month_wise_cancel.get)
# max_cancel_rate_month=max(,key=month_wise_cancel.get)
         
print(f"the number of null children :  {children_null}")
print(f"the number of null agent :  {agent_null}")
print(f"the number of null country :  {country_null}")
print(f"total clean rows: {len(unique_data)}")
print("=========This is the analaysis of revenue==========") 
print(f"total revenue is : {round(total_revenue,2)}")
print(f"The revenue of city hotel is{round(city_revenue,2)} ")
print(f"The revenue of resort hotel is{round(resort_revenue,2)} ")
print(f"total booking is: {total_booking}")
print(f"total cancel is: {total_cancel}")
print(f"the rate of cancellation is : {cancelation_rate}")



print("=========This is the analaysis of revenue==========") 
print("===========Month wise booking ==========")
for m,b in month_wise_booking.items():
            print(f"{m:<10}:{b}")
print("===========Month wise cancel ==========")
for m,c in month_wise_cancel.items():
            print(f"{m:<10}:{c}")
print("===========Month wise cancellation rate ==========")
for m in month_wise_booking:
     booking=month_wise_booking[m]
     cencel=month_wise_cancel.get(m,0)

     rate=(cencel/booking)*100

     print(f"{m:<10}:{round(rate,2)}")
     month_wise_cancelation_rate={}
     month_wise_cancelation_rate[m]=rate
     max_month_wise_cancelation_rate=max(month_wise_cancelation_rate,key=month_wise_cancelation_rate.get)

print("=======top months of cancelation and booking========")
print(f"highest month of booking is {max_booking_month}")
print(f"highest month of cancelation is {max_cancel_month }")
print(f"highest month of cancelation rate is {max_month_wise_cancelation_rate[]}")

        
        
        
        