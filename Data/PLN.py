from dataclasses import dataclass, field
from typing import List, Tuple
import numpy as np


@dataclass
class TreatmentParameters:
    """
    Class to store the treatment parameters for radiation therapy.
    """
    bixel_width: int
    num_of_beams: int
    iso_center: Tuple[float, float, float] = field(default_factory=tuple)
    gantry_angles: List[float] = field(default_factory=list)
    couch_angles: np.ndarray = field(default_factory=lambda: np.empty(0))


@dataclass
class Resolution:
    """
    Class to define the resolution of the dose grid in the x, y, and z axes.
    """
    x: int
    y: int
    z: int


@dataclass
class DoseGrid:
    """
    Class representing the dose grid, including its resolution.
    """
    resolution: Resolution


@dataclass
class DoseCalculation:
    """
    Class for handling dose calculation based on the dose grid.
    """
    dose_grid: DoseGrid


@dataclass
class Sequencing:
    """
    Class representing the sequencing information for the treatment.
    """
    run_sequencing: int


@dataclass
class Optimization:
    """
    Class to control the optimization process in treatment planning.
    """
    run_dao: int


@dataclass
class TreatmentPlan:
    """
    Class representing a treatment plan, combining radiation mode, machine,
    and additional parameters for the treatment process.
    """
    radiation_mode: str
    machine: str
    num_of_fractions: int
    bio_model: str
    mult_scan: str
    treatment_parameters: TreatmentParameters
    dose_calculation: DoseCalculation
    sequencing: Sequencing
    optimization: Optimization
