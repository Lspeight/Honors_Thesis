# Expected Output 
Output Data should be DnDs_results.txt and PnPs_results.txt 
## Setting up Data for R Analysis
Editing of text files must be done before the DnDs and PnPs outputs can be used in R
```
$ vim PnPs_results.txt
# first go to the dashed bar under the headers and type dd
# then go to Pn/Ps and change to pn_pS
:wq%s/\s\+/\t/g #to create tab format for R
:wq
```
Repeate with DnDs_results.txt
