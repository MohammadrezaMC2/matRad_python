import warnings
from pathlib import Path
from Data import ReadMatFiles

def load_machine(pln):
    machine = None
    file_name = ""
    if "radiation_mode" in pln:
        if "machine" in pln:
            file_name = pln.radiation_mode + "_" + pln.machine
        else:
            file_name = pln.radiation_mode + "_Generic"
            warnings.warn("No machine name given, loading generic machine", DeprecationWarning)
    else:
        AssertionError("No radiation mode given in pln")

    project_root = Path(__file__).resolve().parent.parent
    base_data_folder = project_root / "MatRad" / "BaseData"
    user_data_folder = project_root / "UserData" / "Machine"

    folders = [base_data_folder, user_data_folder]
    for folder in folders:
        if (folder / file_name).exists():
            file_path = folder / file_name
            mat_data = ReadMatFiles.read_mat_file(mat_file_name=file_path)
            machine = mat_data['machine']
    else:
        AssertionError('No machine files were found!')

    return machine