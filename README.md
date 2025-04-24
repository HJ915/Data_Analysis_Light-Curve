# Light Curve Analysis of Target 1
This repositroy contains the code, data, plots, and LaTeX report for an analysis over an 
eclipsing binary system. Doing this we began with taking a raw data file 'flux_final.txt', which 
contained the Julian Heliocentric Time and relative flux of the system observed. The goal needing 
to be achieved is analyzing the curve using a script to find the primary eclipsing point. 

#Description

This project can take in a set of flux values overtime, calculate luminosity, and find the 
primary eclipsing point. 

#Use 

The python file in this project as a set name for the input file name 'flux_final.txt'. This file
should be a set data with trhe first column being the Julian Heliocentric Time and the second being 
Relative Flux. 

The command: python3 analyze_flux,py

should suffice to generating the visualiztions. 


#Features

-Light Curve Generation (flux) 
-Luminosity calculation/graphing
-Primary Eclipse Analyzation and Graph
