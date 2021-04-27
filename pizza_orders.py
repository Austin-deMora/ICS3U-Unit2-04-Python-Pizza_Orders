#!/usr/bin/env python3

# Created by: Austin de Mora
# Created on: April 2020
# This program calculates price of pizza per inch

import constants_p


def main():
    # This function calculates total cost of a pizza

    # input
    diameter = int(
        input("Enter the diameter of the pizza you would " + "like (inch): ")
    )

    # process
    sub_total = (
        constants_p.Labor + constants_p.Rent + (
            diameter * constants_p.Cost_per_inch)
    )
    total = (sub_total * constants_p.HST)

    # output
    print("")
    print("The cost for a {0} inch pizza is ${1:,.2f}".format(diameter, total))
    print("\nDone.")


if __name__ == "__main__":
    main()
