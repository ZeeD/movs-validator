from datetime import date
from decimal import Decimal
from sys import argv

from movs import read_txt

ZERO = Decimal(0)


def validate(fn: str) -> bool:
    print(fn)
    kv, csv = read_txt(fn)
    print(f'bpol.saldo_al:                      {kv.saldo_al}')
    if kv.saldo_al:
        ultimo_update = (date.today() - kv.saldo_al).days
        print(f'ultimo update:                      {ultimo_update} giorni fa')
    print(f'bpol.saldo_contabile:               {kv.saldo_contabile}')
    print(f'bpol.saldo_disponibile:             {kv.saldo_disponibile}')

    s = sum((item.accrediti if item.accrediti is not None else ZERO) -
            (item.addebiti if item.addebiti is not None else ZERO)
            for item in csv)
    print(f'Σ (item.accredito - item.addebito): {s}')
    return kv.saldo_contabile == s == kv.saldo_disponibile


def main() -> None:
    if not argv[1:]:
        raise SystemExit(f'uso: {argv[0]} ACCUMULATOR...')

    for fn in argv[1:]:
        if not validate(fn):
            raise SystemExit(f'{fn} seems has some problems!')


if __name__ == '__main__':
    main()
