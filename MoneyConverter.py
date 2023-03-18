#Foreign currncy to indian rupees coverter
c=input("Enter Country Name:")
print()
m=int(input("Enter a amount:"))
if c=="USA" or c=="United State of America" or c=="America" or c=="america":
    currency="Dollar"
elif c=="UK" or c=="United Kingdom" or c=="uk":
    currency="Pound"
elif c=="Australia" or c=="australia":
    currency="Australian Dollar"
elif c=="Russia" or c=="russia":
    currency="Ruble"
elif c=="China" or c=="china":
    currency="Yuan"
elif c=="Canada" or c=="canada":
    currency="canadian Dollar"
elif c=="New Zealand":
    currency="New Zealand Dollar"
elif c=="Germany" or c=="germany":
    currency="Euro"
elif c=="South Africa" or c=="south africa":
    currency="Rand"

print()
if c=="USA" or c=="United State of America" or c=="America" or c=="america":
    print(m,currency,"is",m*82.74,"Indian Rupees")
elif c=="UK" or c=="United Kingdom" or c=="uk":
    print(m,currency,"is",m*100.44,"Indian Rupees")
elif c=="Australia" or c=="australia":
    print(m,currency,"is",m*58.12,"Indian Rupees")
elif c=="Russia" or c=="russia":
    print(m,currency,"is",m*1.17,"Indian Rupees")
elif c=="China" or c=="china":
    print(m,currency,"is",m*12.19,"Indian Rupees")
elif c=="Canada" or c=="canada":
    print(m,currency,"is",m*61.63,"Indian Rupees")
elif c=="New Zealand":
    print(m,currency,"is",m*53.18,"Indian Rupees")
elif c=="Germany" or c=="germany":
    print(m,currency,"is",m*89.50,"Indian Rupees")
elif c=="South Africa":
    print(m,currency,"is",m*4.80,"Indian Rupees")
else:
    print("oops! \n Country name is not registered")







