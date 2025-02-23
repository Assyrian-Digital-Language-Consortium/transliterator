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

import unicodedata
import re
import logging

from typing import Tuple, Dict, List
from SyrTools import SyrTools

# Enable / disable logging
LOGGING_ENABLED = True

# Configure the logging system
logging.basicConfig(
    level=logging.DEBUG,  # Set the threshold level - DEBUG is the lowest
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Function to toggle logging
def set_logging(enabled):
    if enabled:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.ERROR)


# Algorithm Flowchart
# -----------------------------------------------------------------------------   
# Step 1. Tokenization
# Step 2. Normalization
# Step 3. Removal of BDOL prefixes

class SyrStemmer:
    """
    A class for providing a rudimentary stemmer
    """

    def __init__(self) -> None:
        #self.max_prefix_length = 6
        #self.max_suffix_length = 5
        self.min_stem_length = 3

        self.syrtools = SyrTools()
        self.normalize = self.syrtools.normalize
        self.punctuation = self.syrtools.PUNCTUATION
        self.suffixes = self.syrtools.SUFFIXES        

    def tokenize_words(self, words:str, punctuation) -> List[str]:
        """
        Tokenize Syriac words into a word list

        Parameters:
            words (str): Syriac

        Returns:
            str: The tokenized version of the word.
        """
        result = []        
        # Process each word
        for word in words:
            logger.info(f"Tokenizing: {word}")
            # Replace punctuation with spaces
            for punct in self.punctuation:
                word = word.replace(punct, ' ')
        
            # Split on whitespace and filter out empty strings
            words = word.split()
        
            # Add each non-empty word to the new list
            for word in words:
                if word.strip():  # Only add non-empty words
                    result.append(word)

        return result

    def remove_suffixes(self, word:str) -> str:
        """
        Remove the suffixes from the word

        Parameters:
            word (str): Tokenize Syriac word
        
        Returns:
            str: Suffix-less Syriac word
        """
        # Create list of suffixes and sort by length (longest first)
        suffixes = sorted(list(self.suffixes), key=len, reverse=True)        

        if len(word) >= self.min_stem_length:
                    
            # Try each suffix in order (longest to shortest)
            for suffix in suffixes:
                if word.endswith(suffix):
                    logger.info(f"[*] Matching suffix(es): {suffix}")
                    # Calculate potential stem
                    potential_stem = word[:-len(suffix)]
                    logger.info(f"  Potential stem: {potential_stem}")
                    # Check if stem meets minimum length requirement
                    if len(potential_stem) >= self.min_stem_length:
                        logger.info(f"  Potential stem: matches minimum length {self.min_stem_length}")
                        logger.info(f"  Potential stem: suffix used is {suffix}")
                        potential_stem = self.apply_infinitive_rules(potential_stem)
                        return potential_stem
                    else:
                        logger.info(f"  Potential stem: length too small: {potential_stem}. Will try another suffix.\n")
     
        # Return original word if:
        # 1. Original word is shorter than min_stem_length
        # 2. Longest suffix doesn't match
        # 3. Removing suffix would make word too short
        return word
    
    def apply_infinitive_rules(self, word:str) -> str:
        """
        Apply the infinitive verb rules to the word after the word has been
        normalized and within the remove_suffixes function
        """

        # ---------------------------------------------------------------------
        # VERBS GROUPS
        # ---------------------------------------------------------------------        

        # Pa'el = ܦܵܥܸܠ = Infinitive
        #   1. Verbal roots without ܐ ܘ ܝ as the 2nd or 3rd letters
        #   2. Verbal roots with ܐ as the 2nd letter
        #   3. Verbal roots with ܐ as the 3rd letter

        # If ܝ yudh is in the second or third root position, then replace the 
        # yudh with alaph
        if word[-1] == self.syrtools.LETTER_YUDH or word[-2] == self.syrtools.LETTER_YUDH:
            logger.info(f"  ⮡ Applying infinitive verb rules")

            word_applied: str = ''
            if word[-1] == self.syrtools.LETTER_YUDH:
                word_infinitive = word[:-1] + self.syrtools.LETTER_ALAPH                
            elif word[-2] == self.syrtools.LETTER_YUDH:
                word_infinitive = word[:-2] + self.syrtools.LETTER_ALAPH + word[-1]                
    
            logger.info(f"    Infinitive: {word} -> {word_infinitive}")
            return word_infinitive

    def stem(self, text: str) -> str:
        """
        Stem the Syriac words using mechanistic rules

        Parameters:
            text: Syriac

        Returns:
            str: The Syriac stem
        """                
        words: List[str] = self.tokenize_words(text, self.punctuation)
        
        for word in words:
            logger.info(f"Word: {word}")
            vocalized_word = word
            unvocalized_word = self.normalize(word)            
            word = self.remove_suffixes(unvocalized_word)
            logger.info(f"Processing input data: {vocalized_word} ← {unvocalized_word} ← {word}\n")

if __name__ == "__main__":

    set_logging(LOGGING_ENABLED)
    
    # Set initial logging state
    wordlist = [
        #'ܫܸܡܵܐ ܒܪܝܼܟ݂ܵܐ ܩܐ ܒܪܝܼܟ݂ܵܐ ܢܵܫܵܐ',
        #'ܐܵܢܵܐ ܒܢܸܠܗ ܚܕ ܒܲܝܬܸܐ ܚܕܲܬܸܐ،ܒܵܢܸܐ،ܒܵܢܘܿܝܬܵܐ،‌ܒܢܝܼܬ݂ܵܐ،ܒܲܢܵܝܵܐ،ܒܢܸܠܘܟ',
        "ܒܵܢܝܼܬ݂ܵܐ،ܒܵܢܸܐ،ܚܕܲܬܵܐ،‌ܒܲܢܵܝܵܐ،ܕܝܵܪܵܐ،ܩܝܵܡܵܐ،ܚܝܵܝܵܐ،ܗܘܵܝܵܐ،ܚܝܵܛܵܐ"
    ]

    Stemmer = SyrStemmer()
    Stemmer.stem(wordlist)