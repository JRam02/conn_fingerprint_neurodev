## Optimising connectome fingerprinting for neurodevelopmental conditions

Authors: Jivesh Ramduny & Clare Kelly

### Overview

Recent advances in fMRI research have posited that the functional connectivity profile of an individual may act as a "fingerprint", i.e. the functional connectivity profile exhibits distinct characteristics at the individual level. Our aim is to leverage this knowledge to investigate whether examining the identifiability of connectivity fingerprints may serve as a better way to assess the reliability of functional connectivity measures. We investigate an array of factors that may affect that reliability in order to ultimately optimise functional connectivity measures to attain the long-term goal of discovering robust and reliable biomarkers of psychiatric disorders. We employed the functional connectome fingerprinting approach which was originally proposed by [Finn et al. (2015)](https://www.nature.com/articles/nn.4135). 

### Structural & Functional Data

Structural and functional data were obtained from the openly available [Consortium for Replicability and Reproducibility (CoRR)](http://fcon_1000.projects.nitrc.org/indi/CoRR/html/samples.html) spanning childhood to adulthood. A total of five independent datasets were used which include the New York University (NYUadu), New York University (NYUado), University of Pittsburgh School of Medicine (UPSM), Beijing Normal University (BNU) and Southwest University (SWU). For each dataset, two resting-state scans were obtained from two imaging sessions either on the same day or after several months and years. The complete information regarding the demographic details and fMRI acquisition parameters are provided below.

|  Dataset    |  NYUadu    | NYUado   | UPSM   | BNU   | SWU   |
| :---    |  :---: |  :---: | :---:|:---:|:---:|
| Sample Size | 31 | 25 | 67 | 60 | 82 |
| Age Range (years) | 18-43 | 7-13 | 14-19 | 19-23 | 18-25 |
| Gender (M: Males F: Females) | M:16 F:15 | M:15 F:10 | M:34 F:33 | M:32 F:28 | M:33 F:49 |
| Scan Duration (min) | 06:00 | 06:00 | 05:06 | 08:06 | 08:00 |
| Time Between Retest Scans | Same day | Same day | 1-4 years | 3 months | 1 year |
| Scanner Manufacturer | Siemens | Siemens | Siemens | Siemens | Siemens |
| Scanner Model | Magnetom Allegra | Magnetom Allegra | TrioTrim | TrioTrim | TrioTrim |
| Field Strength | 3.0T | 3.0T | 3.0T | 3.0T | 3.0T | 
| TR (ms) | 2000 | 2000 | 1500 | 2000 | 2000 |

### Functional Connectivity Profiles

We used a functionally defined Shen 268 parcellation to derive the FC profiles of each individual between sessions as described by [Finn et al. (2015)](https://www.nature.com/articles/nn.4135). For each individual, the mean timeseries of each ROI was extracted across the whole brain and the Pearson's correlation coefficient was calculated between all possible ROI pairs to conduct a symmetric 268 x 268 FC matrix; the correlation values represent the connecitivity strength (i.e. edges) between two ROIs (i.e. nodes). This procedure was repeated for each of the two imaging sessions such that an individual had two FC matrices which reflect his/her connectivity profiles during each session. We eliminated some edges in the FC matrices for each individual due to the lack of coverage across the whole brain. We also considered only the upper triangular part of the FC matrices to remove duplicate edges in the subsequent analyses. From 35,778 edges in the functional connectome, there were 31,878 distinct edges which remained in the NYUadu dataset, 15,051 edges in the NYUado dataset, 30,381 edges in the UPSM dataset, 27,028 edges in the BNU dataset and 28,680 edges in the SWU dataset.

### Identification Procedure

Identification was performed by creating a "database" which stored all the FC matrices of each individual from session 1. Iteratively, the FC matrix from a given individual from session 2 was then selected and this FC matrix was treated as the "target matrix". The target matrix was then compared with each of the FC matrices in the database to find the corresponding matrix which is maximally correlated with each other. An individual is correctly identified if the FC matrices in the database and target matrix share the highest Pearson's correlation coefficient. The predicted identity (ID) was compuated using two approaches:
1. binary identification (BID): ID was assigned a score of 1 if the predicted identity matched the true identity of the individual, otherwise the ID was given a score of 0.
2. relative rank (RR): RR is a continous measure ranging from 0 to 1, and quantifies the degree of "confusion" for inaccurately identified individuals such that the fewer individuals inaccurately ranked above their true ID, the lower the degree of confusion and lower the RR.

The ID accuracy for each dataset was computed as the percentage of individuals who were correctly identified out of the total number of individuals in each dataset. We then averaged the ID accuracy for each dataset by exchanging the roles of the database-target matrix. The identification procedure was repeated until the FC matrices of each subject served as target matrices across the five datasets and two database-target matrix configurations.

### Head Motion
