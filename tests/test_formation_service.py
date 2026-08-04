import pytest
from app.services.formation_service import FormationService

def test_returns_positions_for_433():
    service = FormationService()
    positions = service.get_positions("4-3-3")
    assert positions == ["GK", "LB", "CB", "CB", "RB", "CM", "CM", "CAM", "LW", "RW", "ST"]

def test_returns_exactly_11_positions():
    service = FormationService()
    positions = service.get_positions("4-3-3")
    assert len(positions) == 11

def test_invalid_formation_raises_value_error():
    service = FormationService()
    with pytest.raises(ValueError):
        service.get_positions("9-9-9")