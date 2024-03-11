# Description

This repository contains a tokenization (word segmentation) utility for Tibetan. It is based on [BoTok, a tokenizer developed by OpenPecha](https://github.com/OpenPecha/Botok). Tokenization separates raw text into machine-readable lists of individual words for subsequent NLP tasks. Botok aims to work on both modern and classical Tibetan and also provides PoS tags for Tibetan. With Botok you have to turn every file into a string, whereas `botok_tokenizer.py` simplifies that process by allowing you to point to a whole folder/directory or a single .txt file. It also selects just the tokenizer element of Botok, rather than the PoS tagger element, which we have not incldued in this utility. To run the tokenizer, place the raw text files in a folder and then run `botok_tokenizer.py`. 

## Usage

`botok_tokenizer.py` is input agnostic, and can interpret either directories or individual files. If a directory is input, all text files in that directory will be tokenized and stored at the directory level holding `botok_tokenizer.py`. 

With `botok_tokenizer.py` at the same level of file structure as the desired input, call it from the command line with the following template:

`python3 botok_tokenizer.py <input_path> <output_path>`

Note: do not include the angle brackets in actual usage. 

This script simplifies the process of tokenization by allowing files or directories to be passed into BoTok's tokenizer as inputs, rather than strings.  
