#!/usr/bin/env python3
"""SPARTACO / OM337 — offline desktop application bootstrap.
Copyright (c) 2026 Ilver Villasmil.
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AUDITOR_DIR = ROOT / 'modules' / 'auditor'
INTERFACE_DIR = ROOT / 'modules' / 'interfaz'
AUDITOR_FILE = AUDITOR_DIR / 'auditor_descarte.py'
INTERFACE_FILE = INTERFACE_DIR / 'interfaz_3_AUDITOR.py'


def prepare() -> None:
    for file in (AUDITOR_FILE, INTERFACE_FILE):
        if not file.is_file():
            raise SystemExit(f'Missing required module: {file.relative_to(ROOT)}')
    # The interface imports auditor_descarte by its original module name.
    for directory in (str(AUDITOR_DIR), str(INTERFACE_DIR)):
        if directory not in sys.path:
            sys.path.insert(0, directory)
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)


def main() -> int:
    parser = argparse.ArgumentParser(description='SPARTACO / OM337 desktop bootstrap')
    parser.add_argument('--check', action='store_true', help='Check local files and dependencies without opening the GUI')
    args = parser.parse_args()
    prepare()
    if importlib.util.find_spec('webview') is None:
        print('Missing dependency: pywebview. Install with: python -m pip install pywebview', file=sys.stderr)
        return 1
    if args.check:
        print('OK: auditor module, interface module, and pywebview are available.')
        return 0
    from interfaz_3_AUDITOR import main as launch_desktop
    launch_desktop()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
