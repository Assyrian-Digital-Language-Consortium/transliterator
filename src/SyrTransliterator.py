"""
' @file SyrTransliterator.py
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
"""

from SyrTools import SyrTools


class SyrTransliterator(SyrTools):
    def __init__(self):
        super().__init__()

        self.ipa_to_roman_map = {
            # Rukakheh & Qushayeh
            "v": "w",
            "ɣ": "gh",
            "ð": "dh",
            "x": "kh",
            "f": "f",
            "θ": "th",
            "g": "g",
            "d": "d",
            "k": "k",
            "p": "p",
            "t": "t",
            # Majleaneh
            "ʤ": "j",
            "ʒ": "zh",
            "tʃ": "ch",
            # Mater Lectionis
            "u": "u",
            "o": "o",
            "i": "i",
            # Consonants
            "ʔ": "'",
            "b": "b",
            "g": "g",
            "d": "d",
            "h": "h",
            "w": "w",
            "z": "z",
            "ḥ": "kh",
            "tˤ": "ṭ",
            "j": "y",
            "k": "k",
            "l": "l",
            "m": "m",
            "n": "n",
            "s": "s",
            "ʕ": "ʿ",
            "p": "p",
            "sˤ": "ṣ",
            "q": "q",
            "r": "r",
            "ʃ": "sh",
            # Eastern Vowels
            "a": "a",
            "ɑ": "a",
            "ɪ": "i",
            "e": "e",
            # Western Vowels
            "o": "o",
            "u": "u",
        }

        self.punctuation_replacements = {"؟": "?", "،": ",", "؛": ";"}

        self.ipa_vowels = (
            list(self.eastern_vowel_ipa_map.values())
            + list(self.western_vowel_ipa_map.values())
            + list(self.mater_lectionis_ipa_map.values())
        )

        self.ipa_bdol = ("b", "d", "w", "l")
        self.ipa_mater_lectionis = list(self.mater_lectionis_ipa_map.values())

    """
    This function removes all decorative characters from the given text.
    """

    def remove_decorative_chars(self, text):
        return "".join([c for c in text if not (c in self.DECORATIVE)])

    def remove_siyame(self, text):
        return text.replace(self.COMBINING_DIAERESIS, "")

    def handle_abbreviations_and_contractions(self, text):

        eastern_replacements = [
            ["܏ܩܛ", "ܩܲܕ݇ܡ ܛܲܗܪܵܐ"],
            ["܏ܒܛ", "ܒܲܬ݇ܪ ܛܲܗܪܵܐ"],
            ["ܩܫ܊", "ܩܵܫܝܼܫܵܐ"],
        ]

        if self.eastern(text):
            for old, new in eastern_replacements:
                text = text.replace(old, new)

        text = text.replace(self.ABBREVIATION_MARK, "")
        text = text.replace(self.CONTRACTION, "")
        return text

    def transliterate(self, text):
        lossless_ipa_text = self.encode_ipa(text)
        lossless_ipa_text = self.remove_siyame(lossless_ipa_text)

        phonetic_ipa_text = self.naturalize_ipa(lossless_ipa_text)

        return {
            "ipa": lossless_ipa_text,
            "natural_ipa": phonetic_ipa_text,
            "romanized": self.ipa_to_roman(phonetic_ipa_text),
        }

    # returns the given subtoken in token which belongs set_type
    def get_subtoken_of_type(self, token, set_type):
        s = ""
        for t in token:
            if t in set_type:
                s += t
        return s

    def tokenize_cluster(self, cluster):
        token_str = (
            self.get_subtoken_of_type(cluster, self.LETTER)
            + self.get_subtoken_of_type(cluster, self.SIYAMEH)
            + self.get_subtoken_of_type(cluster, self.QUSHAYEH)
            + self.get_subtoken_of_type(cluster, self.RUKAKHEH)
            + self.get_subtoken_of_type(cluster, self.MAJLEANEH)
            + self.get_subtoken_of_type(cluster, self.VOWEL)
            + self.get_subtoken_of_type(cluster, self.QANUNEH)
        )

        if len(self.get_subtoken_of_type(cluster, self.TALQANEH)) > 0:
            token_str = f"[{token_str}]"

        for key in self.mater_lectionis_ipa_map:
            token_str = token_str.replace(
                key, self.mater_lectionis_ipa_map[key]
            )

        for key in self.rukakheh_qushayeh_ipa_map:
            token_str = token_str.replace(
                key, self.rukakheh_qushayeh_ipa_map[key]
            )

        for key in self.majleaneh_ipa_map:
            token_str = token_str.replace(key, self.majleaneh_ipa_map[key])

        for key in self.consonant_ipa_map:
            token_str = token_str.replace(key, self.consonant_ipa_map[key])

        for key in self.eastern_vowel_ipa_map:
            token_str = token_str.replace(key, self.eastern_vowel_ipa_map[key])

        return f"{token_str}"

    def naturalize_ipa(self, ipa):
        vowels = list(self.eastern_vowel_ipa_map.values()) + list(
            self.mater_lectionis_ipa_map.values()
        )

        """
        Convert IPA to a more naturalized pronunciation by applying
        pronunciation rules.
        """
        ipa_chars = list(ipa)  # Convert to list for easy modification

        # Remove initial ʔ if followed by 'i', 'u', or 'o'
        glottal_stop_ipa = self.consonant_ipa_map["ܐ"]
        if (
            ipa_chars
            and ipa_chars[0] == glottal_stop_ipa
            and len(ipa_chars) > 1
            and ipa_chars[1] in vowels
        ):
            ipa_chars.pop(0)  # Remove first ʔ

        # Remove final ʔ if preceded by 'a', 'ɑ', 'ɪ', or 'e'

        short_vowels = {
            self.eastern_vowel_ipa_map[self.PTHAHA_DOTTED],
            self.eastern_vowel_ipa_map[self.ZQAPHA_DOTTED],
            self.eastern_vowel_ipa_map[self.DOTTED_ZLAMA_HORIZONTAL],
            self.eastern_vowel_ipa_map[self.DOTTED_ZLAMA_ANGULAR],
        }

        if (
            len(ipa_chars) > 1
            and ipa_chars[-1] == glottal_stop_ipa
            and ipa_chars[-2] in short_vowels
        ):
            ipa_chars.pop()

        # Convert 'i' to 'ɪ' if sandwiched between two unvocalized consonants
        for j in range(1, len(ipa_chars) - 1):
            if (
                ipa_chars[j] == self.mater_lectionis_ipa_map["ܝܼ"]
                and ipa_chars[j - 1] not in vowels
                and ipa_chars[j + 1] not in vowels
            ):
                ipa_chars[j] = self.eastern_vowel_ipa_map[
                    self.DOTTED_ZLAMA_HORIZONTAL
                ]  # Change 'i' to 'ɪ'

        return "".join(ipa_chars)  # Convert back to string

    # Tokenize a word by Consonant+Diacritic+Vocalization
    def tokenize_word(self, word):
        ret_tokens = ""
        cluster = [word[0]]
        for c in word[1:]:
            if c not in self.LETTER:
                cluster.append(c)
            else:
                # create a sub-token in consonant, majleana, diacritic,
                # vocalization order
                ret_tokens += self.tokenize_cluster(cluster)
                cluster = [c]
        ret_tokens += self.tokenize_cluster(cluster)

        return f"{ret_tokens}"

    def split_syriac_text(self, text):
        """Splits a Syriac text into isolated words and punctuation."""
        result = []
        word = ""

        for char in text:
            if char in self.PUNCTUATION or char.isspace():
                if word:
                    result.append(word)  # Store the word collected so far
                    word = ""
                if char in self.PUNCTUATION or char.isspace():
                    result.append(
                        self.replace_punctuation(char)
                    )  # Store punctuation as a standalone element
            else:
                word += char  # Keep building a word

        if word:  # Add the last collected word if any
            result.append(word)

        return result

    def split_ipa_text(self, text):
        result = []
        word = ""
        punctuations = [",", ":", ";", "!", ".", "-", "<", ">", "?", "'", '"']
        for char in text:
            if char in punctuations or char.isspace():
                if word:
                    result.append(word)  # Store the word collected so far
                    word = ""
                if char in punctuations or char.isspace():
                    result.append(char)  # Store punctuation
            else:
                word += char  # Keep building a word

        if word:  # Add the last collected word if any
            result.append(word)

        return result

    def encode_ipa(self, text):
        words = self.split_syriac_text(text)
        ipastr = ""
        for word in words:
            if word not in self.PUNCTUATION and not word.isspace():
                word = self.remove_decorative_chars(word)
                word = self.handle_abbreviations_and_contractions(word)
                word = self.apply_special_cases(word)
                word = self.tokenize_word(word)

            ipastr += word
        return ipastr

    def apply_bdol_prefixes(self, text):
        split_ipa = self.split_ipa_text(text)
        bdolized_str = ""
        for tok in split_ipa:
            if (
                len(tok) > 1
                and tok[0] in self.ipa_bdol
                and tok[1] not in self.ipa_vowels
            ):
                bdolized_str += f"{tok[0]}'{tok[1:]}"
            else:
                bdolized_str += tok
        return bdolized_str

    def handle_glottals(self, text):
        split_ipa = self.split_ipa_text(text)
        filtered_str = ""
        for tok in split_ipa:
            if (
                tok[0] == self.consonant_ipa_map["ܐ"]
                or tok[0] == self.consonant_ipa_map["ܑ"]
            ):
                filtered_str += tok[1:]
            elif (
                tok[-1] == self.consonant_ipa_map["ܐ"]
                or tok[-1] == self.consonant_ipa_map["ܑ"]
            ):
                filtered_str += tok[:-1]
            elif (
                tok[0] == self.consonant_ipa_map["ܐ"]
                or tok[0] == self.consonant_ipa_map["ܑ"]
            ) and (
                tok[-1] == self.consonant_ipa_map["ܐ"]
                or tok[-1] == self.consonant_ipa_map["ܑ"]
            ):
                filtered_str += tok[1:-1]
            else:
                filtered_str += tok
        return filtered_str

    def replace_punctuation(self, mark):
        for key in self.punctuation_replacements.keys():
            mark = mark.replace(key, self.punctuation_replacements[key])
        return mark

    def apply_special_cases(self, word):
        special_phonetic_replacements = [
            ["ܗ̇ܘ", "ܐܵܘܵ"],
            ["ܗ̇ܝ", "ܐܵܝܵ"],
            ["ܝܠܵܗ̇", "ܝܼܠܵܗ"],
            ["ܝܠܗ̇", "ܝܼܠܵܗ"],
            ["ܝܠܗ", "ܝܼܠܹܗ"],
            ["ܝܠܹܗ", "ܝܼܠܹܗ"],
            ["ܗ̇", "ܗ"],
            ["ܡ̇ܢ", "ܡܵܢ"],
            ["ܡ̣ܢ", "ܡܸܢ"],
            ["ܢܲܦ̮ܫ", "ܢܲܘܫ"],
            ["ܟܠ", "ܟܘܼܠ"],
            ["ܟܠܢ", "ܟܘܼܠܵܢ"],
        ]

        for old, new in special_phonetic_replacements:
            index = word.find(old)
            if old in word:
                if len(old) == len(word):
                    word = word.replace(old, new)
                elif len(word) >= index + len(old):
                    if (
                        len(word) > index + len(old)
                        and word[index + len(old)] in self.VOWEL
                    ):
                        pass
                    else:
                        word = word.replace(old, new)

        return word

    def remove_bracketed_content(self, ipa_text):
        """
        Removes characters inside square brackets, including the brackets
        themselves.
        """
        result = []
        inside_brackets = False
        for char in ipa_text:
            if char == "[":
                inside_brackets = True
            elif char == "]":
                inside_brackets = False
            elif not inside_brackets:
                result.append(char)
        return "".join(result)

    def ipa_to_roman(self, ipa_text):
        ipa_text = self.remove_bracketed_content(ipa_text)
        ipa_text = self.apply_bdol_prefixes(ipa_text)
        ipa_text = self.handle_glottals(ipa_text)

        """Convert an IPA transcription to Romanized phonemes."""
        result = []
        i = 0
        while i < len(ipa_text):
            found = False
            # Check for multi-character IPA sequences (longest match first)
            for length in [3, 2, 1]:  # Handle digraphs like "tʃ"
                if i + length <= len(ipa_text):
                    segment = ipa_text[i : i + length]
                    if segment in self.ipa_to_roman_map:
                        result.append(self.ipa_to_roman_map[segment])
                        i += length
                        found = True
                        break
            if not found:
                result.append(ipa_text[i])  # Keep unknown characters as-is
                i += 1
        return "".join(result)

    def invert_dict(self, d):
        """Invert a dictionary so that values become keys and vice versa.
        Handles multiple keys mapping to the same value by making lists.
        """
        inverted = {}
        for key, value in d.items():
            if value in inverted:
                inverted[value].append(key)
            else:
                inverted[value] = [key]
        return inverted

    def reverse_transliterate(self, ipa_text, eastern=True):
        if not ipa_text:
            return ""

        # Inverting all mappings
        ipa_to_syriac_map = {}
        if eastern:
            for original_map in [
                self.rukakheh_qushayeh_ipa_map,
                self.majleaneh_ipa_map,
                self.mater_lectionis_ipa_map,
                self.consonant_ipa_map,
                self.eastern_vowel_ipa_map,
                self.punctuation_replacements,
            ]:
                ipa_to_syriac_map.update(self.invert_dict(original_map))
        else:
            for original_map in [
                self.rukakheh_qushayeh_ipa_map,
                self.majleaneh_ipa_map,
                self.mater_lectionis_ipa_map,
                self.consonant_ipa_map,
                self.western_vowel_ipa_map,
                self.punctuation_replacements,
            ]:
                ipa_to_syriac_map.update(self.invert_dict(original_map))

        """
        Convert an IPA transcription to Syriac script using the generated
        mapping.
        """
        result = []
        i = 0
        while i < len(ipa_text):
            found = False
            # Check for multi-character IPA sequences (longest match first)
            for length in [3, 2, 1]:  # Handle digraphs like "tʃ"
                if i + length <= len(ipa_text):
                    segment = ipa_text[i : i + length]
                    if segment in ipa_to_syriac_map:
                        result.append(
                            ipa_to_syriac_map[segment][0]
                        )  # Choose first if multiple
                        i += length
                        found = True
                        break
            if not found:
                result.append(ipa_text[i])  # Keep unknown characters as-is
                i += 1

            syr_text = "".join(result)

            result = []
            inside_brackets = False
            for char in syr_text:
                if char == "[":
                    inside_brackets = True
                elif char == "]":
                    if not inside_brackets:
                        result.append(self.OBLIQUE_LINE_ABOVE)
                    inside_brackets = False
                elif not inside_brackets:
                    result.append(char)
        return "".join(result)
