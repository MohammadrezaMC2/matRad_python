import os
from Data import PLN
from MatRadConfig import MatradConfig
from abc import ABC, abstractmethod, abstractproperty
from Util import FindSubclasses
from MatRad.BaseData import LoadMachine

# region AbstractClass
class StfGeneratorBaseAbstract(ABC):
    @property
    @abstractproperty
    def name(self):
        pass

    @property
    @abstractproperty
    def short_name(self):
        pass

    @property
    @abstractproperty
    def possible_radiation_modes(self):
        pass

    def __init__(self, pln):
        self.vis_mode = False
        self.add_margin = True
        self.mult_scan = None
        self.bio_model = None
        self.radiation_mode =  None
        self.machine = None

        self._is_stf_generator = True
        self._pln = pln
        self._cube_dim = None
        self._vox_target_world_coords = None
        self._vio_target = None
        self._ct = None
        self._cst = None


        if pln is not None:
            # assigne
            pass

    def __set_defaults(self):
        Mat_rad_cfg = MatradConfig()
        default_prop_stf = Mat_rad_cfg.defaults.prop_stf
        pass

    def get_generator_from_pln(self, pln):
        generator = []
        intial_default_generator = False
        self.get_available_generators()


    def get_available_generators(self, optional_paths=None):
        machine = None
        machine_mode = None

        if optional_paths is None:
            optional_paths = []
            full_path = os.path.abspath(__file__)
            optional_paths.append(os.path.dirname(full_path))

        else:
            if not (all(isinstance(x, str) for x in optional_paths) and
                    all(optional_paths)):
                AssertionError('Invalid path array!')

            else:
                current_script_path = os.path.abspath(__file__)
                current_script_dir = os.path.dirname(current_script_path)
                optional_paths = [current_script_dir] + optional_paths

        if self._pln is not None:
            if not (isinstance(self._pln, PLN.Pln) or self._pln is None):
                AssertionError('Invalid pln!')
        pass
        available_stf_generator = FindSubclasses.find_sub_classes(os.path.basename(__file__),
                                                                  folder=optional_paths,
                                                                  include_abstract=False)


        if optional_paths is not None and self._pln is not None:
            machine = LoadMachine.load_machine(self._pln)
            machine_mode = machine['meta']['radiation_mode']

        """
            I was here last time!
        """

#endregion


class StfGeneratorBase(StfGeneratorBaseAbstract):
    name = "Custom STF Generator"
    possible_radiation_modes = ["mode1", "mode2"]
    short_name = "CSTF"
