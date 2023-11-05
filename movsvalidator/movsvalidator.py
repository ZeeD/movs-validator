from datetime import date
from sys import argv

from movs.model import KV
from movs import read_txt
from movs.model import Row


def validate_saldo(kv: KV, csv: list[Row]) -> bool:
    print(f'bpol.saldo_al:                      {kv.saldo_al}')
    if kv.saldo_al:
        ultimo_update = (date.today() - kv.saldo_al).days
        print(f'ultimo update:                      {ultimo_update} giorni fa')
    print(f'bpol.saldo_contabile:               {float(kv.saldo_contabile):_}')
    print(
        f'bpol.saldo_disponibile:             {float(kv.saldo_disponibile):_}')

    s = sum(item.money for item in csv)
    print(f'Σ (item.accredito - item.addebito): {float(s):_}')
    ret = kv.saldo_contabile == s == kv.saldo_disponibile
    if not ret:
        delta = max([abs(kv.saldo_contabile-s), abs(s-kv.saldo_disponibile)])
        print(f'Δ:                                  {float(delta):_}')
    return ret


def validate_dates(csv: list[Row]) -> bool:
    data_contabile: date | None = None
    for row in csv:
        if data_contabile is not None and data_contabile < row.data_contabile:
            print(f'{data_contabile} < {row.data_contabile}!')
            return False
    return True


def validate(fn: str) -> bool:
    print(fn)
    kv, csv = read_txt(fn)
    return all([validate_saldo(kv, csv), validate_dates(csv)])


def main() -> None:
    if not argv[1:]:
        raise SystemExit(f'uso: {argv[0]} ACCUMULATOR...')

    for fn in argv[1:]:
        if not validate(fn):
            raise SystemExit(f'{fn} seems has some problems!')
