import os
from Data import PLN
from Util import FindSubclasses
from abc import ABC, abstractmethod, abstractproperty


class StfGeneratorBase(ABC):
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

        self._pln = pln
        self._cube_dim = None
        self.vox_target_world_coords = None
        self._vio_target = None
        self._ct = None
        self._cst = None

        if pln is not None:
            # assigne
            pass

    def __set_defaults(self):
        pass

    def get_generator_from_pln(self, pln):
        generator = []
        intial_default_generator = False
        self.get_available_generators()


    def get_available_generators(self, optional_paths=None):

        if optional_paths is None:
            full_path = os.path.abspath("STFGeneratorBase.py")
            optional_paths = os.path.dirname(full_path)

        else:
            if not (all(isinstance(x, str) for x in optional_paths) and
                    all(optional_paths)):
                AssertionError('Invalid path array!')

            else:
                current_script_path = os.path.abspath(__file__)
                current_script_dir = os.path.dirname(current_script_path)
                optional_paths = [current_script_dir] + optional_paths

        if self.pln is not None:
            if not (isinstance(self.pln, PLN.Pln) or self.pln is None):
                AssertionError('Invalid pln!')
        pass



