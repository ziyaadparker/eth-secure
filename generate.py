from itertools import product
from itertools import islice
from ethereum import utils

def allkeys(chars, length):
    for letters in product(chars, repeat=length):
        yield ''.join(letters)

def main():
    f_o = open('private_public_eth_keys.csv', 'w')
    letters = "0123456789abcdef"
    for wordlen in range(64,65):
        n_skip = 5000000
        for prvt_key in islice(allkeys(letters, wordlen), 3, None, n_skip):
            print(prvt_key)
            public_key = utils.privtoaddr(prvt_key)
            f_o.write(prvt_key + ',' + public_key +'\n')

if __name__=="__main__":
    main()
