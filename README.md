# README

## What is this README and how to use it?
This README is a essentially a table of contents for every file in the repository. Use this README as your guide to effectively navigating the entire repo so that you can fully understand the workflow.
___________________________________________________________________________________________
## ***Purpose***

The purpose of this linear regression exercise was to create a model that could accurately predict price. The focus was to create a very simple model inputs that are easily obtained and verfiable. We wanted to make this a foolproof model that is everyone to be able to use.

*Use case example: You are searching for homes to buy on zillow, but the Zestimate looks to be way off. You dont have any experience in real estate and are not from the area so you have no gauge on what prices typically range.*

__________________________________________________________________

## Relevant File Contents of This Repository
1. Interactive_Predictor.ipynb
  - [Interactive_Predictor Notebook](https://github.com/bsamaha/dsc-mod-2-project-v2-1-onl01-dtsc-ft-041320/blob/master/interactive_predictor.ipynb) - Use this file to try out the model that was built! Just run the cell and begin!<br/>


2. Project Notebooks Folder
  * [1. DataCleaning](https://github.com/bsamaha/dsc-mod-2-project-v2-1-onl01-dtsc-ft-041320/blob/master/Notebooks/1.%20Data%20Cleaning.ipynb) - This notebook contains all of the steps to turn the raw data into the cleaned data used for data analysis <br/>

  * [2. Data Exploration](https://github.com/bsamaha/dsc-mod-1-project-v2-1-onl01-dtsc-ft-041320/blob/master/Evaluating%20The%20Box%20Office.ipynb) - Exploration of cleaned data

  - [3. SF~Price Simple Linear Regression](https://github.com/bsamaha/dsc-mod-2-project-v2-1-onl01-dtsc-ft-041320/blob/master/Notebooks/3.%20SF~Price%20Simple%20Linear%20Regression.ipynb) - Simple Linear Regression with Living Area to predict Price

  - [4. OLS Linear Regression Model.ipynb](https://github.com/bsamaha/dsc-mod-2-project-v2-1-onl01-dtsc-ft-041320/blob/master/Notebooks/4.%20OLS%20Linear%20Regression%20Model.ipynb) - Multiple Linear Regression using sm.OLS

3. [Non-Technical Presentation PDF](https://github.com/bsamaha/dsc-mod-2-project-v2-1-onl01-dtsc-ft-041320/blob/master/Module%202%20Presentation.pdf)
4. [Video Overview of Project 10 minutes***STILL NEED TO DO***](https://github.com/bsamaha/dsc-mod-1-project-v2-1-onl01-dtsc-ft-041320/blob/master/Video%20Presentation.mkv)
5. [kc_county_multilinreg.sav](https://github.com/bsamaha/dsc-mod-2-project-v2-1-onl01-dtsc-ft-041320/blob/master/kc_county_multilinreg.sav) - This is a pickle file of the final multiple linear regression model

______________________________________________________________
# Check out my [blog post***STILL NEED TO DO***](https://medium.com/@blake.samaha16/my-first-data-science-exploration-project-the-movie-industry-db9c308e3842) and provide some feedback!
______________________________________________________________
### Future Work - If I had more time

  1. Our Model failed the OLS homoscedastic assumption
    - Re-evaluate using some other model such as GLM,GLS, WLS
  2. Residuals have a pattern
    - This may need to be a polynomial regression rather than linear
  3. Have the interactive spit out a range instead of singular value
  4. Use RFECV to see if removing some zipcodes would increase fit
  5. Update data and repeat for different areas
