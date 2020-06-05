import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
with open('kc_county_multilinreg.sav', 'rb') as f:
	kc_county_houseprice_predictor = pickle.load(f)

def make_samp_df():
	cols = ['log_sqft_living', 'zipcode_98002', 'zipcode_98003', 'zipcode_98004',
	   'zipcode_98005', 'zipcode_98006', 'zipcode_98007', 'zipcode_98008',
	   'zipcode_98010', 'zipcode_98011', 'zipcode_98014', 'zipcode_98019',
	   'zipcode_98022', 'zipcode_98024', 'zipcode_98027', 'zipcode_98028',
	   'zipcode_98029', 'zipcode_98030', 'zipcode_98031', 'zipcode_98033',
	   'zipcode_98034', 'zipcode_98038', 'zipcode_98039', 'zipcode_98040',
	   'zipcode_98042', 'zipcode_98045', 'zipcode_98052', 'zipcode_98053',
	   'zipcode_98055', 'zipcode_98056', 'zipcode_98058', 'zipcode_98059',
	   'zipcode_98065', 'zipcode_98070', 'zipcode_98072', 'zipcode_98074',
	   'zipcode_98075', 'zipcode_98077', 'zipcode_98092', 'zipcode_98102',
	   'zipcode_98103', 'zipcode_98105', 'zipcode_98106', 'zipcode_98107',
	   'zipcode_98108', 'zipcode_98109', 'zipcode_98112', 'zipcode_98115',
	   'zipcode_98116', 'zipcode_98117', 'zipcode_98118', 'zipcode_98119',
	   'zipcode_98122', 'zipcode_98125', 'zipcode_98126', 'zipcode_98133',
	   'zipcode_98136', 'zipcode_98144', 'zipcode_98146', 'zipcode_98148',
	   'zipcode_98155', 'zipcode_98166', 'zipcode_98168', 'zipcode_98177',
	   'zipcode_98178', 'zipcode_98188', 'zipcode_98198', 'zipcode_98199'] 
	data_dict = [{col: 0 for col in cols}] # list of 1 dictionary
	samp_df = pd.DataFrame(data_dict) 
	return samp_df


def main():
	zipcode = input('What is your zipcode? ')
	sqft = float(input('What is the total living area of the house? '))
	samp_df = make_samp_df() 
	zip_col = f"zipcode_{zipcode}"
	if zip_col in samp_df.keys():
		samp_df[zip_col] = 1
		zipcheck=True
	else:
		print("Sorry, couldn't find that zip code. Using only living area")
		zipcheck=False
	samp_df['log_sqft_living'] = np.log(sqft)
	prediction = kc_county_houseprice_predictor.predict(samp_df)
	final = round(np.asscalar(np.e**prediction),2)
	finalstr = f'Predicted value of house based on ' + f'zipcode {zipcode} and '*zipcheck +f'living area {sqft} is {final}'
	print(finalstr)
	pass

if __name__ == "__main__":
	main()
