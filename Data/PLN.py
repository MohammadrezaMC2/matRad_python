from dataclasses import dataclass, field
from typing import List, Tuple
import numpy as np

@dataclass
class PropStf:
    """
    Represents spot-time factor (STF) properties for radiation treatment planning.
    """
    bixel_width: int  # Width of the bixel (beamlet)
    num_of_beams: int  # Number of beams in the treatment plan
    iso_center: Tuple[float, float, float] = field(default_factory=tuple)  # Isocenter coordinates
    gantry_angles: List[float] = field(default_factory=list)  # List of gantry angles for beam delivery
    couch_angles: np.ndarray = field(default_factory=lambda: np.empty(0))  # Array of couch angles

@dataclass
class Resolution:
    """
    Represents the resolution of the dose grid in three dimensions.
    """
    x: int  # Resolution in the x-direction
    y: int  # Resolution in the y-direction
    z: int  # Resolution in the z-direction

@dataclass
class DoseGrid:
    """
    Defines the dose grid resolution for dose calculation.
    """
    resolution: Resolution  # Dose grid resolution settings

@dataclass
class PropDoseCalc:
    """
    Stores properties related to dose calculation.
    """
    dose_grid: DoseGrid  # Dose grid settings for calculations

@dataclass
class PropSeq:
    """
    Contains properties related to sequencing in treatment planning.
    """
    run_sequencing: int  # Flag to indicate if sequencing should be executed

@dataclass
class PropOpt:
    """
    Stores properties related to optimization in treatment planning.
    """
    run_dao: int  # Flag to indicate if DAO (Dose Algorithm Optimization) should be run

@dataclass
class Pln:
    """
    Represents the overall treatment plan configuration, including machine settings, biological model, and optimization properties.
    """
    radiation_mode: str  # Type of radiation mode used in the treatment
    machine: str  # Machine used for the treatment plan
    num_of_fractions: int  # Number of fractions in the treatment plan
    bio_model: str  # Biological model used in calculations
    mult_scan: str  # Multi-scan setting
    prop_stf: PropStf  # Spot-time factor settings
    prop_dose_calc: PropDoseCalc  # Dose calculation settings
    prop_seq: PropSeq  # Sequencing settings
    prop_opt: PropOpt  # Optimization settings