import numpy as np
from Data import PLN
from Data import ReadMatFiles
from Geometry import GetIsoCenter
import GenerateStf

mat_file_name = "Data/TG119.mat"
mat_data = ReadMatFiles.read_mat_file(mat_file_name=mat_file_name)
ct = mat_data['ct']
cst = mat_data['cst']

gantry_angles=[0, 90]
iso_center = (0,0,0)
prop_stf = PLN.PropStf(
    bixel_width=5,
    gantry_angles=gantry_angles,
    couch_angles=np.zeros(len(gantry_angles), dtype=float),
    num_of_beams=len(gantry_angles),
    iso_center=iso_center,
)

resolution = PLN.Resolution(
    x=50, # mm
    y=50, # mm
    z=50  # mm
)

dose_grid = PLN.DoseGrid(
    resolution=resolution
)
prop_dose_calc = PLN.PropDoseCalc(
    dose_grid=dose_grid
)

prop_seq = PLN.PropSeq(
    run_sequencing=1
)

prop_opt = PLN.PropOpt(
    run_dao=0
)


pln = PLN.Pln(
    radiation_mode='photons',
    machine='Generic',
    num_of_fractions=30,
    bio_model='none',
    mult_scan='nomScan',
    prop_stf=prop_stf,
    prop_dose_calc=prop_dose_calc,
    prop_seq=prop_seq,
    prop_opt=prop_opt
)

pln.prop_stf.num_of_beams = len(pln.prop_stf.gantry_angles)

pln.prop_stf.iso_center = GetIsoCenter.get_iso_center(cst, ct, visBool=False)

stf = GenerateStf.generate_stf(ct,cst,pln)















