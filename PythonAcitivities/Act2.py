tot_sales = {}

x = 0; y = 0

while True:

    snum = int(input('Salesman Number: '))
    sname = input('Salesman Name: ')

    firstq = float(input("First Quarter: "))
    secondq = float(input("Second Quarter: "))
    thirdq = float(input("Third Quarter: "))
    fourthq = float(input("Fourth Quarter: "))

    tot_sales.update({'Salesman Number': snum, 'Salesman Name': sname,
                  'First Quarter': firstq, 'Second Quarter': secondq, 'Third Quarter': thirdq, 'Fourth Quarter': fourthq})
    tot_sales.update(tot_sales)

new_rec = input("New Record: ").strip().lower()
if new_rec != 'Yes':
    print("Salesman Number: %d" % (snum))
    print("Salesman Name: %s" % (sname))
    print("Salesman Number: %.2f" % (firstq))
    print("Salesman Number: %d" % (snum))
else:






