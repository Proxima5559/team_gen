from typing import Literal
FORMATIONS = {
    "4-3-3": ["GK", "LB", "CB", "CB", "RB", "CM", "CM", "CAM", "LW", "RW", "ST"],
    "4-4-2": ["GK", "LB", "CB", "CB", "RB", "LM", "CM", "CM", "RM", "ST", "ST"],
    "4-2-3-1": ["GK", "LB", "CB", "CB", "RB", "CDM", "CDM", "LAM", "CAM", "RAM", "ST"],
    "4-3-3 (Defensive)": ["GK", "LB", "CB", "CB", "RB", "CDM", "CM", "CM", "LW", "RW", "ST"],
    "4-3-2-1": ["GK", "LB", "CB", "CB", "RB", "CM", "CM", "CM", "LF", "RF", "ST"],
    "3-4-3": ["GK", "CB", "CB", "CB", "LM", "CM", "CM", "RM", "LW", "RW", "ST"],
    "3-5-2": ["GK", "CB", "CB", "CB", "LWB", "CDM", "CDM", "RWB", "CAM", "ST", "ST"],
    "5-3-2": ["GK", "LWB", "CB", "CB", "CB", "RWB", "CM", "CM", "CM", "ST", "ST"],
    "5-4-1": ["GK", "LWB", "CB", "CB", "CB", "RWB", "LM", "CM", "CM", "RM", "ST"],
}

FormationType = Literal[
    "4-3-3",
    "4-4-2",
    "4-2-3-1",
    "4-3-3 (Defensive)",
    "4-3-2-1",
    "3-4-3",
    "3-5-2",
    "5-3-2",
    "5-4-1",
]