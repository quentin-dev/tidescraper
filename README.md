# tidescraper

The goal of this project is to output a CSV with all tide data from the port
of Ouistreham for the current year.

## Development

This project uses `black`, `flake8`, `isort`, and `pre-commit` in order to
provide a fully functional development environment.

## Installation

1) `python -m venv venv`
2) `. venv/bin/activate`
3) `pip install -r requirement.txt`
4) `pre-commit install`
5) `./tidescraper.py --help`

## Options

|    Name     | Short Option |         Long Option          |            Description             | Default Value |
|:-----------:|:------------:|:----------------------------:|:----------------------------------:|:-------------:|
|    Help     |     `-h`     |           `--help`           |       Shows help information       |     NONE      |
|    Mode     |     NONE     | `--mode {debug, production}` |         Sets logging level         |    `debug`    |
| Output file | `-o OUTPUT`  |      `--output OUTPUT`       | Sets the output filename to OUTPUT | `output.csv`  |

## Useful links

- [Horaires des marées Ouistreham](https://www.ouistreham-plaisance.com/web/horaires-des-marees.php)
