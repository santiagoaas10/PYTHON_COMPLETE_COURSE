cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print(f"stopping the prod line, this car is {status}")
        break
    print(f"this car is {status}")


print('----------')
print('----------')
print('----------')
i=0
for status in cars:
    if status == "faulty":
        print(f"skipping this car number {i} shipment because it is {status}")
        continue
    print(f"shipping car number {i}, status is {status}")
    i+=1