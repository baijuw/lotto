from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

page = 'http://www.walottery.com/winningnumbers/'  # Web URL to scrap
global l, m, n, o, p, q, r
l = m = n = o = p = q = r = 1


class PowerBall:
    def __init__(self):
        self.cash = 0
        self.win = {0, 0, 0, 0, 0}
        self.power_ball = 0
        self.date = None
        self.jackpot = None

    def print_powerball(self):
        print()
        print('-' * 13, ' ' * 4, 'Powerball', ' ' * 4, '-' * 13)
        """ Split and join the array before it is displayed """
        print('Last draw:  [', ' '.join(self.win), ']', '  Powerball : ', self.power_ball)
        print('The next jackpot is: ', self.jackpot)
        print('cash option: ', self.cash)
        print('The next draw date is: ', self.date)
        print('-' * 47)
        print('\n')


class MegaMillion:
    def __init__(self):
        self.cash = 0
        self.win = {0, 0, 0, 0, 0}
        self.mega_ball = 0
        self.date = None
        self.jackpot = None

    def print_megamillion(self):
        print('-' * 13, ' ' * 4, 'Megamillion', ' ' * 4, '-' * 13)
        print('Last draw:  [', ' '.join(self.win), ']', '  MegaBall : ', self.mega_ball)
        print('The next jackpot is: ', self.jackpot)
        print('cash option: ', self.cash)
        print('The next draw date is: ', self.date)
        print('-' * 47)
        print('\n')


class Lotto:
    def __init__(self):
        self.cash = 0
        self.win = [0, 0, 0, 0, 0, 0]
        self.date = None
        self.jackpot = None

    def print_lotto(self):
        print('-' * 13, ' ' * 4, 'Lotto', ' ' * 4, '-' * 13)
        print('Last draw:  [', ' '.join(self.win), ']')
        print('The next jackpot is: ', self.jackpot)
        print('cash option: ', self.cash)
        print('The next draw date is: ', self.date)
        print('-' * 47)
        print('\n')

class Hit5:
    def __init__(self):
        self.win = [0, 0, 0, 0, 0]
        self.date = None
        self.jackpot = None

    def print_hit5(self):
        print('-' * 13, ' ' * 4, 'Hit5', ' ' * 4, '-' * 13)
        print('Last draw:  [', ' '.join(self.win), ']')
        print('The next jackpot is: ', self.jackpot)
        print('The next draw date is: ', self.date)
        print('-' * 47)
        print('\n')

class Match4:
    def __init__(self):
        self.win = [0, 0, 0, 0]
        self.jackpot = None

    def print_match4(self):
        print('-' * 13, ' ' * 4, 'Match4', ' ' * 4, '-' * 13)
        print('Last draw:  [', ' '.join(self.win), ']')
        print('The next jackpot is: ', self.jackpot)
        print('-' * 47)
        print('\n')


class DailyGame:
    def __init__(self):
        self.win = [0, 0, 0]
        self.jackpot = None

    def print_dailygame(self):
        print('-' * 13, ' ' * 4, 'Daily Game', ' ' * 4, '-' * 13)
        print('Last draw:  [', ' '.join(self.win), ']')
        print('The next jackpot is: ', self.jackpot)
        print('-' * 47)
        print('\n')

class Keno:
    def __init__(self):
        self.win = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.jackpot = None

    def print_keno(self):
        print('-' * 13, ' ' * 4, 'Keno', ' ' * 4, '-' * 13)
        print('Last draw:  [', ' '.join(self.win), ']')
        print('-' * 47)
        print('\n')

def read_url(page, htm=None):
    """Special url read function which does the following
       1. read url
       2. write a file with utf-8 decoded raw output to a sample file for reference
       3. return the raw output of urlopen"""
    output_file = 'urllib_request_output'  # Raw output file from urllib.request, just for reference
    htm = urlopen(page)
    return htm


def read_bsobj(htm):
    soup = BeautifulSoup(htm, "html.parser")
    assert isinstance(soup, object)
    return soup


def connect_to_google():
    pass


def log_to_google():
    pass


def hit5(i):
    global l
    if l == 1:
        x = Hit5()
        x.win = [z.get_text() for z in i.ul.find_all('li')]
        x.jackpot = i.footer.h1.get_text()
        x.date = i.footer.find_all('h4')[1].strong.get_text()
        x.print_hit5()
        l += 1


def lotto(i):
    global m
    if m == 1:
        x = Lotto()
        x.cash = i.footer.p.strong.get_text()
        x.win = [z.get_text() for z in i.ul.find_all('li')]
        x.jackpot = i.footer.h1.get_text()
        x.date = i.footer.find_all('h4')[1].strong.get_text()
        x.print_lotto()
    m += 1


def megamillions(i):
    global n
    if n == 1:
        x = MegaMillion()
        x.cash = i.footer.p.strong.get_text()
        x.win = [z.get_text() for z in i.ul.find_all('li') if not z.has_attr('class')]
        x.mega_ball = i.ul.find_all('li', {'class': 'game-ball-megamillions'})[0].get_text()
        x.jackpot = i.footer.h1.get_text()
        x.date = i.footer.find_all('h4')[1].strong.get_text()
        x.print_megamillion()
    n += 1


def dailygame(i):
    global o
    if o == 1:
        x = DailyGame()
        x.win = [z.get_text() for z in i.ul.find_all('li')]
        x.jackpot = i.footer.h1.get_text()
        x.print_dailygame()
    o += 1


def match4(i):
    global p
    if p == 1:
        x = Match4()
        x.win = [z.get_text() for z in i.ul.find_all('li')]
        x.jackpot = i.footer.h1.get_text()
        x.print_match4()
    p += 1


def powerball(i):
    global q
    """ Since there were duplicate segments on the website, we have to make sure
    that we extract the information only once. So a simple global variable and if
    an if statment is used"""

    if q == 1:
        """ Create a powerball instance """

        x = PowerBall()
        x.cash = i.footer.p.strong.get_text()

        """ Using list comprehension and an if statement with the has_attr method
        to get the winning numbers"""

        x.win = [z.get_text() for z in i.ul.find_all('li') if not z.has_attr('class')]

        """ Get text from the first occurrence of the class attribute with value
         game-ball-powervall"""

        x.power_ball = i.ul.find_all('li', {'class': 'game-ball-powerball'})[0].get_text()
        x.jackpot = i.footer.h1.get_text()
        x.date = i.footer.find_all('h4')[1].strong.get_text()
        x.print_powerball()
    q += 1


def keno(i):
    global r
    if r == 1:
        x = Keno()
        x.win = [z.get_text() for z in i.ul.find_all('li')]
        x.print_keno()
    r += 1


htm = read_url(page)
soup = read_bsobj(htm)
dict = {'hit5': hit5,
        'lotto': lotto,
        'megamillions': megamillions,
        'dailygame': dailygame,
        'match4': match4,
        'powerball': powerball,
        'keno': keno}

main_block = soup.find_all('div', {'class': ['game-bucket', re.compile(r'game-bucket-(.+)')]})
for i in main_block:
    x = re.search(r'game-bucket-(.+)', i.parent.div["class"][1])
    # print(x.group(1))
    if x.group(1) in dict.keys():
        dict[x.group(1)](i)