from app.generators.history_generator import HistoryGenerator
from app.services.random_service import RandomService
from app.models.team import History

def test_history_generator_returns_history():
    generator = HistoryGenerator(RandomService(seed=42))
    history = generator.generate(founded=1912)

    assert isinstance(history, History)
    assert history.founded == 1912
    assert len(history.milestones) >= 1
    assert history.milestones[0] == "Club founded in 1912."

def test_history_milestones_are_not_empty():
    generator = HistoryGenerator(RandomService(seed=42))
    history = generator.generate(founded=1912)

    for milestone in history.milestones:
        assert milestone