#Date: 17/10/2019
#Authors: Jivesh Ramduny & Clare Kelly
#Location: Imaging Mind Architecture Lab, Trinity College Dublin

import os
import glob
#import pandas as pd
import numpy as np

#load the final correlation matrix derived from inter-subject correlations
shen_corr_id = np.array(np.loadtxt('/Users/user/Desktop/TCDPhD/UPSM_rest_rest_halfway_anat.txt'))

#extract the diagonal values of the final correlation matrix
diag = np.diag(shen_corr_id)

#extract the maximum value in each row of the final correlation matrix
max_corr = np.amax(shen_corr_id, axis = 1)

#ID is based on a binary system where each diagonal value is compared with the
#maximum value of that row in the final correlation matrix. We expect that the
#diagnoal value is greater than or equal to the maximum value of each row to
#allow successful identification
diag_to_array = np.array(diag)
max_corr_to_array = np.array(max_corr)
ID = np.greater_equal(diag_to_array, max_corr_to_array)
print(ID)

#success rate is defined as the total number of positive identifications divided
#by the total number of subjects
success_rate = np.sum(ID)/(ID.shape)
print(success_rate)
