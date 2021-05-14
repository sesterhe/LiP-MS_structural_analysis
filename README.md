# LiP-data-structural-analysis

### codeauthor: <br/>
Fabian Sesterhenn, PhD <br/>
Picotti Group <br/>
Institute of Molecular Systems Biology<br/>
ETH Zurich, Switzerland <br/>
 
### contact: <br/>
<fabian.sesterhenn@gmail.com>

This repository contains code to analyze LiP-MS data in the context of protein structures. It requires that you have analyzed your MS data before, and that you have a csv file with at least UniProt IDs, peptide sequences and pvalues. 


## What you can do: 

- Match your peptides to structural descriptors: 
  - Predicted disorder 
  - Predicted secondary structure 
- Find PDB structures that contain the peptides of interest 
- Create a list of commands to be run in PyMol in order to visualize the peptides on protein structures. 
- Automatic computation of distance to annotated functional sites/binding sites 


It also provides examples for plotting the distribution of different structural descriptors so you can compare different sets of peptides/conditions. 
