#playfair

import re
from enum import Enum


LETTERS = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'


class Playfair:
    @staticmethod
    def check_input(arg):
        if not isinstance(arg, str):
            raise TypeError(
                'The argument of the function should be an instance of `str`')

        if not all(i.isascii() & i.isprintable() for i in arg):
            raise ValueError(
                'The argument of the function should be a `str` containing only printable ASCII characters')

    @staticmethod
    def prepare(msg):
        msg = msg.upper().replace('J', 'I')
        Playfair.check_input(msg)
        msg = ''.join([i for i in msg if i.isalpha()])
        while msg:
            s = msg[:2]
            if len(set(s)) == 2 and s[-1] != 'X':
                msg = msg[2:]
            else:
                s = s[0] + 'X'
                msg = msg[1:]
            yield s

    def __init__(self, key):
        key = key.upper().replace('J', 'I')
        Playfair.check_input(key)
        key = ''.join(i for i in key if i.isalpha())
        self.square = list(dict.fromkeys(key + LETTERS))

    def locate(self, letter):
        letter = letter.upper()
        return list(divmod(self.square.index(letter), 5))

    def get_letter(self, pos):
        index = pos[0] * 5 + pos[1]
        return self.square[index]

    def transform(self, pair, move):
        p0, p1 = map(self.locate, pair)
        def roll(x): return (x + move) % 5
        for i in range(3):
            if i < 2 and p0[i] == p1[i]:
                j = 1 - i
                p0[j], p1[j] = map(roll, (p0[j], p1[j]))
                break
            if i == 2:
                p0[1], p1[1] = p1[1], p0[1]
        return ''.join(map(self.get_letter, (p0, p1)))

    def encrypt(self, msg):
        pairs = Playfair.prepare(msg)
        return ' '.join(self.transform(pair, 1) for pair in pairs)

    def decrypt(self, msg):
        msg = msg.upper()
        Playfair.check_input(msg)
        if not re.match(r'^([A-Z]{2}(\s)?)+$', msg):
            raise ValueError(
                "The inputted message isn't a valid Playfair cipher message")
        msg = re.findall('[A-Z]{2}', msg)
        def rule1(x): return x if x[1] != 'X' else x[0]
        return ' '.join(rule1(self.transform(s, -1)) for s in msg)


def test():
    p = Playfair("Imagine there's no heaven")
    plain = [
        'I am a new soul, I came to this strange world',
        'Starry starry night, paint your palette blue and grey',
        'I crown me king of the sweet cold north',
        'If I die young, bury me in satin',
        "Come gather 'round people, wherever you roam",
        'Somewhere over the rainbow'
    ]
    encrypted = [
        'MG AG IS ZT FI FA BG IT EV HR NE EH HG IN TU CE QB',
        'EH GH CG EH GH CG IM AR RK GM MS UC YE LG FH HW HT LX IO GI CN ST ZY',
        'GO EC ZM IT FM IN FU HR TE UT TH DV QB ID SH BA',
        'EU NO EO UC ZI AC YE WG OE SD MH MI',
        'DV IT NG HR TS EC ZI CQ OF QP TU RT ST OT CG FI EC GA',
        'ED IT XT TS OF OT SH RT HG MI CV XY'
    ]
    decrypted = [
        'IA MA NE WS OU LI CA ME TO TH IS ST RA NG EW OR LD',
        'ST AR RY ST AR RY NI GH TP AI NT YO UR PA LE T TE BL UE AN DG RE Y',
        'IC RO WN ME KI NG OF TH ES WE ET CO LD NO RT H',
        'IF ID IE YO UN GB UR YM EI NS AT IN',
        'CO ME GA TH ER RO UN DP EO PL EW HE RE VE RY OU RO AM',
        'SO ME WH ER EO VE RT HE RA IN BO W'
    ]
    # assert [p.encrypt(i) for i in plain] == encrypted
    print("encrypted code :\n")
    [print(p.encrypt(i)) for i in plain]
    # assert [p.decrypt(i) for i in encrypted] == decrypted
    print("decrypted code : \n")
    [print(p.decrypt(i)) for i in encrypted]



test()
