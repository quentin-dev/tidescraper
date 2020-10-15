class DataPair:
    def __init__(self, morning: str, night: str):

        self.morning = morning
        self.night = night

    def __repr__(self):

        return f"Morning: {self.morning} & Night: {self.night}"
