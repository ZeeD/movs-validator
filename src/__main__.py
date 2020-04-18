#!/usr/bin/env python

'validator'

import logging
import sys

from movsvalidator import Validator


def main() -> None:
    'main'

    if not sys.argv[1:]:
        raise SystemExit(f'uso: {sys.argv[0]} ACCUMULATOR...')

    for fn in sys.argv[1:]:
        try:
            Validator(fn).validate()
        except Exception:  # pylint: disable=broad-except
            logging.exception(fn)


if __name__ == '__main__':
    main()
