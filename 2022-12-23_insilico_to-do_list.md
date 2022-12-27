# 2022-12-23_insilico_to-do_list
> update from 12-15
> re-update on 12-23
> last update on 12-27

> This document is not written in stone and is for record purposes. *R&R and specifics can always change.* 

## 1. CAI and TAI tool (command line, linux) - **Yoon pro**

> Priority level HIGH

1. https://github.com/elisadonnard/CodonOPT

2. stAIcalc: tRNA adaptation index calculator based on species-specific weights (https://academic.oup.com/bioinformatics/article/33/4/589/2593585?login=false)

    - **Download** -> tAI calc (tau-tai.azurewebsites.net)

3. GitHub - mariodosreis/tai: The tRNA adaptation index

## 2. Structure dot bracket으로 보기로 한 이유 

> Priority level MID

https://www.pnas.org/doi/10.1073/pnas.2112677119#sec-5

### dot-bracket structure comparison - **split to find one that works well**

http://beagle.bio.uniroma2.it/documentation.php

https://academic.oup.com/nar/article/42/10/6146/2436561

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5860439/pdf/btx704.pdf

## 3. 권오성 프로님 요청 [Figure 4] - **Kim pro**

> Priority level MID

https://www.pnas.org/doi/10.1073/pnas.1908052116

## 4. UTR selection 알고리즘 

> Priority level HIGH

### regression analysis - **Eum pro**

- Regression using R - statistical approach

- Regression but slope 찾을때 tensorflow - ML approach

- Things to consider:

    - covariates

        - categorical? continous?

    - independent variable (Translation efficiency, gene expression, Half life, etc.)

        - categorical? continous?

### AI approach - **Moon pro**

- bidirectional LSTM-CRF sequence tagging 

## 5. Module Combining Strategy - **Everyone**

> Priority level HIGH/MID

- CDS optimization first? and then UTR fitting + structural insight

## 6. Ribosome Loading - **Yoon pro (slowly)**

> Priority level MID/LOW

- Nascent Ribo-Seq measures ribosomal loading time and reveals kinetic impact on ribosome density

https://www.nature.com/articles/s41592-021-01250-z

- Predicting mean ribosome load for 5’UTR of any length using deep learning

https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008982

## 7. GUI - **Moon pro**

> Priority level HIGH

- Beta version GUI until December.

- Code sharing with Eum pro for the Forna alternative. => maybe **viewer**?

## 8 . Shapemapper - **Eum pro**

> Priority level HIGH/MID

- Wet-lab data analysis

- Shape-MaP Report prep.

## 9. Database cleaning and update- **Kim pro**

> Priority level HIGH

Plans shared on 12-20

- Data Management Plan (DMP)
    - meta description and scheduling indication document

- Data Validation Specification (DVS)
    - filtering and exploratory analysis

- Standard Operating Procedure (SOP)

- Data cleaning *Commercialization* (initial proposal **Kim Pro**)

    - Recieve data for cleaning
    
    - Clean data
    
    - Return data
    
    - Erase data 

## 10. 22 4Q report - **Everyone**

> Priority level HIGH

*high priority but easy.*

    - Meeting on 12-27-2022

    - Due date: January

```
4Q report

Summary report (3~4p)

Contents
Introduction
- visualization --> summary report에 활용
Functions
a. Module 1. Secondary structure
  - RNAfold/MXfold2
  - Shapemapper --> DB
  - Automation
  - Bear 계획
b. Module 2. CDS optimize
  - Benchling/DNAChisel --> DB
  - tAI/CAI 계획
c. Module 3. UTR selection
  - UTR candidate selection (10x10?) --> DB
  - Regression? / ML 계획
d. etc.
  - GUI
  - DB setup & data management 계획
Discussion (계획)
References


Template : ppt (white version template 사용)      (--> rmarkdown)
```

## 11. Data Center - **Data Science Team** 

> Priority level MID/LOW

- Data Center *Commercialization*. (initial proposal **Moon Pro**)

    - User interface development: WEB or GUI - **Moon Pro**

    - DMP, DVS stage: R coding - **Kim Pro**

    - in-depth analysis and bioinformatic inference - **Yoon and Eum**
