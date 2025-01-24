from dataclasses import dataclass, field
from typing import List, Tuple
import numpy as np


@dataclass
class PropStf:
    bixel_width: int
    num_of_beams: int
    iso_center: Tuple[float, float, float] = field(default_factory=tuple)
    gantry_angles: List[float] = field(default_factory=list)
    couch_angles: np.ndarray = field(default_factory=lambda: np.empty(0))

@dataclass
class Resolution:
    x: int
    y: int
    z: int

@dataclass
class DoseGrid:
    resolution: Resolution

@dataclass
class PropDoseCalc:
    dose_grid: DoseGrid

@dataclass
class PropSeq:
    run_sequencing:  int

@dataclass
class PropOpt:
    run_dao: int

@dataclass
class Pln:
    radiation_mode: str
    machine: str
    num_of_fractions: int
    bio_model: str
    mult_scan: str
    prop_stf: PropStf
    prop_dose_calc: PropDoseCalc
    prop_seq: PropSeq
    prop_opt: PropOpt

@dataclass
class Pln:
    radiation_mode : str
    machine : str
    num_off_fraction : int
    bio_model : str
    mult_scan : str

