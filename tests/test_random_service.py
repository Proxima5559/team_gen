from app.services.random_service import RandomService

def test_choice_returns_item_from_list():
    service = RandomService(seed=42)
    items = ["a", "b", "c"]
    result = service.choice(items)
    assert result in items

def test_weighted_choice_returns_item_from_list():
    service = RandomService(seed=42)
    items = ["a", "b", "c"]
    result = service.weighted_choice(items, [1, 2, 3])
    assert result in items

def test_integer_returns_value_within_range():
    service = RandomService(seed=42)
    value = service.integer(10, 20)
    assert 10 <= value <= 20

def test_float_returns_value_within_range():
    service = RandomService(seed=42)
    value = service.float(1.5, 2.5)
    assert 1.5 <= value <= 2.5

def test_same_seed_produces_same_sequence():
    s1 = RandomService(seed=42)
    s2 = RandomService(seed=42)

    seq1 = [s1.integer(1, 100) for _ in range(5)]
    seq2 = [s2.integer(1, 100) for _ in range(5)]

    assert seq1 == seq2