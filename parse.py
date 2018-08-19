from bs4 import BeautifulSoup
import pprint
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
import pandas as pd

pp = pprint.PrettyPrinter()
text = '''<p style="color: grey;">Last Updated: <b>18/8/2018 12:53 pm</b></p><p>Item and quantity: <b>Bath Soap 10 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:58 pm</b></p><p>Item and quantity: <b>Blankets 100 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:55 pm</b></p><p>Item and quantity: <b>Broom 10 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>19/8/2018 2:19 pm</b></p><p>Item and quantity: <b>Dal (Paripp) 10 Kg</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:54 pm</b></p><p>Item and quantity: <b>Detergents 10 Kg</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:53 pm</b></p><p>Item and quantity: <b>Dish Washing Soaps 10 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:57 pm</b></p><p>Item and quantity: <b>Dress - Kids 40 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:57 pm</b></p><p>Item and quantity: <b>Dress - Ladies 40 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:56 pm</b></p><p>Item and quantity: <b>Floor Cleaning Liquid 10 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:58 pm</b></p><p>Item and quantity: <b>Mats 20 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:54 pm</b></p><p>Item and quantity: <b>Toilet Cleaning Brush 10 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:55 pm</b></p><p>Item and quantity: <b>Toilet Cleaning Liquid 10 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:57 pm</b></p><p>Item and quantity: <b>Undergarments - Gents 40 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:56 pm</b></p><p>Item and quantity: <b>Undergarments - Kids 20 Piece</b></p><hr><p style="color: grey;">Last Updated: <b>18/8/2018 12:56 pm</b></p><p>Item and quantity: <b>Undergarments - Ladies 20 Piece</b></p><hr>
.'''


def parse_data():
    temp_list = []
    soup = BeautifulSoup(''.join(text), features='html.parser')
    for i in soup.prettify().split('<hr/>'):
        soup_temp = BeautifulSoup(''.join(i), features='html.parser')
        x = soup_temp.find_all('p')
        temp_l2 = []
        temp_dict = {}
        for each_elem in x:
            lines = each_elem.getText().strip().splitlines()
            temp_l2.append(lines[2].strip())
        if len(x) > 0:
            temp_dict['updated'] = temp_l2[0]
            temp_dict['item'] = temp_l2[1]
            temp_list.append(temp_dict)
            # print '~' * 30
    pp.pprint(temp_list)
    return pd.DataFrame(temp_list)


if __name__ == '__main__':
    parse_data()
