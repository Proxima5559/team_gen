from random import Random

class RandomService:
    def __init__(self, seed: int | None = None):
        if seed is None:
            seed = Random().randint(1, 2_147_483_647)
        self.seed = seed
        self.rng = Random(seed)

    def choice(self, items):
        return self.rng.choice(items)

    def weighted_choice(self, items, weights):
        return self.rng.choices(items, weights=weights, k=1)[0]

    def integer(self, a: int, b: int) -> int:
        return self.rng.randint(a, b)

    def float(self, a: float, b: float) -> float:
        return self.rng.uniform(a, b)

    def shuffle(self, items):
        self.rng.shuffle(items)
        return items