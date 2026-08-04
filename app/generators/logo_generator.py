# from app.models.logo import LogoConfig
# from app.data.colors import COLORS
# from app.services.logo_asset_service import LogoAssetService
# from app.services.random_service import RandomService

# class LogoGenerator:
#     def __init__(self, random_service: RandomService, asset_service: LogoAssetService):
#         self.random = random_service
#         self.asset_service = asset_service

#     def _make_initials(self, club_name: str) -> str:
#         parts = [part for part in club_name.split() if part and part[0].isalpha()]
#         return "".join(part[0] for part in parts)[:3].upper()

#     def generate(self, club_name: str, founded_year: int) -> LogoConfig:
#         shields = self.asset_service.list_shields()
#         mascots = self.asset_service.list_mascots()

#         if not shields:
#             raise ValueError("No shield SVG files found")

#         primary_color = self.random.choice(COLORS)
#         secondary_color = self.random.choice([c for c in COLORS if c != primary_color])
#         accent_color = self.random.choice([c for c in COLORS if c not in (primary_color, secondary_color)])

#         patterns = ["stripes", "diagonal", "split", "solid", "chevrons"]
#         borders = ["thin", "bold", "double", "gold"]

#         return LogoConfig(
#             shield_file=self.random.choice(shields),
#             mascot_file=self.random.choice(mascots) if mascots else None,
#             pattern=self.random.choice(patterns),
#             border_style=self.random.choice(borders),
#             primary_color=primary_color,
#             secondary_color=secondary_color,
#             accent_color=accent_color,
#             initials=self._make_initials(club_name),
#             stars=max(0, (2026 - founded_year) // 25),
#             founded_year=founded_year,
#         )