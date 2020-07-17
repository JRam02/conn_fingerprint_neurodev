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

Failure to control for gross motion has the potential to bias the true estimates of FC-based measures as there is an inverse relationship between FC patterns and head movements, especially in developmental cohorts [(Satterthwaite et al., 2012)](https://pubmed.ncbi.nlm.nih.gov/22233733/). In order to avoid head motion in confounding the ID accuracy, we excluded high-motion individuals in the five datasets by using a root-mean-square framewise displacement (rmsFD) threshold as implemented by [Jenkinson et al. (2002)](https://pubmed.ncbi.nlm.nih.gov/12377157/). We selected an rmsFD threshold that is neither very strict (e.g. rmsFD < 0.1mm) nor very liberal (e.g. rmsFD > 0.3-0.5mm). We retained all the low-motion individuals with rmsFD <= 0.2mm in either imaging session. We then determined whether there was a relationship between head motion and ID accuracy in both imaging sessions.

### Temporal Signal-to-Noise Ratio (tSNR)

tSNR provides a measure of the noise characteristics in the fMRI timeseries over time which may stem from physiological (e.g. motion, respiration, cardiac processes) and scanner-related (e.g. scanner drifts, field inhomogeneity) artefacts [(Welvaert et al., 2013)](https://pubmed.ncbi.nlm.nih.gov/24223118/). Gains in tSNR have offered the potential to detect small fluctuations in the fMRI signal at higher spatial resolutions in addition to localising finer brain areas [(Murphy et al., 2007)](https://pubmed.ncbi.nlm.nih.gov/17126038/). We tested if there was an association between tSNR and ID accuracy to understand how the quality of the fMRI signal affects the individual functional connectome.

### Age

Recent work has shown that greater connectome distinctiveness, i.e. the degree to which an individual connectome differentiates that person from a group is associaed with increasing age during a critical period that spans puberty [(Kaufmann et al., 2017)](https://www.nature.com/articles/nn.4511). We examined age-related variability in ID accuracy that spanned across childhood to adulthood.

### Global Signal Regression (GSR)

GSR has been applied as a denoising strategy to account for physiological noise related to head motion, respiration, cardiac processes and blood vessels [(Colenbier et al., 2020](https://www.sciencedirect.com/science/article/pii/S1053811920301865?dgcid=rss_sd_all); [Power et al., 2017](https://pubmed.ncbi.nlm.nih.gov/27751941/); [Fox et al., 2009)](https://pubmed.ncbi.nlm.nih.gov/19339462/). Although GSR remains a controversial preprocessing step till date, it is highly efficient in removing the positive associations between motion parameters and FC-based measures [(Power et al., 2017](https://pubmed.ncbi.nlm.nih.gov/27751941/); [Power et al., 2014](https://www.sciencedirect.com/science/article/pii/S1053811913009117); [Yan et al., 2013)](https://pubmed.ncbi.nlm.nih.gov/23631983/), increasing the specificity of positive correlations between brain regions [(Weissenbacher et al., 2009](https://pubmed.ncbi.nlm.nih.gov/19442749/); [Fox et al., 2009)](https://pubmed.ncbi.nlm.nih.gov/19339462/), and improving the presence of neuroanatomical networks [(Fox et al., 2009)](https://pubmed.ncbi.nlm.nih.gov/19339462/). We preprocssed the functional data with and without regressing out the global signal in the fMRI timeseries to assess the effectiveness of GSR in boosting the ID accuracy.

### Parcellation Schemes

Parcellation schemes provide an understanding about the brain's anatomical, functional and cytoarchitectural organisation in a homogeneous manner, and different parcellation schemes capture coarse and fine-grained properties of brain areas [(Eickhoff et al., 2018](https://www.nature.com/articles/s41583-018-0071-7?proof=trueNov); [Eickhoff et al., 2015)](https://onlinelibrary.wiley.com/doi/full/10.1002/hbm.22933). This is because these parcellation schemes differ in terms of their coverage (e.g. cortical, whole-brain), space (e.g. volume, surface) and resolution (e.g. 10-1000). We parcellated the functional data using four publicly available parcellation schemes including [Shen 268](https://www.nature.com/articles/nn.4135), [Glasser 360](https://www.nature.com/articles/nature18933), [MIST 444](https://mniopenresearch.org/articles/1-3) and [Schaefer 1000-17Networks](https://academic.oup.com/cercor/article/28/9/3095/3978804), to determine whether there was, if any, a linear or nonlinear (e.g. exponential, polynomial) relationship between these parcellation features and ID accuracy.

### Parcel Resolution

Prior FC-based studies have indicted that higher parcel resolutions may improve the individual differences of the functional connectome (Vanderwal et al., 2019; Bellec et al., 2015). Thus, we investigated the associations between parcel resolution and ID accuracy by employing three parcellation schemes using [Schaefer 17Networks](https://github.com/ThomasYeoLab/CBIG/tree/master/stable_projects/brain_parcellation/Schaefer2018_LocalGlobal), [MIST](https://mniopenresearch.org/articles/1-3) and [DiFuMo](https://github.com/Parietal-INRIA/DiFuMo) atlases which offered 8 (i.e. 100, 200, 300, 400, 500, 600, 800, 1000), 10 (i.e. 7, 12, 20, 36, 64, 122, 197, 325, 444, 1095) and 5 (i.e. 64, 128, 256, 512, 1024) levels of parcel dimensionality, respectively.

### Parcellation Coverage

The spatial distribution of FC-based measures have shown significantly lower test-retest reliability estimates when subcortical connections are considered as opposed to cortical connections [(Shah et al., 2016)](https://onlinelibrary.wiley.com/doi/full/10.1002/brb3.456). The reliability of FC estimates may suffer from the inclusion of subcortical regions due to their small volumes, close proximity to physiological sources and low SNR due to signal dropout [(Noble et al., 2019)](https://www.sciencedirect.com/science/article/pii/S1053811919307487). We parcellated the functional data into cortical, subcortical and cerebellar regions using the Shen 268 parcellation to examine the influence of spatial brain coverage on ID accuracy. We identified the subcortical and cerebellar regions in the Shen 268 parcellation using the Harvard-Oxford atlas (https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Atlases) and Buckner atlas (http://surfer.nmr.mgh.harvard.edu/fswiki/CerebellumParcellation_Buckner2011), respectively. We then obtained the cortical regions by subtracting the subcortical and cerebellar areas from the whole-brain Shen 268 parcellation.

### Network Organisation

Several studies have demonstrated that some functional networks yield stronger predictive power in facilitating the identification of an individual [(Jalbrzikowski et al., 2019](https://onlinelibrary.wiley.com/doi/10.1002/hbm.25118); [Horien et al., 2019](https://www.sciencedirect.com/science/article/pii/S1053811919300886); [Finn et al., 2015)](https://www.nature.com/articles/nn.4135). Firstly, we delineated the functional data as previously described using the Shen 268 parcellation to assess the contributions of 8 functional networks on ID accuracy [(Finn et al., 2015)](https://www.nature.com/articles/nn.4135). These functional networks are as follows: (1) medial frontal; (2) frontoparietal; (3) default mode; (4) subcortical and cerebellum; (5) motor; (6) visual I; (7) visual II; and (8) visual association. Secondly, 
