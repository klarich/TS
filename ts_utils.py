from typing import List, Optional

from reagent import Reagent


def create_reagents(filename: str, minimum_uncertainty: float, prior_std: float, num_to_select: Optional[int] = None) -> List[Reagent]:
    """
    Creates a list of Reagents from a file
    :param filename: a smiles file containing the reagents
    :param minimum_uncertainty: Minimum uncertainty about the mean for the prior. We don't want to start with too little
    uncertainty about the mean if we (randomly) get initial samples which are very close together. Can set this
    higher for more exploration / diversity, lower for more exploitation.
    :param prior_std: This is the "known" standard deviation for the distribution of which we are trying to estimate the
    mean. Should be proportional to the range of possible values the scoring function can produce.
    :param num_to_select: For dev purposes; the number of molecules to return
    :return: List of Reagents
    """
    reagent_list = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            smiles, reagent_name = line.split()
            reagent = Reagent(reagent_name=reagent_name, smiles=smiles, minimum_uncertainty=minimum_uncertainty, known_std=prior_std)
            reagent_list.append(reagent)
    if num_to_select is not None and len(reagent_list) > num_to_select:
        reagent_list = reagent_list[:num_to_select]
    return reagent_list


def read_reagents(reagent_file_list, num_to_select: Optional[int], minimum_uncertainty: float, prior_std: float):
    """
    Read the reagents SMILES files
    :param reagent_file_list: a list of filenames containing reagents for the reaction. Each file list contains smiles
    strings for a single component of the reaction.
    :param num_to_select: select how many reagents to read, mostly a development function
    :param minimum_uncertainty: Minimum uncertainty about the mean for the prior. We don't want to start with too little
    uncertainty about the mean if we (randomly) get initial samples which are very close together. Can set this
    higher for more exploration / diversity, lower for more exploitation.
    :param prior_std: This is the "known" standard deviation for the distribution of which we are trying to estimate the
    mean. Should be proportional to the range of possible values the scoring function can produce.
    """
    reagents = []
    for reagent_filename in reagent_file_list:
        reagent_list = create_reagents(filename=reagent_filename, num_to_select=num_to_select,
                                       minimum_uncertainty=minimum_uncertainty, prior_std=prior_std)
        reagents.append(reagent_list)
    return reagents
