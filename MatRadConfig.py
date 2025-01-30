from fontTools.varLib.models import nonNone
from scipy.stats import false_discovery_control


class MatradConfig:
    log_level = 4
    keep_log  = False
    write_log = False
    # defaults

    disable_gui = False

    dev_mode = False
    edu_mode = False
    # gui


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


    def __init__(self):
        pass