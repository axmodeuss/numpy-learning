import pandas as pd
drivers=pd.DataFrame({"DriverID":[101,102,103,104],
    "Driver":["Ali","Sara","Reza","Bahar"],
    "City":["Tehran","Shiraz","Tehran","Mashhad"],
    "Rate":[4.8,4.9,4.5,4.7]})

passengers=pd.DataFrame({"PassengerID":[1,2,3,4,5,6],
    "Passenger":["Amir","Nima","Maryam","Sina","Parsa","Haniyeh"]})

trips=pd.DataFrame({ "TripID":[1001,1002,1003,1004,1005,1006],
    "DriverID":[101,102,101,103,104,102],
    "PassengerID":[1,2,3,4,5,6],
    "Distance":[12,8,15,5,20,10],
    "Duration":[25,18,30,12,40,20],
    "Fare":[180000,120000,250000,90000,320000,150000],
    "Status":["Done","Done","Done","Canceled","Done","Done"],
    "Date":[
        "2025-06-01",
        "2025-06-02",
        "2025-06-03",
        "2025-06-04",
        "2025-06-05",
        "2025-06-06"
    ]})

payments=pd.DataFrame({"TripID":[1001,1002,1003,1004,1005,1006],
    "PaymentMethod":[
        "Online",
        "Cash",
        "Online",
        "Cash",
        "Online",
        "Online"
    ]})

df=pd.merge(trips,drivers,on="DriverID")
df=pd.merge(df,passengers,on="PassengerID")
df=pd.merge(df,payments,on="TripID")

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

df["PricePerKM"] = (
    df["Fare"] / df["Distance"]
).round(0)

df["AverageSpeed"] = (
    df["Distance"] / (df["Duration"] / 60)
).round(2)

print("========== Final Table ==========")
print(df)

print("\n========== Total Revenue ==========")
print(df[df["Status"]=="Done"]["Fare"].sum())

print("\n========== Revenue By Driver ==========")
print(
    df[df["Status"]=="Done"]
    .groupby("Driver")["Fare"]
    .sum()
)

print("\n========== Trips By Driver ==========")
print(
    df.groupby("Driver")["TripID"].count()
)

print("\n========== Average Driver Rating ==========")
print(
    df.groupby("Driver")["Rate"].mean()
)

print("\n========== Revenue By City ==========")
print(
    df[df["Status"]=="Done"]
    .groupby("City")["Fare"]
    .sum()
)

print("\n========== Average Fare ==========")
print(df["Fare"].mean())

print("\n========== Longest Trip ==========")
print(df.loc[df["Distance"].idxmax()])

print("\n========== Fastest Trip ==========")
print(df.loc[df["AverageSpeed"].idxmax()])

print("\n========== Online Payments ==========")
print(df[df["PaymentMethod"]=="Online"])

print("\n========== Canceled Trips ==========")
print(df[df["Status"]=="Canceled"])

print("\n========== Monthly Revenue ==========")
print(
    df[df["Status"]=="Done"]
    .groupby("Month")["Fare"]
    .sum()
)

print("\n========== Best Driver ==========")
best = (
    df[df["Status"]=="Done"]
    .groupby("Driver")["Fare"]
    .sum()
    .idxmax()
)

print(best)

print("\n========== Statistics ==========")
print(df.describe())

print("\n========== Sorted By Revenue ==========")
print(df.sort_values(by="Fare", ascending=False))

df.to_csv("taxi_app_report.csv", index=False)