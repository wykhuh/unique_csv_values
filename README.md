# Unique values from CSV

Reads a CSV and produces another CSV with unique values.

## 1. unique_values_flourish_networks

`unique_values_flourish_networks.py` reads in a csv with two columns of taxa, and produces a csv with one column of unique taxa. Use this with Flourish network graphs which require a CSV of unique values.

### Setup

Have `Links.csv` in `input_data` directory.

### Run

```bash
unique_values_flourish_networks.py
```

## 2. append_unique_values

`append_unique_values.py` reads an one-column CSV, and creates a CSV with unique values. If the output CSV already exists, the script will check the existing CSV and add unique values to the existing file.

### Run

```bash
append_unique_values.py -i <path to input csv> -o <output csv filename>
```
