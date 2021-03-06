#!/usr/bin/env python3

import csv
import sys

def main():
    with open(sys.argv[1], newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        print("""insert into donations (donor, donee, amount, donation_date, donation_date_precision, donation_date_basis, cause_area, url, affected_regions, notes) values""")
        first = True

        for row in reader:
            assert row["amount"].startswith("$")
            if row["amount"].endswith(" million") or row["amount"].endswith(" Million"):
                amount = float(row["amount"].split()[0].replace("$", "")) * 1e6
            else:
                amount = float(row["amount"].replace("$", "").replace(",", ""))

            notes = ("Program: " + row["program"] + ". " if row["program"] else "") + row["purpose"]

            print(("    " if first else "    ,") + "(" + ",".join([
                mysql_quote("Ralph C. Wilson, Jr. Foundation"),  # donor
                mysql_quote(row["donee"]),  # donee
                str(amount),  # amount
                mysql_quote(""),  # donation_date
                mysql_quote(""),  # donation_date_precision
                mysql_quote("donation log"),  # donation_date_basis
                mysql_quote(row["program_area"]),  # cause_area
                mysql_quote("http://www.ralphcwilsonjrfoundation.org/our-grantees/"),  # url
                mysql_quote(row["region"]),  # affected_regions
                mysql_quote(notes),  # notes
            ]) + ")")
            first = False
        print(";")


def mysql_quote(x):
    """Quote the string x using MySQL quoting rules. If x is the empty string,
    return "NULL". Probably not safe against maliciously formed strings, but
    our input is fixed and from a basically trustable source."""
    if not x:
        return "NULL"
    x = x.replace("\\", "\\\\")
    x = x.replace("'", "''")
    x = x.replace("\n", "\\n")
    return "'{}'".format(x)


if __name__ == "__main__":
    main()
