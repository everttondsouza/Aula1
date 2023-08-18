car_stock = {'BMW X6':[5], 'BMW I5':[0], 'BMW I8':[3]}

car_desire = input('Informe carro desejado: ')

if car_desire in car_stock:
    availability = car_stock[car_desire][0]
    if availability > 0:
        print(f'O carro {car_desire} esta dísponivel e contém {availability} em estoque')
    else:
        print('Desculpe, este carro não está dísponivel')