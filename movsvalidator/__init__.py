from datetime import date
from sys import argv

from movs import read_txt


def validate(fn: str) -> bool:
    print(fn)
    kv, csv = read_txt(fn)
    print(f'bpol.saldo_al:                      {kv.saldo_al}')
    if kv.saldo_al:
        ultimo_update = (date.today() - kv.saldo_al).days
        print(f'ultimo update:                      {ultimo_update} giorni fa')
    print(f'bpol.saldo_contabile:               {float(kv.saldo_contabile):_}')
    print(
        f'bpol.saldo_disponibile:             {float(kv.saldo_disponibile):_}')

    s = sum(item.money for item in csv)
    print(f'Σ (item.accredito - item.addebito): {float(s):_}')
    return kv.saldo_contabile == s == kv.saldo_disponibile


def main() -> None:
    if not argv[1:]:
        raise SystemExit(f'uso: {argv[0]} ACCUMULATOR...')

    for fn in argv[1:]:
        if not validate(fn):
            raise SystemExit(f'{fn} seems has some problems!')


if __name__ == '__main__':
    main()
