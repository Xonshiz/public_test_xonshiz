#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append("..")
from comic_dl import ComicDL
import sites
import manga_eden
import sys

if __name__ == "__main__":
    ComicDL(sys.argv[1:])