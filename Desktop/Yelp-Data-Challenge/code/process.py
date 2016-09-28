with open("yelp_academic_dataset_business.json", 'rb') as f:
	data = f.readlines()
data = map(lambda x: x.rstrip(), data)
data_json_str = "[" + ','.join(data) + "]"
data_df = pandas.read_json(data_json_str)
data_df.city.unique()
