from AFND import AFND
from AFD import AFD

class E_AFND(AFND):
    def __init__(self, alphabet):
        super().__init__(alphabet)
        self.alphabet = alphabet+"&"