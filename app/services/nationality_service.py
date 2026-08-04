class NationalityService:
    def __init__(self, country_to_nationality: dict[str, str]):
        self.country_to_nationality = country_to_nationality

    def from_country(self, country: str) -> str:
        return self.country_to_nationality.get(country, country)