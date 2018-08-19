from bs4 import BeautifulSoup

text = '''<p style="color: grey;">Last Updated: <b>18/8/2018 12:53 pm</b></p><p>Item and quantity: <b>Bath Soap 10 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:58 pm</b></p><p>Item and quantity: <b>Blankets 100 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:55 pm</b></p><p>Item and quantity: <b>Broom 10 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>19/8/2018 2:19 pm</b></p><p>Item and quantity: <b>Dal (Paripp) 10 Kg</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:54 pm</b></p><p>Item and quantity: <b>Detergents 10 Kg</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:53 pm</b></p><p>Item and quantity: <b>Dish Washing Soaps 10 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:57 pm</b></p><p>Item and quantity: <b>Dress - Kids 40 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:57 pm</b></p><p>Item and quantity: <b>Dress - Ladies 40 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:56 pm</b></p><p>Item and quantity: <b>Floor Cleaning Liquid 10 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:58 pm</b></p><p>Item and quantity: <b>Mats 20 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:54 pm</b></p><p>Item and quantity: <b>Toilet Cleaning Brush 10 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:55 pm</b></p><p>Item and quantity: <b>Toilet Cleaning Liquid 10 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:57 pm</b></p><p>Item and quantity: <b>Undergarments - Gents 40 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:56 pm</b></p><p>Item and quantity: <b>Undergarments - Kids 20 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:56 pm</b></p><p>Item and quantity: <b>Undergarments - Ladies 20 Piece</b></p><hr>
.'''

soup = BeautifulSoup(''.join(text))
for i in soup.prettify().split('<hr/>'):
    soup_temp = BeautifulSoup(''.join(i))
    x = soup_temp.find_all('p')
    for each_elem in x:
        print each_elem.getText().strip()
    print '~' * 30
