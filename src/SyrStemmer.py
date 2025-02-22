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

from typing import Tuple, Dict, List
from SyrTools import SyrTools

# text = "ܠܲܚܡܵܐ ܠܡܕ݂ܝܼܢ݇ܬܵܐ ܒܕܸܡܵܐ ܒܘܼܡܵܐ ܘܲܪܕܵܐ ܘܟܬ݂ܵܒ݂ܵܐ ܒܘܼܫܠܵܐ ܒܲܫܘܼܠܲܢ ܠܸܥܙܵܐ ܘܟܲܪܥܵܐ ܕܐܵܗܵܐ ܕܟܘܼܪܣܝܵܐ ܒܘܼܫܵܠܵܐ ܠܵܒܸܫ"


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
            print("word:", word)
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
        
            print("\n")
            # Try each suffix in order (longest to shortest)
            for suffix in suffixes:                
                if word.endswith(suffix):
                    print("suffix:", suffix)
                    # Calculate potential stem
                    potential_stem = word[:-len(suffix)]
                    print("potential:", potential_stem)
                    # Check if stem meets minimum length requirement
                    if len(potential_stem) >= self.min_stem_length:
                        potential_stem = self.apply_infinitive_rules(potential_stem)
                        return potential_stem
     
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
        if word[-1] == 'ܝ':
            word = word[:-1] + 'ܐ'
    
        if word[-2] == 'ܝ':
            word = word[:-2] + 'ܐ' + word[-1]       
    
        return word

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
            vocalized_word = word
            unvocalized_word = self.normalize(word)            
            word = self.remove_suffixes(unvocalized_word)
            print("%s -> %s -> %s" % (vocalized_word, unvocalized_word, word))

if __name__ == "__main__":
    wordlist = [
        #'ܫܸܡܵܐ ܒܪܝܼܟ݂ܵܐ ܩܐ ܒܪܝܼܟ݂ܵܐ ܢܵܫܵܐ',
        #'ܐܵܢܵܐ ܒܢܸܠܗ ܚܕ ܒܲܝܬܸܐ ܚܕܲܬܸܐ،ܒܵܢܸܐ،ܒܵܢܘܿܝܬܵܐ،‌ܒܢܝܼܬ݂ܵܐ،ܒܲܢܵܝܵܐ،ܒܢܸܠܘܟ',
        "ܒܵܢܝܼܬ݂ܵܐ،ܒܵܢܸܐ،ܚܕܲܬܵܐ،‌ܒܲܢܵܝܵܐ،ܕܝܵܪܵܐ،ܩܝܵܡܵܐ،ܚܝܵܝܵܐ،ܗܘܵܝܵܐ،ܚܝܵܛܵܐ"
    ]

    Stemmer = SyrStemmer()
    Stemmer.stem(wordlist)