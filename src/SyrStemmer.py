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
        self.verb_to_be = self.syrtools.VERB_TO_BE
        self.personal_pronouns = self.syrtools.PERSONAL_PRONOUNS     
        self.bdol_letters = self.syrtools.BDOL_LETTERS   

    def tokenize_words(self, words:str, punctuation) -> List[str]:
        """
        Tokenize Syriac words into a word list

        Parameters:
            words (str): Syriac word

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

    def remove_tense(self, word:str, group:str, label:str) -> str:
        """
        Remove specified tense from tokenized words

        Parameters:
            word (str): Tokenized Syriac word

        Returns:
            str: Emtpy string if it matches the grouping
        """
        # Create list of the combined masculine, feminine, and plural 'to be' verbs
        tenses = sorted(list(group), key=len, reverse=True)

        for tense in tenses:            
            if word.endswith(tense):
                logger.info(f"[*] Matching {label}: {tense}. Word dropped.")
                return ""
        
        return word

    def remove_bdol_letters(self, word:str) -> str:
        """
        Does the tokenized word contains a BDOL letter? If so, remove it

        Parameters:
            word (str): Tokenized Syriac word
        
        Returns:
            str: BDOL-less Syriac word
        """
                
        # Naive interpretation focusing on ܒ for now
        if word and word[0] in self.syrtools.LETTER_BETH:
            logger.info(f"[*] Matching BDOL letter {word[0]} in {word}")
            # Remove first letter and check remaining length
            remaining = word[1:]
            if len(remaining) >= self.min_stem_length:
                logger.info(f"    ⮡ Potential stem: {remaining}")
                return remaining
               
        return word

    def remove_suffixes(self, word:str) -> str:
        """
        Remove the suffixes from the word

        Parameters:
            word (str): Tokenized Syriac word
        
        Returns:
            str: Suffix-less Syriac word
        """
        # Create list of suffixes and sort by length (longest first)
        suffixes = sorted(list(self.suffixes), key=len, reverse=True)        

        if len(word) >= self.min_stem_length:
                    
            # Try each suffix in order (longest to shortest)
            for suffix in suffixes:
                if word.endswith(suffix):
                    logger.info(f"✳ Matching suffix(es): {suffix}")
                    # Calculate potential stem
                    potential_stem = word[:-len(suffix)]                    
                    # Check if stem meets minimum length requirement
                    if len(potential_stem) >= self.min_stem_length:
                        logger.info(f"  Potential stem: matches minimum length {self.min_stem_length}")
                        logger.info(f"  Potential stem: suffix used is {suffix}")
                        logger.info(f"  Potential stem: {potential_stem}")
                        potential_stem = self.apply_infinitive_rules(potential_stem)                        
                        return potential_stem
                    else:
                        logger.info(f"  Potential stem: length too small: {potential_stem}. Will try another suffix.")
     
        # Return original word if:
        # 1. Original word is shorter than min_stem_length
        # 2. Longest suffix doesn't match
        # 3. Removing suffix would make word too short
        return word

    def apply_infinitive_rules(self, word:str) -> str:
        """
        Apply the infinitive verb rules to the word after the word has been
        normalized and processed
        """

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
                
            return word_infinitive

        return word

    def apply_present_tense_rules(self, word:str) -> str:
        """
        Apply the present continuous tense verb rules to the word after the 
        word has been normalized and processed
        """

        # P

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
            logger.info(f"---------------------------------------------------------------------")
            logger.info(f"Word: {word}")
            logger.info(f"---------------------------------------------------------------------")
            vocalized_word = word
            unvocalized_word = self.normalize(word)
            processed_word = self.remove_tense(unvocalized_word, self.verb_to_be, "verb 'to be'")
            processed_word = self.remove_tense(processed_word, self.personal_pronouns, "personal pronouns")
            
            # Non-empty word
            if processed_word:
                processed_word = self.remove_suffixes(processed_word)
                processed_word = self.remove_bdol_letters(processed_word)

                logger.info(f"⚙ Processing input data ")
                logger.info(f"  vocalized: {vocalized_word}")
                logger.info(f"  unvocalized: {unvocalized_word}") 
                logger.info(f"  processed: {processed_word}")
            logger.info(f"")
        
if __name__ == "__main__":

    set_logging(LOGGING_ENABLED)
    
    # Set initial logging state
    wordlist = [
        #'ܫܸܡܵܐ ܒܪܝܼܟ݂ܵܐ ܩܐ ܒܪܝܼܟ݂ܵܐ ܢܵܫܵܐ',
        #'ܐܵܢܵܐ ܒܢܸܠܗ ܚܕ ܒܲܝܬܸܐ ܚܕܲܬܸܐ،ܒܵܢܸܐ،ܒܵܢܘܿܝܬܵܐ،‌ܒܢܝܼܬ݂ܵܐ،ܒܲܢܵܝܵܐ،ܒܢܸܠܘܟ',
        "ܒܵܢܝܼܬ݂ܵܐ،ܒܵܢܸܐ،ܚܕܲܬܵܐ،‌ܒܲܢܵܝܵܐ،ܕܝܵܪܵܐ،ܩܝܵܡܵܐ،ܚܝܵܝܵܐ،ܗܘܵܝܵܐ،ܚܝܵܛܵܐ",
        "ܐܵܢܵܐ ܒܸܟܬܵܒ݂ܵܐ ܝܘܸܢ،ܗܘ ܒܵܩܝܵܡܵܐ ܝܠܸܗ،ܐܲܢܬ̄ ܒܸܒܢܵܝܵܐ ܝܘܲܬܝ،",
        "ܠܸܫܵܢܵܐ ܕܝܸܡܵܐ"
    ]

    Stemmer = SyrStemmer()
    Stemmer.stem(wordlist)