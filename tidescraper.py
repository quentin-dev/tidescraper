#!/usr/bin/env python3

import argparse
import asyncio
import datetime
import logging
from calendar import monthrange
from typing import Dict

import aiohttp

import constants
import models
import scraper


async def getYearTideInfo() -> Dict[str, models.TideData]:
    """Get all tide data for a given year"""
    yearlyValues = {}

    currentYear = datetime.datetime.now().year

    conn = aiohttp.TCPConnector(limit=constants.MAX_CONNECTIONS_DEFAULT)

    async with aiohttp.ClientSession(connector=conn) as session:

        values = {}

        logging.info("Going to loop over every day of the year")

        for month in range(1, 13):

            days = monthrange(currentYear, month)[1]

            for day in range(1, days + 1):

                values[f"{currentYear}-{month}-{day}"] = scraper.getTideInfo(
                    session, day, month
                )

        logging.info("Going to create TideData for every day of the year")

        for key, value in zip(values.keys(), await asyncio.gather(*values.values())):

            yearlyValues[key] = models.TideData.fromParsedData(value)

    return yearlyValues


def saveValues(values: Dict[str, models.TideData], filename: str):
    """Save given dictionary to the given filename"""

    logging.info(f"Going to save data to file: {filename}")

    with open(filename, "w") as file:

        file.write("date, day, htm, htn, ltm, ltn, wm, wn\n")

        for key in values.keys():

            entry = values[key]

            file.write(f"{key}, {entry.csv()}\n")

    logging.info(f"Finished saving data to {filename}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="tidescraper",
        description="Get tide data in Ouistreham for every day of the current year",
    )

    parser.add_argument(
        "--mode",
        type=str,
        choices=["debug", "production"],
        default="debug",
        help="Set logging level",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=constants.OUTPUT_FILE_DEFAULT,
        help="Set output filename",
    )

    args = parser.parse_args()

    loglevel = logging.INFO if args.mode == "production" else logging.DEBUG

    logging.basicConfig(level=loglevel)

    logging.info(f"Logging level set to {logging.getLevelName(loglevel)}")
    logging.info("Starting tidescraper")

    yearlyValues = asyncio.run(getYearTideInfo())

    saveValues(yearlyValues, args.output)
