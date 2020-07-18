#!/bin/bash
#Date: 26/09/2019
#Authors: Jivesh Ramduny & Clare Kelly
#Location: Imaging Mind Archiecture Lab, Trinity College Dublin

datadir=/Volumes/active_projects/CORR/subs
outdir=/Volumes/active_projects/Jiv/adult_func_conn/shen_2mm_268ROI
subdir=/Volumes/active_projects/Jiv/adult_func_conn/sublist.txt

for sub in `cat ${subdir}`; do

  echo ${sub}
  
  if [ -f ${datadir}/${sub}/session_1/rest_1/rest_res_36param2standard.nii.gz ]; then
     
    3dROIstats -quiet -mask_f2short -nzmean -nomeanout -numROI 268 \
    -mask /Volumes/active_projects/Jiv/adult_func_conn/shen_2mm_268_parcellation.nii \
    ${datadir}/${sub}/session_1/rest_1/rest_res_36param2standard.nii.gz \
    > ${outdir}/${sub}_shen_2mm_268ROI_rest_session_1.txt
      
  fi
  
done
  
for sub in `cat ${subdir}`; do
  
  echo ${sub}
  
  if [ -f ${datadir}/${sub}/session_2/rest_1/rest_res_36param2standard.nii.gz ]; then
  
    3dROIstats -quiet -mask_f2short -nzmean -nomeanout -numROI 268 \
    -mask /Volumes/active_projects/Jiv/adult_func_conn/shen_2mm_268_parcellation.nii \
    ${datadir}/${sub}/session_2/rest_1/rest_res_36param2standard.nii.gz \
    > ${outdir}/${sub}_shen_2mm_268ROI_rest_session2.txt
      
  fi
    
done
