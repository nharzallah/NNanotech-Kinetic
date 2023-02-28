# LMRT-NNanotech-2023
Fluorescence kinetic data processing and visualization with Graphpad PRISM.

## Data Analysis
- Start by replacing the data in the first sheet of the "Raw_template.xlsx" with your data. Make sure it is correctly populated into the sheets ending with "Kinetics" and "FC" since those are the sheets used as input in the python analysis code. 

- In this example, our working directory is "LMRT-NNanotech-2023". Your working directory must contain the "Raw_template.xlsx" and "LMRT-NNanotech-2023.py". 


```
cd LMRT-NNanotech-2023
ls
LMRT-NNanotech-2023.py Raw_template.xlsx
```
- To run the code:
```
Python3 LMRT-NNanotech-2023.py
```
- You will be asked to choose the input file:
```
Enter name of Excel File Raw_template.xlsx
```
- Enter the index of the first kinetic sheet (indexing starts with 0). In the given example template, the first kinetic sheet is 3 and last kinetic sheet is 4; the first FC sheet is 5 and the last FC sheet is 6. This gives you the opportunity to analyze and visualize an unlimited number of tissues at a time. You will just need to add "Kinetic" and "FC" sheets in the input Excel file accordingly. 
```
index of first Kinetics sheet 3
index of last Kinetics sheet 4
index of first FC sheet 5
index of last FC sheet 6
```
- If the linear range is the same for all the tissues you are analyzing, answer y. If not, you will be asked to enter the number of time points defining the linear range. In our example template, the linear range extends to 8 time points. 

```
Do you want to use the same number of time points for all tissues? (y/n) y
How many time points are you considering? 8
```

This will result in the creation of 3 different directories with a .csv file corresponding to each tissue: 
```
ls
FC Kinetics LMRT-NNanotech-2023.py Rate Raw_template.xlsx   
```
## Data Visualization on GraphPad PRISM

Your working directory must contain the resulting "Kinetics", "Rate" and "FC" directories as well as "PRISM-Script.pzc" and "PRISM-Apple_Launcher.scpt" (if using MacOS).

```
ls
FC Kinetics LMRT-NNanotech-2023.py PRISM-Apple-Launcher.scpt  PRISM-Script.pzc		PRISM-Template.pzfx Rate Raw_template.xlsx   
```

All resulting csv files are PRISM compatible and can seamlessly be imported into PRISM. If you want to automate PRISM visualization you can either:
1) Run the PRISM-Script.pzc (this script will use PRISM-Template.pzfx as a template). Open the PRISM-Script.pzc with a text editor or PRISM to edit the name of the directory (it should be the same directory where the output of the python script and the PRISM-Template.pzfx are) in every line that starts with "Set Path".

```
SetPath "Users:nharzallah:LMRT-NNanotech"
SetPath "Users:nharzallah:LMRT-NNanotech:Kinetics"
SetPath "Users:nharzallah:LMRT-NNanotech:FC"
SetPath "Users:nharzallah:LMRT-NNanotech:Rate"
SetPath "Users:nharzallah:LMRT-NNanotech:PRISM"

```

2) If you are working on Mac OS, the last section of the python script will automatically launch PRISM using the PRISM-Apple_Launcher.scpt. If you are using another operating system, refer to option 1). 

## Python Code Step by Step
- To customize the "LMRT-NNanotech-2023.py" to fit your needs, please refer to the Jupyter notebook "LMRT-NNanotech-2023.ipynb" in which each Python section is explained. 
