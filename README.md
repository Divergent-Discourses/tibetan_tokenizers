# Description

This repository contains tokenization utilities for Tibetan, based on various external tokenizers. `botok_tokenizer.py` uses [BoTok, a tokenizer developed by OpenPecha](https://github.com/OpenPecha/Botok). Tokenization separates raw text into machine-readable lists of individual words for subsequent NLP tasks. 

## Usage

`botok_tokenizer.py` is input agnostic, and can interpret either directories or individual files. If a directory is input, all text files in that directory will be tokenized and stored at the directory level holding `botok_tokenizer.py`. 

With `botok_tokenizer.py` at the same level of file structure as the desired input, call it from the command line with the following template:

`python3 botok_tokenizer.py <input_path> <output_path>`

Note: do not include the angle brackets in actual usage. 
