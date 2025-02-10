# Assyrian Digital Language Consortium Transliterator

This project is developed by the **Assyrian Digital Language Consortium** and provides tools for transliterating Syriac text into IPA (International Phonetic Alphabet) and romanized forms. The transliterator is designed with dialectal variation in mind, making it possible to override default mappings with dialect-specific JSON files.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
  - [Basic Transcription](#basic-transcription)
  - [Loading Dialect Overrides](#loading-dialect-overrides)
- [Testing](#testing)
- [Contributing](#contributing)

## Features

- **Transliteration:** Converts Syriac text into IPA and then to romanized output.
- **Dialect Overrides:** Easily load custom mapping files (in JSON format) to adjust the transliteration for dialect-specific pronunciation.
- **Reverse Transliteration:** Converts IPA back to Syriac script using inverted mappings.
- **Extensibility:** Built on top of a base toolset (`SyrTools`) with clearly separated mapping dictionaries and phonetic rules.
- **Testing:** Integrated unit tests using `pytest`.

## Requirements

- **Python 3.8+**  
- **pip** for installing dependencies  
- Optionally, **pytest** for running tests

```python
pip install -r requirements.txt
```

## Usage

The core functionality is exposed via the SyrTransliterator class, located in the src/SyrTransliterator.py file.

### Basic Transcription

Here’s an example of how to transliterate Syriac text using the default mappings:

```python
from SyrTransliterator import SyrTransliterator

# Instantiate the transliterator (using default mappings)
transliterator = SyrTransliterator()

text = "ܒܨܲܦܪܵܐ ܟܹܐ ܟܵܬ݂ܒ݂ܹܢ ܐܸܓܪ̈ܵܬ݂ܵܐ"
result = transliterator.transliterate(text)

print("IPA:", result["ipa"])
print("Natural IPA:", result["natural_ipa"])
print("Romanized:", result["romanized"])
```

Output:
```
python3 examples/basic_transliterator.py
IPA: bsˤaprɑʔ keʔ kɑθven ʔɪgrɑθɑʔ
Natural IPA: bsˤaprɑʔ keʔ kɑθven ʔɪgrɑθɑ
Romanized: b'ṣapra ke kathwen igratha
```

### Loading Dialect Overrides

A method for overriding dialects is possible via the dialect JSON mappings in src/dialects, where the romanized IPA phonemes can be manipulated to better suit a dialect.

To support dialect-specific rules (e.g., the Iranian Koine dialect), you can supply JSON mapping files when creating the SyrTransliterator instance. These files override parts of the default mapping for IPA symbols, vowels, and consonants.

For example:
```python
from SyrTransliterator import SyrTransliterator

iranian_koine_file = f'{src_dir}/dialects/iranian_koine.json'
transliterator = SyrTransliterator(dialect_map_filename=iranian_koine_file)

text = "ܒܨܲܦܪܵܐ ܟܹܐ ܟܵܬ݂ܒ݂ܹܢ ܐܸܓܪ̈ܵܬ݂ܵܐ"
result = transliterator.transliterate(text)

print("IPA:", result["ipa"])
print("Natural IPA:", result["natural_ipa"])
print("Romanized:", result["romanized"])
```

Output:
```
IPA: bsˤaprɑʔ keʔ kɑθven ʔɪgrɑθɑʔ
Natural IPA: bsˤaprɑʔ keʔ kɑθven ʔɪgrɑθɑ
Romanized: b'ṣapra ke katven igrata
```

## Testing

Unit tests are implemented using pytest. To run the tests:
```
pytest tests
```

Full linting, refactoring, and testing is done via:
```
./run_tests.sh
```

## Contributing

Contributions are welcome! If you have ideas for improvements, bug fixes, or additional dialect mapping files, please:

- Fork the repository.
- Create a feature branch.
- Run run_tests.sh to lint, refactor, and test your changes. Git add any new refactor changes that may have been introduced after running the command.
- Submit a pull request with your changes.
- Open issues for any bugs or feature requests.

Please follow the project’s coding style and include appropriate tests with your contributions.
