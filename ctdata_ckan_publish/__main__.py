# -*- coding: utf-8 -*-
"""Allow to be executable through `python -m ctdata_ckan_publish`."""
from __future__ import absolute_import

from .cli import main

if __name__ == "__main__":  # pragma: no cover
        main(prog_name="publish")
