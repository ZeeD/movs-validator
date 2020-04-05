import movs


class Validator:
    def __init__(self, fn: str) -> None:
        kv, csv = movs.read_txt(fn)
        self.kv = kv
        self.csv = csv

    def validate(self):
        print(f'bpol.saldo_contabile: {self.kv.saldo_contabile}')
        print(f'bpol.saldo_disponibile: {self.kv.saldo_disponibile}')

        s = sum(item.accredito - item.addebito for item in self.csv)
        print(f'Σ (item.accredito - item.addebito): {s}')
