from asyncio.windows_events import INFINITE
from Data import DEFAULTS
from pathlib import Path


class MatradConfig:
    """
    Class to manage configuration settings for MatRad.
    This includes logging, machine defaults, dose calculation properties, optimization settings, etc.
    """

    # Default configuration settings
    log_level = 4
    keep_log = False
    write_log = False
    defaults = None

    # GUI and mode flags
    disable_gui = False
    sampling_scenarios = None
    dev_mode = False
    edu_mode = False

    # Internal properties for configuration
    _prop_dose_calc = None
    _prop_opt = None
    _prop_stf = None
    _message_log = []
    _evn = None
    _is_octave = None
    _is_matlab = None
    _mat_rad_version = None
    _mat_rad_src_root = None
    _primary_user_folder = None
    _example_folder = None
    _third_party_folder = None
    _mat_rad_root = None

    def __init__(self):
        """
        Initialize the MatradConfig instance and set up default configuration.
        """
        self._mat_rad_root = Path(__file__).resolve().parent.parent
        self.set_defaults()

    def set_defaults(self):
        """
        Set default properties for various configuration sections.
        These include machine settings, bio model configurations,
        dose calculation properties, and optimization parameters.
        """
        self.defaults = DEFAULTS.Defaults

        # Machine configuration defaults
        self.defaults.machine.photons = 'Generic'
        self.defaults.machine.protons = 'Generic'
        self.defaults.machine.helium = 'Generic'
        self.defaults.machine.carbon = 'Generic'
        self.defaults.machine.brachy = 'HDR'
        self.defaults.machine.fall_back = 'Generic'

        # Bio model configuration defaults
        self.defaults.bio_model.photons = 'none'
        self.defaults.bio_model.protons = 'constRBE'
        self.defaults.bio_model.helium = 'HEL'
        self.defaults.bio_model.carbon = 'LEM'
        self.defaults.bio_model.brachy = 'none'
        self.defaults.bio_model.fall_back = 'none'

        # STF (Spot-Time Factor) properties
        self.defaults.prop_stf.generator = ('PhotonIMRT', 'ParticleIMPT', 'SimpleBrachy')
        self.defaults.prop_stf.longitudinal_spot_spacing = 2
        self.defaults.prop_stf.add_margin = True
        self.defaults.prop_stf.bixel_width = 5

        # Dose calculation properties
        self.defaults.prop_dose_calc.engine = ('SVDPB', 'HongPB')
        self.defaults.prop_dose_calc.dose_grid = {'x': 3, 'y': 3, 'z': 3}
        self.defaults.prop_dose_calc.dosimetric_lateral_cutOff = 0.995
        self.defaults.prop_dose_calc.geometric_lateral_cutOff = 50
        self.defaults.prop_dose_calc.kernel_cutOff = INFINITE
        self.defaults.prop_dose_calc.ssd_density_threshold = 0.05
        self.defaults.prop_dose_calc.use_given_EqDensity_cube = False
        self.defaults.prop_dose_calc.use_custom_primary_photon_fluence = False
        self.defaults.prop_dose_calc.calc_let = False
        self.defaults.prop_dose_calc.select_voxel_is_in_scenarios = 'all'
        self.defaults.prop_dose_calc.air_off_set_correction = True
        self.defaults.prop_dose_calc.fine_sampling.sigma_sub = 1
        self.defaults.prop_dose_calc.fine_sampling.N = 2
        self.defaults.prop_dose_calc.fine_sampling.method = 'fitCircle'

        # Monte Carlo dose calculation settings
        self.defaults.prop_dose_calc.num_histories_ = 1E6
        self.defaults.prop_dose_calc.num_histories_per_beamlet = 2E4
        self.defaults.prop_dose_calc.output_MCvariance = True

        # Optimization properties
        self.defaults.prop_opt.optimizer = 'IPOPT'
        self.defaults.prop_opt.max_iter = 500
        self.defaults.prop_opt.run_dao = 0
        self.defaults.prop_opt.clear_unused_voxels = False

        # Sequencing properties
        self.defaults.prop_seq.sequencer = 'siochi'

        # Global settings for GUI, sampling, and modes
        self.disable_gui = False
        self.defaults.sampling_scenarios = 25
        self.dev_mode = False
        self.edu_mode = False

    def set_default_properties_for_testing(self):
        """
        Set default properties optimized for testing purposes.
        Adjusts properties like grid resolution, lateral cutoff, and Monte Carlo history settings.
        """
        self.set_defaults()

        # Set testing-specific values
        self.log_level = 1

        # STF settings for testing
        self.defaults.prop_stf.longitudinal_spot_spacing = 20
        self.defaults.prop_stf.bixel_width = 20

        # Dose calculation properties for testing
        self.defaults.prop_dose_calc.dose_grid.resolution = {'x': 5, 'y': 6, 'z': 7}
        self.defaults.prop_dose_calc.geometric_lateral_cutOff = 20
        self.defaults.prop_dose_calc.dosimetric_lateral_cutOff = 0.8
        self.defaults.prop_dose_calc.kernel_cutOff = 20

        # Monte Carlo settings for testing
        self.defaults.prop_dose_calc.num_histories_per_beamlet = 100
        self.defaults.prop_dose_calc.num_histories_direct = 100

        # Adjust sampling scenarios for testing
        self.defaults.sampling_scenarios = 2
        self.disable_gui = True
        self.dev_mode = True
        self.edu_mode = False
