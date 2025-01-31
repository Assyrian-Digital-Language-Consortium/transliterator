'''
' @file Syr.py
'
' @author The Assyrian Digital Language Consortium  
' @date 1 Feb 2025
'
' @brief Syriac transliteration and phonetic approximation
'
' @description: This file contains the Syr class which is used 
'               to as a base clase utility for working with Syriac 
'               text.
'
' @license MIT License
' @copyright Assyrian Digital Language Consortium  
'''

import unicodedata

class Syr:
    def __init__(self):
        # --------------------------------------------------------------------------
        # Punctuation and Special Marks
        # --------------------------------------------------------------------------
        self.END_OF_PARAGRAPH              = '\u0700'  # ܀
        self.SUPRALINEAR_FULL_STOP         = '\u0701'  # ܁
        self.SUBLINEAR_FULL_STOP           = '\u0702'  # ܂
        self.SUPRALINEAR_COLON             = '\u0703'  # ܃
        self.SUBLINEAR_COLON               = '\u0704'  # ܄
        self.HORIZONTAL_COLON              = '\u0705'  # ܅
        self.COLON_SKEWED_LEFT             = '\u0706'  # ܆
        self.COLON_SKEWED_RIGHT            = '\u0707'  # ܇
        self.SUPRALINEAR_COLON_SKEWED_LEFT = '\u0708'  # ܈
        self.SUBLINEAR_COLON_SKEWED_RIGHT  = '\u0709'  # ܉
        self.CONTRACTION                   = '\u070A'  # ܊
        self.HARKLEAN_OBELUS               = '\u070B'  # ܋
        self.HARKLEAN_METOBELUS            = '\u070C'  # ܌
        self.HARKLEAN_ASTERISCUS           = '\u070D'  # ܍
        self.ABBREVIATION_MARK             = '\u070F'  # ܏
        self.BARREKH                       = '\u074A'  # ݊
        self.MUSIC                         = '\u0749'  # ݉

        # --------------------------------------------------------------------------
        # 2) Letters
        # --------------------------------------------------------------------------
        self.LETTER_ALAPH                  = '\u0710'  # ܐ
        self.LETTER_SUPERSCRIPT_ALAPH      = '\u0711'  # ܑ
        self.LETTER_BETH                   = '\u0712'  # ܒ
        self.LETTER_GAMAL                  = '\u0713'  # ܓ
        self.LETTER_GAMAL_GARSHUNI         = '\u0714'  # ܔ
        self.LETTER_DALATH                 = '\u0715'  # ܕ
        self.LETTER_DOTLESS_DALATH_RISH    = '\u0716'  # ܖ
        self.LETTER_HE                     = '\u0717'  # ܗ
        self.LETTER_WAW                    = '\u0718'  # ܘ
        self.LETTER_ZAIN                   = '\u0719'  # ܙ
        self.LETTER_HETH                   = '\u071A'  # ܚ
        self.LETTER_TETH                   = '\u071B'  # ܛ
        self.LETTER_TETH_GARSHUNI          = '\u071C'  # ܜ
        self.LETTER_YUDH                   = '\u071D'  # ܝ
        self.LETTER_YUDH_HE                = '\u071E'  # ܞ
        self.LETTER_KAPH                   = '\u071F'  # ܟ
        self.LETTER_LAMADH                 = '\u0720'  # ܠ
        self.LETTER_MIM                    = '\u0721'  # ܡ
        self.LETTER_NUN                    = '\u0722'  # ܢ
        self.LETTER_SEMKATH                = '\u0723'  # ܣ
        self.LETTER_FINAL_SEMKATH          = '\u0724'  # ܤ
        self.LETTER_E                      = '\u0725'  # ܥ (ʿAyn - Unicode name is "Letter E")
        self.LETTER_PE                     = '\u0726'  # ܦ
        self.LETTER_REVERSED_PE            = '\u0727'  # ܧ
        self.LETTER_SADHE                  = '\u0728'  # ܨ
        self.LETTER_QAPH                   = '\u0729'  # ܩ
        self.LETTER_RISH                   = '\u072A'  # ܪ
        self.LETTER_SHIN                   = '\u072B'  # ܫ
        self.LETTER_TAW                    = '\u072C'  # ܬ

        # --------------------------------------------------------------------------
        # Garshuni (Persian and Sogdian) Letters
        # --------------------------------------------------------------------------
        self.LETTER_PERSIAN_BHETH          = '\u072D'  # ܭ
        self.LETTER_PERSIAN_GHAMAL         = '\u072E'  # ܮ
        self.LETTER_PERSIAN_DHALATH        = '\u072F'  # ܯ
        self.LETTER_SOGDIAN_ZHAIN          = '\u074D'  # ݍ
        self.LETTER_SOGDIAN_KHAPH          = '\u074E'  # ݎ
        self.LETTER_SOGDIAN_FE             = '\u074F'  # ݏ

        # --------------------------------------------------------------------------
        # 4) Vowel Marks (Zlameh, Ptakheh, Rwasa, Esasa, Hbasa, Zqapa, Rwakha)
        # --------------------------------------------------------------------------

        self.PTHAHA_DOTTED                 = '\u0732'  # ܲ
        self.ZQAPHA_DOTTED                 = '\u0735'  # ܵ
        self.HBASA_ESASA_DOTTED            = '\u073C'  # ܼ
        self.DOTTED_ZLAMA_HORIZONTAL       = '\u0738'  # ܸ
        self.DOTTED_ZLAMA_ANGULAR          = '\u0739'  # ܹ
        self.RWAHA                         = '\u073F'  # ܿ

        self.PTHAHA_ABOVE                  = '\u0730'  # ܰ
        self.PTHAHA_BELOW                  = '\u0731'  # ܱ
        self.ZQAPHA_ABOVE                  = '\u0733'  # ܳ
        self.ZQAPHA_BELOW                  = '\u0734'  # ܴ
        self.RBASA_ABOVE                   = '\u0736'  # ܶ
        self.RBASA_BELOW                   = '\u0737'  # ܷ
        self.HBASA_ABOVE                   = '\u073A'  # ܺ
        self.HBASA_BELOW                   = '\u073B'  # ܻ
        self.ESASA_ABOVE                   = '\u073D'  # ܽ
        self.ESASA_BELOW                   = '\u073E'  # ܾ

        # --------------------------------------------------------------------------
        # Other Diacritical/Grammatical Marks
        # --------------------------------------------------------------------------
        self.QUSHSHAYA                     = '\u0741'  # ݁
        self.RUKKAKHA                      = '\u0742'  # ݂
        self.TWO_VERTICAL_DOTS_ABOVE       = '\u0743'  # ݃
        self.TWO_VERTICAL_DOTS_BELOW       = '\u0744'  # ݄
        self.THREE_DOTS_ABOVE              = '\u0745'  # ݅
        self.THREE_DOTS_BELOW              = '\u0746'  # ݆
        self.OBLIQUE_LINE_ABOVE            = '\u0747'  # ݇
        self.OBLIQUE_LINE_BELOW            = '\u0748'  # ݈
        # (self.BARREKH and self.MUSIC are defined above under punctuation)

        # --------------------------------------------------------------------------
        # Generic Combining Diacritical Marks (non-Syriac block)
        # --------------------------------------------------------------------------
        self.COMBINING_TILDE_BELOW         = '\u0330'  #  ̰ (U+0330)
        self.COMBINING_TILDE_ABOVE         = '\u0303'  #  ̃ (U+0303)
        self.COMBINING_MACRON_BELOW        = '\u0331'  #  ̱ (U+0331)
        self.COMBINING_MACRON              = '\u0304'  #  ̄ (U+0304)
        self.COMBINING_BREVE_BELOW         = '\u032E'  #  ̮ (U+032E)
        self.COMBINING_DIAERESIS           = '\u0308'  #  ̈ (U+0308)
        self.COMBINING_DOT_BELOW           = '\u0323'  #  ̣ (U+0323)
        self.COMBINING_DOT_ABOVE           = '\u0307'  #  ̇ (U+0307)

        # --------------------------------------------------------------------------
        # Decorative Characters (non-Syriac block)
        # --------------------------------------------------------------------------
        self.KASHIDA                       = '\u0640'  # ـ (U+0640)
       
        # --------------------------------------------------------------------------
        # Useful sets for easy reference
        # --------------------------------------------------------------------------
        self.LETTER = (
            self.LETTER_ALAPH,
            self.LETTER_SUPERSCRIPT_ALAPH,
            self.LETTER_BETH,
            self.LETTER_GAMAL,
            self.LETTER_GAMAL_GARSHUNI,
            self.LETTER_DALATH,
            self.LETTER_DOTLESS_DALATH_RISH,
            self.LETTER_HE,
            self.LETTER_WAW,
            self.LETTER_ZAIN,
            self.LETTER_HETH,
            self.LETTER_TETH,
            self.LETTER_TETH_GARSHUNI,
            self.LETTER_YUDH,
            self.LETTER_YUDH_HE,
            self.LETTER_KAPH,
            self.LETTER_LAMADH,
            self.LETTER_MIM,
            self.LETTER_NUN,
            self.LETTER_SEMKATH,
            self.LETTER_FINAL_SEMKATH,
            self.LETTER_E,
            self.LETTER_PE,
            self.LETTER_REVERSED_PE,
            self.LETTER_SADHE,
            self.LETTER_QAPH,
            self.LETTER_RISH,
            self.LETTER_SHIN,
            self.LETTER_TAW,
        )

        self.BDOL_LETTERS = (
            self.LETTER_BETH,
            self.LETTER_DALATH,
            self.LETTER_WAW,
            self.LETTER_LAMADH,
        )

        self.TALQANEH = (
            self.COMBINING_MACRON_BELOW,
            self.COMBINING_MACRON,
            self.OBLIQUE_LINE_ABOVE,
            self.OBLIQUE_LINE_BELOW,
        )

        self.PUNCTUATION = (
            self.END_OF_PARAGRAPH,
            self.SUPRALINEAR_FULL_STOP,
            self.SUBLINEAR_FULL_STOP,
            self.SUPRALINEAR_COLON,
            self.SUBLINEAR_COLON,
            self.HORIZONTAL_COLON,
            self.COLON_SKEWED_LEFT,
            self.COLON_SKEWED_RIGHT,
            self.SUPRALINEAR_COLON_SKEWED_LEFT,
            self.SUBLINEAR_COLON_SKEWED_RIGHT,
            self.CONTRACTION,
            self.HARKLEAN_OBELUS,
            self.HARKLEAN_METOBELUS,
            self.HARKLEAN_ASTERISCUS,
            self.BARREKH,
            '.',
            ',',
            '!',
            '?',
            ';',
            ':',
            '،',
            '؛',
            '؟',
        )

        self.VOWEL = (
            self.PTHAHA_ABOVE,
            self.PTHAHA_BELOW,
            self.PTHAHA_DOTTED,
            self.ZQAPHA_ABOVE,
            self.ZQAPHA_BELOW,
            self.ZQAPHA_DOTTED,
            self.RBASA_ABOVE,
            self.RBASA_BELOW,
            self.DOTTED_ZLAMA_HORIZONTAL,
            self.DOTTED_ZLAMA_ANGULAR,
            self.HBASA_ABOVE,
            self.HBASA_BELOW,
            self.HBASA_ESASA_DOTTED,
            self.ESASA_ABOVE,
            self.ESASA_BELOW,
            self.RWAHA,
        )
        self.NON_MATIS_VOWEL = (
            self.PTHAHA_ABOVE,
            self.PTHAHA_BELOW,
            self.PTHAHA_DOTTED,
            self.ZQAPHA_ABOVE,
            self.ZQAPHA_BELOW,
            self.ZQAPHA_DOTTED,
            self.RBASA_ABOVE,
            self.RBASA_BELOW,
            self.DOTTED_ZLAMA_HORIZONTAL,
            self.DOTTED_ZLAMA_ANGULAR,
            self.HBASA_ABOVE,
            self.HBASA_BELOW,
            self.ESASA_ABOVE,
            self.ESASA_BELOW,
        )

        self.GARSHUNI = (
            self.LETTER_PERSIAN_BHETH,
            self.LETTER_PERSIAN_GHAMAL,
            self.LETTER_PERSIAN_DHALATH,
            self.LETTER_SOGDIAN_ZHAIN,
            self.LETTER_SOGDIAN_KHAPH,
            self.LETTER_SOGDIAN_FE,
        )

        self.DIACRITICS = (
            self.QUSHSHAYA,
            self.RUKKAKHA,
            self.COMBINING_TILDE_BELOW,
            self.COMBINING_TILDE_ABOVE,
            self.COMBINING_MACRON_BELOW,
            self.COMBINING_MACRON,
            self.COMBINING_BREVE_BELOW,
            self.COMBINING_DIAERESIS,
            self.COMBINING_DOT_BELOW,
            self.COMBINING_DOT_ABOVE,
            self.OBLIQUE_LINE_ABOVE,
            self.OBLIQUE_LINE_BELOW,
            self.PTHAHA_DOTTED,
            self.ZQAPHA_DOTTED,
            self.HBASA_ESASA_DOTTED,
            self.DOTTED_ZLAMA_HORIZONTAL,
            self.DOTTED_ZLAMA_ANGULAR,
            self.RWAHA,
            self.PTHAHA_ABOVE,
            self.PTHAHA_BELOW,
            self.ZQAPHA_ABOVE,
            self.ZQAPHA_BELOW,
            self.RBASA_ABOVE,
            self.RBASA_BELOW,
            self.HBASA_ABOVE,
            self.HBASA_BELOW,
            self.ESASA_ABOVE,
            self.ESASA_BELOW,
        )

        self.MATIS_VOWEL = (
            self.HBASA_ESASA_DOTTED,
            self.RWAHA,
        )

        self.DECORATIVE = (
            self.KASHIDA,
        )

        self.UNVOCALIZED = (
            self.LETTER_SUPERSCRIPT_ALAPH,
        )

        # Phonetic Map
        self.GLOTTAL_STOP = 'ʾ'
        self.PHARYNGEAL = 'ʿ'

    '''
    This function removes all diacritics from the given text.
    '''
    def remove_diacritics(self, text):
        return ''.join([c for c in text if c in self.LETTER])
    
    '''
    This function returns true if the given text contains any Syriac characters.
    '''
    def contains(self, text):
        for c in text:
            if c in self.LETTER:
                return True
        return False
    
    '''
    This function returns true if the given text contains any Syriac vowels.
    '''
    def contains_vowels(self, text):
        for c in text:
            if c in self.VOWEL:
                return True
        return False
    
    def remove_talqaneh_clusters(self, text):
        """
        Removes any 'letter + vowels + talqaneh' cluster from the text.
        In other words, if a letter has at least one talqaneh diacritic,
        we remove that entire group of (letter + vowels + talqaneh codes).
        
        Example scenario:
            - letter: ܐ
            - vowels: ܿ or ܸ
            - talqaneh: \u0747 (OBLIQUE_LINE_ABOVE), etc.
        If the cluster has any diacritic in self.TALQANEH, 
        that whole cluster is skipped in the final result.
        """
        result = []
        i = 0
        while i < len(text):
            ch = text[i]
            # If this character is *not* a Syriac letter, just keep it.
            if ch not in self.LETTER:
                result.append(ch)
                i += 1
                continue

            # If we see a LETTER, gather the entire "cluster":
            #   letter + zero or more [vowels/diacritics]
            cluster = [ch]
            j = i + 1

            # Collect any subsequent chars that are vowels or diacritics
            # so they stay with the same base letter.
            while j < len(text) and (text[j] in self.VOWEL or text[j] in self.DIACRITICS):
                cluster.append(text[j])
                j += 1

            # Now check if any of those collected chars are in self.TALQANEH.
            # If yes, we skip the entire cluster.
            if any((c in self.TALQANEH) for c in cluster):
                # Do not add to result — effectively remove it
                pass  # skip
            else:
                # Keep the entire cluster
                result.extend(cluster)

            # Move i to the end of this cluster
            i = j

        return ''.join(result)
    '''
    This function returns true if the given text contains any Eastern Syriac vowels.
    '''
    def contains_eastern_vowels(self, text):
        for c in text:
            if c in self.EASTERN_VOWEL:
                return True
        return False
    
    '''
    This function returns true if the given text contains any Western Syriac vowels.
    '''
    def contains_western_vowels(self, text):
        for c in text:
            if c in self.WESTERN_VOWELS:
                return True
        return False
    
    '''
    This function returns true if the given text contains any Garshuni characters.
    '''
    def contains_garshuni(self, text):
        for c in text:
            if c in self.GARSHUNI:
                return True
        return False
    
    '''
    This function returns true if the given text contains any non-vowel diacritics.
    '''
    def contains_non_vowel_diacritics(self, text):
        for c in text:
            if c in self.NON_VOWEL_DIACRITICS:
                return True
        return False
    
    '''
    This function removes all decorative characters from the given text.
    '''
    def remove_decorative_chars(self, text):

        if f'{self.LETTER_DOTLESS_DALATH_RISH}{self.COMBINING_DIAERESIS}' in text:
            text = text.replace(f'{self.LETTER_DOTLESS_DALATH_RISH}{self.COMBINING_DIAERESIS}', 'ܪ')

        return ''.join([c for c in text if not (c in self.DECORATIVE)])

    '''
    Removes one particular diacritic from 'text'.
    '''
    def remove_diacritic(self, diacritic, text):
        return text.replace(diacritic, '')

    def remove_siyame(self, text):
        return text.replace(self.COMBINING_DIAERESIS, '')
    
    '''
    Remove all unvocalized characters from the given text.
    '''
    def remove_unvocalized(self, text):
        return ''.join([c for c in text if not (c in self.UNVOCALIZED)])
    
    def handle_abreviations_and_contractions(self, text):
        replacements = [
            ['܏ܩܛ', 'ܩܲܕ݇ܡ ܛܲܗܪܵܐ'],
            ['܏ܒܛ', 'ܒܲܬ݇ܪ ܛܲܗܪܵܐ'],
            ['ܩܫ܊', 'ܩܵܫܝܼܫܵܐ'],
        ]

        for old, new in replacements:
            text = text.replace(old, new)
        
        text = text.replace(self.ABBREVIATION_MARK, '')
        text = text.replace(self.CONTRACTION, '')
        return text

    def handle_quiescent_letters(self, text):
        """
        Handle Matis Lectionis
        """
        if text[0:3] == f'{self.LETTER_ALAPH}{self.LETTER_WAW}{self.HBASA_ESASA_DOTTED}' \
        or text[0:3] == f'{self.LETTER_ALAPH}{self.LETTER_WAW}{self.RWAHA}':
            text = text[1:]
        
        final_char = ''
        if text[-1] in self.PUNCTUATION:
            final_char = text[-1]
            text = text[:-1]

        """
        Remove final glottal stop if a non-matis vowel precedes an Alap and vice-versa
        """
        # find index of the last letter or vowel
        index = len(text) - 1
        while text[index] not in self.LETTER and text[index] not in self.VOWEL and index > 0:
            index -= 1
        if text[index] == self.LETTER_ALAPH:    
            if len(text) >= 2 and text[index - 1] in self.NON_MATIS_VOWEL:
                text = text[:-1]

        if len(text) >= 1 and text[0] == f'{self.LETTER_ALAPH}' and text[1] in self.NON_MATIS_VOWEL:
            text = text[1:]
        
        if len(text) > 1 and text[0] == f'{self.LETTER_ALAPH}' and not (text[1] in self.VOWEL):
            text = text[1:]
        
        return text + final_char
    
    def apply_matis_lectionis(self, text):
        """
        Apply Matis Lectionis
        """
        text = text.replace(f'{self.LETTER_WAW}{self.HBASA_ESASA_DOTTED}', 'ū')
        text = text.replace(f'{self.LETTER_WAW}{self.RWAHA}', 'o')
        
        ## Shorten Yudh+Khwasa to i in constrained by two unvocalized letters
        index = text.find(f'{self.LETTER_YUDH}{self.HBASA_ESASA_DOTTED}')
        if index != -1:
            if ((index > 0 and text[index - 1] in self.VOWEL) or \
                (len(text) > index + 3 and text[index + 2] in self.LETTER and text[index + 3] in self.VOWEL)):
                text = text[:index] + 'ī' + text[index+2:]
            else:
                text = text[:index] + 'i' + text[index+2:]

        return text
    
    """
    Main method that takes a Syriac string and returns a dict with:
    {
        'latin': <transliterated version>,
        'phonetic': <phonetic approximation>
    }
    
    This method is split into smaller steps for clarity.
    """
    def transliterate(self, text):
        """
        Takes a Syriac string and returns a dict:
        {
           'latin': <transliterated string>,
           'phonetic': <phonetic approximation>
        }
        """
        translit_text = ''
        phonetic_text = ''
        words = text.split()

        for word in words:
            word = unicodedata.normalize('NFC', word)
            
            word = self.remove_decorative_chars(word)

            word = self.handle_abreviations_and_contractions(word)

            word = self.remove_unvocalized(word)

            word = self.apply_special_cases(word)

            word = self.remove_talqaneh_clusters(word)
            word = self.handle_quiescent_letters(word)
            word = self.apply_bdul_prefixes(word)
            word = self.apply_consonant_doubling(word)
            word = self.remove_siyame(word)
            word = self.apply_matis_lectionis(word)

            latin_transliteration = self.convert_syriac_to_latin(word)
            translit_text += latin_transliteration + ' '

            phonetic_text += self.make_phonetic_approx(latin_transliteration) + ' '

        translit_text = translit_text.strip()
        phonetic_text = phonetic_text.strip()
        
        return {
            'latin': translit_text,
            'phonetic': phonetic_text
        }

    def apply_bdul_prefixes(self, text):
        if len(text) > 4 and text[0] in self.BDOL_LETTERS and text[1] not in self.VOWEL:
                if not (text[1] == self.LETTER_WAW and text[2] in self.MATIS_VOWEL) and \
                   not (text[1] == self.LETTER_YUDH and text[2] in self.MATIS_VOWEL) or \
                   text[1] in self.LETTER and not (text[2] in self.VOWEL):
                    text = f"{text[0]}'{text[1:]}"
        return text

    def apply_consonant_doubling(self, text):
       # TODO: Implement this method
        return text

    # --------------------------------------------------------------------------
    # Convert to Latin (core BGDKPT, Majleana, vowels, etc.)
    # --------------------------------------------------------------------------
    def convert_syriac_to_latin(self, text):
        """
        Main letter-by-letter (plus diacritic) transliteration.
        Replaces BGDKPT with qushshaya/rukkakha forms, etc.
        """

        # 1) Handle “Majleana” or “softening” combos
        text = text.replace(f"ܟ{self.COMBINING_TILDE_ABOVE}", 'č')
        text = text.replace(f"ܟ{self.COMBINING_TILDE_BELOW}", 'č')
        text = text.replace(f"ܓ{self.COMBINING_TILDE_BELOW}", 'j')
        text = text.replace(f"ܫ{self.COMBINING_TILDE_BELOW}", 'ž')
        text = text.replace(f"ܫ{self.COMBINING_TILDE_ABOVE}", 'ž')
        # If you also handle ܙ + tilde => ž
        text = text.replace(f"ܙ{self.COMBINING_TILDE_ABOVE}", 'ž')
        text = text.replace(f"ܙ{self.COMBINING_TILDE_BELOW}", 'ž')

        # 2) BGDKPT + Rukkakha
        text = text.replace(f"ܒ{self.RUKKAKHA}", 'ḇ')
        text = text.replace(f"ܓ{self.RUKKAKHA}", 'ḡ')
        text = text.replace(f"ܕ{self.RUKKAKHA}", 'ḏ')
        text = text.replace(f"ܟ{self.RUKKAKHA}", 'ḵ')
        text = text.replace(f"ܦ{self.RUKKAKHA}", 'f')
        # Some texts also use combining breve below for "f"
        text = text.replace(f"ܦ{self.COMBINING_BREVE_BELOW}", 'f')
        text = text.replace(f"ܬ{self.RUKKAKHA}", 'ṯ')

        # 3) BGDKPT + Qushshaya
        text = text.replace(f"ܒ{self.QUSHSHAYA}", 'b')
        text = text.replace(f"ܓ{self.QUSHSHAYA}", 'g')
        text = text.replace(f"ܕ{self.QUSHSHAYA}", 'd')
        text = text.replace(f"ܦ{self.QUSHSHAYA}", 'p')
        text = text.replace(f"ܟ{self.QUSHSHAYA}", 'k')
        text = text.replace(f"ܬ{self.QUSHSHAYA}", 't')

        # 4) Base mapping (letters with no diacritics)
        base_map = {
            'ܐ': self.GLOTTAL_STOP,
            'ܒ': 'b',
            'ܓ': 'g',
            'ܔ': 'j',
            'ܕ': 'd',
            'ܗ': 'h',
            'ܘ': 'w',
            'ܙ': 'z',
            'ܚ': 'ḥ',
            'ܛ': 'ṭ',
            'ܝ': 'y',
            'ܟ': 'k',
            'ܠ': 'l',
            'ܡ': 'm',
            'ܢ': 'n',
            'ܣ': 's',
            self.LETTER_FINAL_SEMKATH: 's',
            'ܥ': self.PHARYNGEAL,    # ʿ
            'ܦ': 'p',
            'ܨ': 'ṣ',
            'ܩ': 'q',
            'ܪ': 'r',
            'ܫ': 'š',
            'ܬ': 't',
        }

        # Convert each character via base_map when possible
        out = []
        for ch in text:
            if ch in base_map:
                out.append(base_map[ch])
            else:
                out.append(ch)
        text = ''.join(out)

        # 5) Convert vowels
        text = text.replace(self.DOTTED_ZLAMA_ANGULAR, "ē")
        text = text.replace(self.DOTTED_ZLAMA_HORIZONTAL, "i")
        text = text.replace(self.PTHAHA_DOTTED, "a")
        text = text.replace(self.ZQAPHA_DOTTED, "ā")
        text = text.replace(self.HBASA_ESASA_DOTTED, "ə")

        return text

    # --------------------------------------------------------------------------
    # Final “phonetic” expansions, e.g. š => sh, ḥ => kh, etc.
    # --------------------------------------------------------------------------
    def make_phonetic_approx(self, text):
        """Applies your final expansions for a more “English-like” approximation."""
        phon_map = {
            'š': 'sh',
            'ḥ': 'kh',
            'ž': 'zh',
            'ḇ': 'w',
            'ṯ': 'th',
            'ḏ': 'dh',
            'ḵ': 'kh',
            'ḡ': 'gh',
            'ē': 'eh',    # or “e”
            'ī': 'ee',
            'ā': 'a',
            'ū': 'u',
            self.GLOTTAL_STOP: "'",
            self.PHARYNGEAL: '`',
        }
        result = []
        l = 0
        for ch in text:
            if ch in phon_map:
                result.append(phon_map[ch])
            else:
                if l == len(text) - 1 and ch == 'h':
                    pass # Drop final “h”
                else:
                    result.append(ch)
            l += 1
        return ''.join(result)

    def apply_special_cases(self, text):
        # Example: remove some specific substring or reorder if needed
        # Suppose you have a list of special pairs:
        special_replacements = [
            ['ܝܼܗܘܼܕ', 'īhud'],
            ['ܝܼܚܝܼܕܘܼܬܵܐ', 'īḥīdutā'],
            ['ܝܼܣܲܪ', 'īsar'],
            ['ܝܼܠܝܼܕܘܼܬܵܐ', 'īlidutā'],
            ['ܝܼܕܵܥ', 'īdāʿ'],
            [f'ܒܗ{self.COMBINING_DOT_ABOVE}ܝ', 'b\'ay'],
            [f'ܗ{self.COMBINING_DOT_ABOVE}ܝ', 'aya'],
            [f'ܗ{self.COMBINING_DOT_ABOVE}ܘ', 'awa'],
            [f'ܡ{self.COMBINING_DOT_ABOVE}ܢ', 'man'],
            [f'ܡ{self.COMBINING_DOT_BELOW}ܢ', 'min'],
            ['ܒܵܬܹܐ', 'bāttē'],
            ['ܟ̰ܵܐܝ', 'čāy'],
            ['ܒܵܐܝ', 'bāy'],
            ['ܐܲܦ̮ܘܿܟܵܕ', 'avokād'],
            ['ܝܼܫܘܿܥ', 'īšoʿ'],
            ['ܢܲܦ̮ܫ', 'noš'],
            ['ܘܼܦ̮', 'ܘܼ'],
            ['ܠܹܗ', 'lēh'],
            ['ܝܘܸܢ', 'ìwen'],
            ['ܝܘܵܢ', 'ìwān'],
            ['ܝܘܲܚ', 'ìwaḥ'],
            ['ܝܘܸܬ', 'ìwet'],
            ['ܝܘܵܬܝ', 'ìwāt'],
            ['ܝܬܘܿܢ', 'ìton'],
            ['ܝܠܹܗ', 'ìlēh'],
            ['ܝܠܵܗ̇', 'ìlāh'],
            ['ܝܢܵܐ', 'ìnā'],
            ['ܝܗ݇ܘܵܐ', 'ìwā'],
            ['ܝܗ݇ܘܵܬ݇', 'ìwā'],
            ['ܝܗ݇ܘܵܘ', 'ìwā'],
            ['ܝܼܘܸܢ', 'īwen'],
            ['ܝܼܘܵܢ', 'īwān'],
            ['ܝܼܘܸܬ', 'īwet'],
            ['ܝܼܘܵܬܝ', 'īwāt'],
            ['ܝܼܠܹܗ', 'īlēh'],
            ['ܝܼܠܵܗ̇', 'īlāh'],
            ['ܝܼܘܲܚ', 'īwaḥ'],
            ['ܝܼܬܘܿܢ', 'īton'],
            ['ܝܼܢܵܐ', 'īnā'],
            ['ܝܼܗ݇ܘܵܐ', 'īwā'],
            ['ܝܼܗ݇ܘܵܘ', 'īwā'],
            ['ܗ݇ܘܝܼ', 'wī'],
            ['ܗ݇ܘܹܝܡܘܼܢ', 'wēmun'],
            ['ܗ݇ܘܵܐ', 'wā'],
            ['ܗ݇ܘܵܘ', 'wā'],
            ['ܗ݇ܘܹܐ', 'wē'],
            ['ܟܠ', 'kul'],
            ['ܟܠܵܢ', 'kullān'],
            ['ܟܠܘܼܟ݂', 'kulloḵ'],
            ['ܟܠܵܟ݂ܝ', 'kullāḵ'],
            ['ܟܠܹܗ', 'kullēh'],
            ['ܟܠܵܗ̇', 'kullāh'],
            ['ܟܠܘܼܗܝ', 'kulluh'],
            ['ܟܠܘܿܗ̇', 'kulloh'],
            ['ܟܠܲܢ', 'kullan'],
            ['ܟܠܵܘܟ݂ܘܿܢ', 'kullāwḵon'],
            ['ܟܠܵܝܗܝ', 'kullāyh'],
            ['ܟܠܗܘܿܢ', 'kullhon'],
            ['ܟܠܵܢܵܐܝܼܬ', 'kullānāʾīt'],
            ['ܟܠܵܢܵܐܝܼܬ݂', 'kullānāʾīṯ'],
            ['ܟܠܵܢܵܝ', 'kullānāy'],
            ['ܟܘܿܠܵܝ', 'kollāy'],
            ['ܟܠܚܲܕ݇', 'kulḥa'],
            ['ܟܠܚܕ݂ܵܐ', 'kulḥḏā'],
            ['ܟܠܫܲܢ݇ܬ', 'kulšat'],
            ['ܝܲܐܠܵܗ', 'yallāh'],
            ['ܘܲܐܠܵܗ', 'wallāh'],
            ['ܙܹܠ݇ܝ', 'zē'],
            ['ܬܵܐܝ', 'tā'],
            [self.LETTER_YUDH_HE, 'yah'],
        ]

        for old, new in special_replacements:
            index = text.find(old)
            if len(old) == len(text) and old in text:
                text = text.replace(old, new)
            elif len(text) > index + len(old) and not (text[index + len(old)] in self.VOWEL):
                text = text.replace(old, new)
        return text