from app.generators.manager_generator import ManagerGenerator
from app.services.random_service import RandomService
from app.services.nationality_service import NationalityService
from app.data.countries import COUNTRY_TO_NATIONALITY
from app.models.manager import Manager

def test_manager_generator_returns_manager():
    generator = ManagerGenerator(
        random_service=RandomService(seed=42),
        nationality_service=NationalityService(COUNTRY_TO_NATIONALITY),
    )

    manager = generator.generate(country="England", formation="4-3-3", style="Possession")

    assert isinstance(manager, Manager)
    assert manager.name
    assert manager.nationality == "English"
    assert manager.formation == "4-3-3"
    assert manager.style == "Possession"