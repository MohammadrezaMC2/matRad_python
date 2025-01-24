from Data import PLN
from Data import ReadMatFiles
from Geometry import GetIsoCenter
import Data


mat_file_name = "Data/TG119.mat"
mat_data = ReadMatFiles.read_mat_file(mat_file_name=mat_file_name)
ct = mat_data['ct']
cst = mat_data['cst']
print(cst.shape)
ixTarget = 2
print(cst[ixTarget, 4])

pln = PLN.Pln
# pln.prop_stf.iso_center = GetIsoCenter.get_iso_center(cst, ct, visBool=False)

