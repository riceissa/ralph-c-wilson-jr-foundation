# Ralph C. Wilson, Jr. Foundation

This repo is for Vipul Naik's Donations List Website: https://github.com/vipulnaik/donations

Relevant issue: https://github.com/vipulnaik/donations/issues/98

## Instructions for running the scripts

Download the data into CSV:

```bash
./scrape.py > grants.csv
```

Use the CSV to generate SQL file:

```bash
./proc.py grants.csv > out.sql
```

## License

CC0 for scripts and readme.
