from app.data.formation import FORMATIONS, FormationType

class FormationService:
    def get_positions(self, formation: FormationType) -> list[str]:
        if formation not in FORMATIONS:
            raise ValueError(f"Unknown formation: {formation}")
        return FORMATIONS[formation]