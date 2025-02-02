from asyncio.windows_events import INFINITE
from Data import DEFAULTS
from pathlib import Path



class MatradConfig:
    """
    Class to manage configuration settings for MatRad.
    This includes logging, machine defaults, dose calculation properties, optimization settings, etc.
    """

    # Default configuration settings
    log_level = 4  # Logging level (higher values indicate more detailed logs)
    keep_log = False  # Flag to keep log files
    write_log = False  # Flag to enable writing logs
    defaults = None  # Placeholder for default configurations

    # GUI and mode flags
    disable_gui = False  # Determines whether GUI is disabled
    sampling_scenarios = None  # Number of scenarios for sampling
    dev_mode = False  # Development mode flag
    edu_mode = False  # Educational mode flag

    # Internal properties for configuration
    _prop_dose_calc = None  # Dose calculation properties
    _prop_opt = None  # Optimization properties
    _prop_stf = None  # Spot-Time Factor (STF) properties
    _message_log = []  # Message log storage
    _evn = None  # Environment settings
    _is_octave = None  # Flag for Octave compatibility
    _is_matlab = None  # Flag for MATLAB compatibility
    _mat_rad_version = None  # Version of MatRad
    _mat_rad_src_root = None  # Source root directory for MatRad
    _primary_user_folder = None  # Primary user folder
    _example_folder = None  # Example folder path
    _third_party_folder = None  # Third-party folder path
    _mat_rad_root = None  # Root directory for MatRad

    def __init__(self):
        """
        Initialize the MatradConfig instance and set up default configuration.
        """
        self._mat_rad_root = Path(__file__).resolve().parent.parent  # Set MatRad root directory
        self.set_defaults()  # Apply default settings

    def set_defaults(self):
        """
        Set default properties for various configuration sections.
        These include machine settings, bio model configurations,
        dose calculation properties, and optimization parameters.
        """

        # Machine configuration defaults
        machine = DEFAULTS.Machine(
            photons='Generic',
            protons='Generic',
            helium='Generic',
            carbon='Generic',
            brachy='HDR',
            fall_back='Generic'
        )

        # Bio model configuration defaults
        bio_model = DEFAULTS.BioModel(
            photons='none',
            protons='constRBE',
            helium='HEL',
            carbon='LEM',
            brachy='none',
            fall_back='none'
        )

        # STF (Spot-Time Factor) properties
        prop_stf = DEFAULTS.PropStf(
            generator=('PhotonIMRT', 'ParticleIMPT', 'SimpleBrachy'),
            longitudinal_spot_spacing=2,
            add_margin=True,
            bixel_width=5
        )

        # Dose calculation properties
        fine_sampling = DEFAULTS.FineSampling(
            sigma_sub=1,
            N=2,
            method='fitCircle'
        )
        dose_grid = DEFAULTS.DoseGrid(
            resolution={'x': 3, 'y': 3, 'z': 3}
        )
        prop_dose_calc = DEFAULTS.PropDoseCalc(
            engine=('SVDPB', 'HongPB'),
            dose_grid=dose_grid,
            dosimetric_lateral_cutOff=0.995,
            geometric_lateral_cutOff=50,
            kernel_cutOff=INFINITE,
            ssd_density_threshold=0.05,
            use_given_eq_densities=False,
            use_custom_primary_photon_fluence=False,
            calc_let=False,
            select_voxel_is_in_scenarios='all',
            air_off_set_correction=True,
            fine_sampling=fine_sampling,
            num_histories_direct=1E6,
            num_histories_per_beamlet=2E4,
            output_MCvariance=True
        )

        # Optimization properties
        prop_opt = DEFAULTS.PropOpt(
            optimizer='IPOPT',
            max_iter=500,
            run_dao=0,
            clear_unused_voxels=False
        )

        # Sequencing properties
        prop_seq = DEFAULTS.PropSeq(
            sequencer='siochi'
        )

        # Global settings for GUI, sampling, and modes
        self.defaults = DEFAULTS.Defaults(
            machine=machine,
            bio_model=bio_model,
            prop_stf=prop_stf,
            prop_dose_calc=prop_dose_calc,
            prop_opt=prop_opt,
            prop_seq=prop_seq,
            sampling_scenarios=25
        )
        self.disable_gui = False  # Enable GUI
        self.dev_mode = False  # Disable development mode
        self.edu_mode = False  # Disable educational mode

    def set_default_properties_for_testing(self):
        """
        Set default properties optimized for testing purposes.
        Adjusts properties like grid resolution, lateral cutoff, and Monte Carlo history settings.
        """
        self.set_defaults()

        # Set testing-specific values
        self.log_level = 1  # Reduced log level for testing

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
        self.disable_gui = True  # Disable GUI for testing
        self.dev_mode = True  # Enable development mode
        self.edu_mode = False  # Keep educational mode disabled
