#!/usr/bin/env python3
# coding=utf-8

"""
    ' @file SyrStemmer.py
    '
    ' @author The Assyrian Digital Language Consortium
    ' @date 13 Feb 2025
    '
    ' @brief Syriac Light Stemmer
    '
    ' @description: This file contains the Syriac light stem algorithm
    '
    ' @license MIT License
    ' @copyright Assyrian Digital Language Consortium 
"""

"""
    ' Algorithm Flowchart
    '
    ' Step 1. Tokenization
    ' Step 2. Normalization
    ' Step 3. Removal of BDOL prefixes
"""

import unicodedata
import re

from typing import Tuple, Dict, List
from SyrTools import SyrTools

text = "ܠܲܚܡܵܐ ܠܡܕ݂ܝܼܢ݇ܬܵܐ ܒܕܸܡܵܐ ܒܘܼܡܵܐ ܘܲܪܕܵܐ ܘܟܬ݂ܵܒ݂ܵܐ ܒܘܼܫܠܵܐ ܒܲܫܘܼܠܲܢ ܠܸܥܙܵܐ ܘܟܲܪܥܵܐ ܕܐܵܗܵܐ ܕܟܘܼܪܣܝܵܐ ܒܘܼܫܵܠܵܐ ܠܵܒܸܫ"