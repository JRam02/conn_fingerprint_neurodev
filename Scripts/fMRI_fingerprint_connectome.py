#Date: 30/10/2019
#Authors: Jivesh Ramduny & Clare Kelly
#Location: Imaging Mind Architecture Lab, Trinity College Dublin

import os
import glob
import pandas as pd
import numpy as np

#input directory for the 268 ROIs timeseries derived from Shen parcellation
rs_datapath = '/Users/immalab/Desktop/JIVPhD/timeseries_noGSR/NYUado/NYU_Schaefer_Multiresolution/NYU_Schaefer_1000/*_NYU_Schaefer_1000Parcels_noGSR_rest_session_1.txt'
mv_datapath = '/Users/immalab/Desktop/JIVPhD/timeseries_noGSR/NYUado/NYU_Schaefer_Multiresolution/NYU_Schaefer_1000/*_NYU_Schaefer_1000Parcels_noGSR_rest_session_2.txt'

rsfilename_list = glob.glob(rs_datapath)
mvfilename_list = glob.glob(mv_datapath)

#initialise an empty list to store all subjects timeseries for Sessions 1
rs_non_zero_roi = []
rsfMRI_timeseries = []
rsfMRI_timeseries_2d = []
rsfMRI_timeseries_corr = []

#initialise an empty list to store all subjects timeseries for Sessions 2
mv_non_zero_roi = []
mvfMRI_timeseries = []
mvfMRI_timeseries_2d = []
mvfMRI_timeseries_corr = []

#iterate through the ROIs timeseries of each subject for Session 1
for rsfilename in rsfilename_list:

    rs_corr_shen = np.transpose(np.loadtxt(rsfilename))

    #append the ROI timeseries for each subject to a list
    rsfMRI_timeseries.append(rs_corr_shen)

    #find the subject-wise indices whose ROI timeseries have a value of 0
    rs_non_zero = np.where(np.any(rs_corr_shen == 0, axis = 1))

    #append the subject-wise indices to a list
    rs_non_zero_roi = np.concatenate((rs_non_zero_roi, rs_non_zero), axis = None)

#convert the appended list of all the subjects' timeseries to an array
rsfMRI_timeseries_to_array = np.asarray(rsfMRI_timeseries)

#iterate through the ROIs timeseries of each subject for Session 2
for mvfilename in mvfilename_list:

    mv_corr_shen = np.transpose(np.loadtxt(mvfilename))

    #append the ROI timeseries for each subject to a list
    mvfMRI_timeseries.append(mv_corr_shen)

    #find the subject-wise indices whose ROI timeseries have a value of 0
    mv_non_zero = np.where(np.any(mv_corr_shen == 0, axis = 1))

    #append the subject-wise indices to a list
    mv_non_zero_roi = np.concatenate((mv_non_zero_roi, mv_non_zero), axis = None)

#convert the appended list of all the subjects' timeseries to an array
mvfMRI_timeseries_to_array = np.asarray(mvfMRI_timeseries)

#append all subject-wise indices whose ROI timeseries contain a value of 0 for Session 1 & 2
all_indices_s1_s2 = np.concatenate((rs_non_zero_roi, mv_non_zero_roi), axis = None)

#find all the unique indices whose ROI timeseries contain a value of 0
find_unique_indices = np.unique(all_indices_s1_s2)

#remove all the rows whose ROI timseries contain a value of 0 based on the list of unique indices for Session 1
rsfMRI_nonzero_timeseries = np.delete(rsfMRI_timeseries_to_array, find_unique_indices, axis = 1)

#sanity check to verify the content and size of the resulting nonzero ROI timeseries
print(np.array(rsfMRI_nonzero_timeseries)); print(np.array(rsfMRI_nonzero_timeseries).shape)

#remove all the rows whose ROI timseries contain a value of 0 based on the list of unique indices for Session 2
mvfMRI_nonzero_timeseries = np.delete(mvfMRI_timeseries_to_array, find_unique_indices, axis = 1)

#sanity check to verify the content and size of the resulting nonzero ROI timeseries
print(np.array(mvfMRI_nonzero_timeseries)); print(np.array(mvfMRI_nonzero_timeseries).shape)

for rs_sub in range(0, len(rsfilename_list)):

    #copy the subject-wise ROI timeseries to a temporary 2D array for Session 1
    rsfMRI_timeseries_2d = rsfMRI_nonzero_timeseries[rs_sub, :, :].copy()

    #compute Pearson’s correlation coefficient for Session 1
    rsfMRI_corr = np.corrcoef(rsfMRI_timeseries_2d)

    #truncate correlation matrix to select upper triangular matrix for Session 1
    rsfMRI_corr_shen = rsfMRI_corr.shape[0]
    arange_rsfMRI_corr, diag = np.triu_indices(rsfMRI_corr_shen, 1)
    trunc_rsfMRI_corr_shen = rsfMRI_corr[arange_rsfMRI_corr, diag]

    #append the truncated correlation matrix of all subjects to the list
    rsfMRI_timeseries_corr.append(trunc_rsfMRI_corr_shen)

#sanity check to verify the length and content of the list for Session 1
print(len(rsfMRI_timeseries_corr)); print(rsfMRI_timeseries_corr)

#convert the list to an array for Session 1
trunc_rsfMRI_corr_to_array = np.asarray(rsfMRI_timeseries_corr)

#sanity check to verify the size of the array for Session 1
print(trunc_rsfMRI_corr_to_array.shape)

#transpose the array to ease further computation for Session 1
trans_rsfMRI_corr = np.transpose(trunc_rsfMRI_corr_to_array)

for mv_sub in range(0, len(mvfilename_list)):

    #copy the subject-wise ROI timeseries to a temporary 2D array for Session 2
    mvfMRI_timeseries_2d = mvfMRI_nonzero_timeseries[mv_sub, :, :].copy()

    #compute Pearson’s correlation coefficient for Session 2
    mvfMRI_corr = np.corrcoef(mvfMRI_timeseries_2d)

    #truncate correlation matrix to select upper triangular matrix for Session 2
    mvfMRI_corr_shen = mvfMRI_corr.shape[0]
    arange_mvfMRI_corr, diag = np.triu_indices(mvfMRI_corr_shen, 1)
    trunc_mvfMRI_corr_shen = mvfMRI_corr[arange_mvfMRI_corr, diag]

    #append the truncated correlation matrix of all subjects to the list
    mvfMRI_timeseries_corr.append(trunc_mvfMRI_corr_shen)

#sanity check to verify the length and content of the list for Session 2
print(len(mvfMRI_timeseries_corr)); print(mvfMRI_timeseries_corr)

#convert the list to an array for Session 2
trunc_mvfMRI_corr_to_array = np.asarray(mvfMRI_timeseries_corr)

#sanity check to verify the size of the array for Session 2
print(trunc_mvfMRI_corr_to_array.shape)

#transpose the array to ease further computation for Session 2
trans_mvfMRI_corr = np.transpose(trunc_mvfMRI_corr_to_array)

#compute columnwise pearson's correlation matrix between Session 1 and Session 2
trans_rsfMRI_corr = (trans_rsfMRI_corr - trans_rsfMRI_corr.mean(axis = 0)) / trans_rsfMRI_corr.std(axis = 0)
trans_mvfMRI_corr = (trans_mvfMRI_corr - trans_mvfMRI_corr.mean(axis = 0)) / trans_mvfMRI_corr.std(axis = 0)
rs_mv_corr = np.dot(trans_rsfMRI_corr.T, trans_mvfMRI_corr) / trans_rsfMRI_corr.shape[0]

#sanity check to verify the size and content of the correlation matrix
print(rs_mv_corr.shape); print(rs_mv_corr)
np.savetxt('/Users/immalab/Desktop/JIVPhD/timeseries_noGSR/NYUado/NYU_Schaefer_Multiresolution/NYUado_Schaefer_1000Parcels_noGSR_rest_rest_halfway_anat.txt', rs_mv_corr)
