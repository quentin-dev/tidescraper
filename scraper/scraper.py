import logging
from typing import List

from bs4 import BeautifulSoup


async def getTideInfo(session, day: int, month: int) -> List[str]:
    """Get parsed data for a given day of the year"""

    url = f"https://www.ouistreham-plaisance.com/web/horaires-des-marees.php?jours={day}&mois={month}&valider=Rechercher"  # noqa: E501

    logging.debug(f"Attempting to GET {url}")

    async with session.get(url) as resp:

        soup = BeautifulSoup(await resp.text(), "html.parser")

        logging.debug("Going to extract tide data from HTML text")

        table = soup.find_all(class_="maree")[0]
        content = table.find_all("tr")[2].find_all("td")

        return [entry.text for entry in content]
