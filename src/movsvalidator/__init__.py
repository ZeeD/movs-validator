import movs


class Validator:
    def __init__(self, fn: str) -> None:
        print(fn)
        kv, csv = movs.read_txt(fn)
        self.kv = kv
        self.csv = csv

    def validate(self):
        print(f'bpol.saldo_contabile:               {self.kv.saldo_contabile}')
        print(f'bpol.saldo_disponibile:             {self.kv.saldo_disponibile}')

        s = sum((item.accrediti if item.accrediti is not None else 0) -
                (item.addebiti if item.addebiti is not None else 0)
                for item in self.csv)
        print(f'Σ (item.accredito - item.addebito): {s}')
