from typing import List

from .datapair import DataPair


class TideData:
    def __init__(
        self, day: str, highTide: DataPair, lowTide: DataPair, weights: DataPair
    ):

        self.day = day
        self.highTide = highTide
        self.lowTide = lowTide
        self.weights = weights

    def __repr__(self):

        return f"Day: {self.day} | High Tide: {self.highTide} | Low Tide: {self.lowTide} | Weights: {self.weights}"

    def csv(self) -> str:
        """Return self as CSV data"""

        return f"{self.day}, {self.highTide.morning}, {self.highTide.night}, {self.lowTide.morning}, {self.lowTide.night}, {self.weights.morning}, {self.weights.night}"  # noqa: E501

    @staticmethod
    def fromParsedData(data: List[str]):
        """Convert parsed data to TideData"""

        return TideData(
            data[0],
            DataPair(data[2], data[3]),
            DataPair(data[4], data[5]),
            DataPair(data[6], data[7]),
        )
