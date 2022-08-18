# CSV Utils CLI

A CSV utilities CLI for basic operations on tabular data on the terminal.

## Installation

To start using the CSV Utilities CLI, you will first have to clone this repository. Use the commond belwo to get started!

```{zsh}
$ git clone https://github.com/awakenedhaki/csv-utils.git
```

After you have clone the repository in your machine, you need to install this packages dependencies. The CSV Utilities CLI is build off of  `click`.

If you are `poetry` installed in your machine, you can run the command below...

```{zsh}
$ poetry install
```

... Otherwise, you can use good 'ol `pip` to install the entire dependency tree.

```{zsh}
$ pip install -r requirements.txt 
```

You are not set up to use the Image Tiler CLI :grinning:

## Usage

Be sure that you python version is compatible with `3.9.13`.

To run the CLI, you can call it by starting with the `python` command, followed by the path to the `cli.py` script.

CSV-utils can be used to split a tabular data file to a defined number of files or number of rows. If the former, the number of rows per file will be calculated. To specify the number of files or rows, use the `--ntables` or `--nrows` options. 

```
$ python <PATH>/cli.py split [OPTIONS] FILENAME DIRECTORY
```

For recurrent use, you can also create an alias to call on the `cli.py` script.

```{zsh}
$ aliase python <PATH>/cli.py
```

## Project Structure

```
.
├── README.md
├── poetry.lock
├── pyproject.toml
├── requirements.txt
└── src
    ├── __init__.py
    ├── cli.py
    ├── commands
    │   ├── __init__.py
    │   ├── merge.py
    │   └── split.py
    ├── objects
    │   ├── __init__.py
    │   └── options.py
    └── utils
        ├── __init__.py
        ├── load_tables.py
        ├── manipulations.py
        └── save_.py
```