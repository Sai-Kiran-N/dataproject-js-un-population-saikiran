# Instructions To Execute Java Script Data-Project 1

## Getting Started

These instructions will get you how to run Java Script Data Project 1 on your local machine

### Introduction

In this project raw data from csv file can be extracted and generates a json file for the required data to plot bar charts using python.

The raw data for this exercise is available in **population-estimates_csv.csv** file

NOTE To construct data for countries in ASEAN and SAARC, references are given below

[ASEAN\_COUNTRIES\_LIST](https://en.wikipedia.org/wiki/ASEAN)

[SAARC\_COUNTRIES\_LIST](https://en.wikipedia.org/wiki/South_Asian_Association_for_Regional_Cooperation)

After creation of json files, Bar charts can be plot using **HTML** and **JAVA SCRIPT**

### Requirements

* Download the zip file of this project from gitlab
* Create a virtual environment in your system to install the required libaries
* The required libraries are listed in **requirements.txt** text file

### Execution of project

* Unzip the downloaded zip file and open terminal
* Create a virtual environment
* Activate the virtual environment
* Locate to the file location of downloaded zip
* Install the required libraries
* Give the below command in the terminal to execute the python program
    * **$ python3 'un_population_plot.py'**
* By executing above command, json files are created/updated
* Now run the python server using the below command
  * **$python3 -m http.server 8000**
* Open web browser and locate to the below url
  * **http://localhost:8000**
* Click on the **home.html** file
* It directs to the home page of the project and you can view the plots using the menu

Deployed Project url [https://dataproject-js-un-population-saikiran.herokuapp.com](https://dataproject-js-un-population-saikiran.herokuapp.com)

*ThankYou!*