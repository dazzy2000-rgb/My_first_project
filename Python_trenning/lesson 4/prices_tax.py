# if prices in ILS ADD 18% TAX
#     if prices in $ add 20% TAX
#     the result in 2 lists

prices = ['45$', '80$','40ILS', '95$','34$','100ILS']
prices_ILS=[]
prices_usd=[]
for price in prices:
    if '$' in price:
        price = price.replace('$', '')
        price_as_int= int(price)
        price_with_tax=price_as_int*1.2
        prices_usd.append(price_with_tax)
        print(f'{price_with_tax}$')
    elif 'ILS' in price:
        price = price.replace('ILS', '')
        price_as_int= int(price)
        price_with_tax=price_as_int*1.18
        prices_ILS.append(price_with_tax)
        print(f'{price_with_tax}ILS')
    else:
        print(f' price with tax its not value')
price_str=str(prices)

