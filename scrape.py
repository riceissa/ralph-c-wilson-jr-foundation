#!/usr/bin/env python3

import sys
import requests
import csv
from bs4 import BeautifulSoup


def main():
    fieldnames = ["donee", "program", "amount", "program_area", "amount",
                  "region", "purpose", "donee_url"]
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    writer.writeheader()

    url = "http://www.ralphcwilsonjrfoundation.org/our-grantees/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    for div in soup.find_all("div", {"class": "grantee"}):
        paras = div.find_all("p")
        assert len(paras) == 6

        if paras[0].em:
            program = paras[0].em.text.strip()
            donee = paras[0].span.text.strip()
        else:
            program = ""
            donee = paras[0].text.strip()

        program_area = paras[1].text.strip()
        assert program_area.startswith("Program Area: ")
        program_area = program_area[len("Program Area: "):]

        amount = paras[2].text.strip()
        assert amount.startswith("Amount: ")
        amount = amount[len("Amount: "):]

        region = paras[3].text.strip()
        assert region.startswith("Region: ")
        region = region[len("Region: "):]

        purpose = paras[5].text.strip()
        donee_url = div.find("a", {"class": "grantee-cta"}).get("href")

        writer.writerow({
            "donee": donee,
            "program": program,
            "amount": amount,
            "program_area": program_area,
            "amount": amount,
            "region": region,
            "purpose": purpose,
            "donee_url": donee_url,
        })


if __name__ == "__main__":
    main()
