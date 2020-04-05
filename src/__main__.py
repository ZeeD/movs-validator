#!/usr/bin/env python

import sys

from movsvalidator import Validator
import logging


def main() -> None:
    if not sys.argv[1:]:
        raise SystemExit(f'uso: {sys.argv[0]} ACCUMULATOR...')

    for fn in sys.argv[1:]:
        try:
            Validator(fn).validate()
        except Exception:
            logging.exception(fn)


if __name__ == '__main__':
    main()
