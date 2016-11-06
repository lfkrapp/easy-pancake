# Correlation between the fission yeast transcriptome and proteome
## Abstract
The goal of the project is to correlate mRNA levels to protein levels through the time course of meiosis in the fission yeast *S.pombe*.

## Data description
For this project, we have to compare the relative concentration of proteins and mRNA at multiple time points. The Simanis-lab (EPFL) provides a data set of relative protein concentrations and relative mRNA concentrations can be found on the website of the <a href="http://bahlerweb.cs.ucl.ac.uk/projects/sexualdifferentiation/meiosis/">bählerlab</a> (ULC). 

The data from the Simanis-lab (EPFL) is a table of measures for 2978 proteins. For each protein a relative concentration is measured for 10 time points in triplicate (2978 x 10 x 3 data points).

The data from the <a href="http://bahlerweb.cs.ucl.ac.uk/projects/sexualdifferentiation/meiosis/">bählerlab</a> (ULC) is a table of measures for 5121 mRNAs. For each mRNA an averaged relative concentration is measured for 8 time points (5121 x 8 data points).

## Feasibility and Risks
The data scraping and wrangling part of the project are not too difficult. The data provided by the bählerlab can easily be aquired. Some work needs to be done for the compatibility of the two data sets.

The challenging part of the project is the analysis of the data. We need to find the suitable correlation test and to interpret the results.

## Deliverables
The outcomes of the project are:
  1. A list of non-correlated entries
  2. Graphs and an interactive vizualisation tool showing the correlation between protein and mRNA levels for each time point
  3. A reusable Jupyter notebook which can be used with new data and outputs a CSV file with the non-correlated entries

## Timeplan
1. Data scraping and wrangling (Week 1)
  * Download and process data from <a href="http://bahlerweb.cs.ucl.ac.uk/projects/sexualdifferentiation/meiosis/">bählerlab</a>
  * Merging data from bählerlab (UCL) and the data provided by Simanis-lab (EPFL)
2. Data analysis (Week 2 to 5)
  * Correlation test
  * Extracting non-correlated entries
  * Clustering of non-correlated entries
3. Finalization (Week 6)
  * Creating graphs showing the correlation between the two data sets
4. (Optional) More data scraping (Week 7)
  * Automatic extraction of proteins sequences for non-correlated entries from <a href="https://www.pombase.org/">pombase</a> database
