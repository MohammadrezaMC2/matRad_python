from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass
class Machine:
    photons: str
    protons: str
    helium: str
    carbon: str
    brachy: str
    fall_back: str

@dataclass
class BioModel:
    photons: str
    protons: str
    helium: str
    carbon: str
    brachy: str
    fall_back: str

@dataclass
class PropStf:
    longitudinal_spot_spacing: int
    add_margin: bool
    bixel_width: int
    generator: Tuple[str, str, str] = field(default_factory=tuple)

@dataclass
class DoseGrid:
    resolution: {}
@dataclass
class FineSampling:
    sigma_sub: int
    N: int
    method: str

@dataclass
class PropDoseCalc:
    geometric_lateral_cutOff: int
    dosimetric_lateral_cutOff: float
    kernel_cutOff: int
    ssd_density_threshold: float
    use_given_eq_densities: bool
    use_custom_primary_photon_fluence: bool
    calc_let: bool
    select_voxel_is_in_scenarios: str
    air_off_set_correction: bool
    fine_sampling: FineSampling
    num_histories_direct: float
    output_MCvariance: bool
    dose_grid: DoseGrid
    use_given_eq_densities: bool
    num_histories_per_beamlet: float
    engine: Tuple[str, str] = field(default_factory=tuple)

@dataclass
class PropOpt:
    optimizer: str
    max_iter: int
    run_dao: int
    clear_unused_voxels: bool


@dataclass
class PropSeq:
    sequencer: str

@dataclass
class Defaults:
    sampling_scenarios: int
    machine: Machine
    bio_model: BioModel
    prop_stf: PropStf
    prop_dose_calc: PropDoseCalc
    prop_opt: PropOpt
    prop_seq: PropSeq

























