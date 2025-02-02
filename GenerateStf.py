from Steering import STFGeneratorBase
def generate_stf(ct,cst,pln,vis_mode=False):

    stfGeneratorBase = STFGeneratorBase.StfGeneratorBase(pln=pln)
    generator = stfGeneratorBase.get_generator_from_pln(pln)
