from app.services.nationality_service import NationalityService

COUNTRY_TO_NATIONALITY = {
    "England": "English",
    "Spain": "Spanish",
}

def test_england_maps_to_english():
    service = NationalityService(COUNTRY_TO_NATIONALITY)
    assert service.from_country("England") == "English"

def test_spain_maps_to_spanish():
    service = NationalityService(COUNTRY_TO_NATIONALITY)
    assert service.from_country("Spain") == "Spanish"

def test_unknown_country_returns_itself():
    service = NationalityService(COUNTRY_TO_NATIONALITY)
    assert service.from_country("Mars") == "Mars"