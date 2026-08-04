# from pathlib import Path

# class LogoAssetService:
#     def __init__(self, shield_dir: str = "app/logo/shields", mascot_dir: str = "app/logo/mascots"):
#         self.shield_dir = Path(shield_dir)
#         self.mascot_dir = Path(mascot_dir)

#     def list_shields(self) -> list[str]:
#         return [p.name for p in self.shield_dir.glob("*.svg")]

#     def list_mascots(self) -> list[str]:
#         return [p.name for p in self.mascot_dir.glob("*.svg")]