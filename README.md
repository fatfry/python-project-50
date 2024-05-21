# Difference generator


### Hexlet tests and linter status:
[![hexlet-check](https://github.com/fatfry/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/fatfry/python-project-50/actions/workflows/hexlet-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/6d00a5cc809dc6d9461c/maintainability)](https://codeclimate.com/github/fatfry/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6d00a5cc809dc6d9461c/test_coverage)](https://codeclimate.com/github/fatfry/python-project-50/test_coverage)
## Description


Difference generator is a program that determines difference between two data structures.
Supported formats:  ```json```, ```yml``` and ```yaml```.


## Installation


Clone the repository and use this commands:

```
make install
make build
make package-install
```

## Usage
```
usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                         select format of output from [stylish, plain, json]
```

### Comparison of flat files (JSON)

`gendiff file1.json file2.json`

[![asciicast](https://asciinema.org/a/rRMsv3vhYJfAqnZqBBPjKc0XZ.svg)](https://asciinema.org/a/rRMsv3vhYJfAqnZqBBPjKc0XZ)### Comparison of flat files (YAML, YML)

`gendiff file1.yml file2.yml`

[![asciicast](https://asciinema.org/a/dTzMIdYUNRERfeHlR7DEz5thO.svg)](https://asciinema.org/a/dTzMIdYUNRERfeHlR7DEz5thO)
`gendiff nested_file1.json nested_file2.json`

[![asciicast](https://asciinema.org/a/V1rgYC6F1ALe8NwAVSS4iZMZh.svg)](https://asciinema.org/a/V1rgYC6F1ALe8NwAVSS4iZMZh)

### Comparison of two files with a nested structure (YML, YAML)

`gendiff nested_file1.yml nested_file2.yml`

[![asciicast](https://asciinema.org/a/PF9ipTUJMJ0B86my9Hlke2Qdj.svg)](https://asciinema.org/a/PF9ipTUJMJ0B86my9Hlke2Qdj)
### Comparison using Plain style

`gendiff -f plain nested_file1.yml nested_file2.yml`

[![asciicast](https://asciinema.org/a/a58YCmWsZ2hkWXoE5vJ2OADiL.svg)](https://asciinema.org/a/a58YCmWsZ2hkWXoE5vJ2OADiL)
### Comparison using Json style

`gendiff -f json filepath1.json filepath2.json`

[![asciicast](https://asciinema.org/a/thF6wmGF6TlzWD13CX2GmDE7M.svg)](https://asciinema.org/a/thF6wmGF6TlzWD13CX2GmDE7M)
