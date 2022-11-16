print("Split Paying Program")
print("Made by Hwan")
print("============")
print("How many people paying?:", end=" ")
peoplePaying=int(input())
print("names?")
namesList=[]
pricesList=[]
for i in range(peoplePaying):
    print("name", i+1, ": ",end=' ')
    namesList.append(input())
    print("How much did you pay? :",end= ' ')
    pricesList.append(int(input()))
print("Total Amount:",sum(pricesList), "wons")
pricePerPerson=int(sum(pricesList)/peoplePaying)
print("Each person has to pay", pricePerPerson, "wons")

zipped=zip(namesList,pricesList)
zipped=sorted(zipped, key=lambda x: abs(x[1]-pricePerPerson))

for i in range(len(pricesList)):
    if pricesList[i]>= pricePerPerson:
        continue
    moneyPaying=pricePerPerson-pricesList[i] #moneyPaying은 내야할 돈
    for j in range(len(pricesList)):
        if moneyPaying==0:
            break
        if pricesList[j]>pricePerPerson:
            moneyNeeded=pricesList[j]-pricePerPerson #moneyNeeded는 받아야 할 돈
            if moneyPaying>=moneyNeeded:
                pricesList[i]+=moneyNeeded
                pricesList[j]-=moneyNeeded
                moneyPaying-=moneyNeeded
                print(namesList[i],": Pay", moneyNeeded, "wons to", namesList[j])
            else:
                pricesList[i]+=moneyPaying
                pricesList[j]-=moneyPaying
                print(namesList[i],": Pay", moneyPaying, "wons to", namesList[j])
                moneyPaying=0
            
             
        
