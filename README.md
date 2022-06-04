## Package to convert Nepali text to romanized English.

[![Downloads](https://pepy.tech/badge/nepali-to-roman)](https://pepy.tech/project/nepali-to-roman) 

While working with many Nepali documents, we encountered lots of data of Nepali names which includes names, surname, address and numbers.
Extracting the data was not a easy task but working with its romanize transliteration was hard.

Many different packages are created for transliteration but they were not quite accurate.

This package contains large amount of Nepali literals and words which are mapped to its respective romanized literal and word.

But that was not the challenging part, still it was not giving the accurate result for instance
"नेपाल" was showing Nepala as the "ल" is mapped as "la".
So we have worked with these type of issues also.

## Installation
`nepali-to-roman` package is available for `Python 3` and can be installed using `pip`. 

First make sure [`pip`](https://pip.pypa.io/en/stable/installing/) is installed.

Then, the package can be installed using this command.
```
pip install nepali-to-roman
```

## Usage

Import the `ntr` module using the following command.
```python
import ntr 
```
The `ntr` module has one function: nep_to_rom

**Detail description**:
Every words of a sentences are broken down into list and are transliterated individually which are later merged into single string.

Syntax:
```python
>>> ntr.nep_to_rom(text)
```

Example:
```python
>>> import ntr
>>> print(ntr.nep_to_rom("म नेपाल मा बस्छु ।"))
Output: ma nepal ma baschhu .


```

## Contributions

The package is licenced with The MIT License (MIT) about which details can be found in the [LICENSE](LICENSE) file. As
the package is open sourced and requires many improvements and extensions, any contributions are welcome. Any other
feedback of any sort are highly welcome.

## About Contributors
['Diwas Pandey'](https://www.diwaspandey.com.np) 
</br>
['Ishparsh Uprety](https://www.ishparshuprety.com.np/)
