#Date: 18/10/2019
#Authors: Jivesh Ramduny & Clare Kelly
#Location: Imaging Mind Architecture Lab, Trinity College Dublin

import os
import glob
import pandas as pd
import numpy as np

#load the final correlation matrix derived from inter-subject correlations
shen_corr_id = np.array(np.loadtxt('/Users/immalab/Desktop/JIVPhD/timeseries_noGSR/NYUado/NYU_Schaefer_Multiresolution/NYUado_Schaefer_1000Parcels_noGSR_rest_rest_halfway_anat.txt'))

#extract the diagonal values of the final correlation matrix
diag = np.diag(shen_corr_id)
diag_to_array = np.array(diag)
diag_dim = diag_to_array[:, None]

#sort the final correlation matrix in a row-wise fashion in descending order
desc_sort_shen_corr_id = np.sort(-shen_corr_id, axis = 1)
order_shen_corr_id = (-desc_sort_shen_corr_id)
order_shen_corr_id_to_array = np.array(order_shen_corr_id)

#find the index (rank) of the diagonal (identity) in the ordered matrix
#retrieve the rank of the identity for each subject based on the column index
ID = np.equal(order_shen_corr_id_to_array, diag_dim)
ID_index = np.argwhere(ID)
ID_index_col = ID_index[:, 1]

#add a constant of 1 to the indices as the default index starts at 0
add_index = ID_index_col + 1

#compute the relative rank of each ID by dividing the rank of digonals by the
#total number of subjects
relative_rank = add_index / (diag_to_array.shape)
print(relative_rank)
np.savetxt('/Users/immalab/Desktop/JIVPhD/timeseries_noGSR/NYUado/NYU_Schaefer_Multiresolution/relative_rank_NYUado_Schaefer_1000Parcels.txt', relative_rank)

#success rate is defined as the mean of the relative rank of all the IDs
sucess_rate = np.mean(relative_rank)
print(sucess_rate)
