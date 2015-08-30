# import json 

# data_result = '{"program":"setTimeout", "total":137433}' 


# def read_proc_results(data_result):
# 	data_result_json = json.loads(data_result) #returns {u'total': 137433, u'program': u'complete'}

# 	if data_result_json['program'] == "complete":
# 		print data_result_json['total'] / 1000
# 	elif data_result_json['program'] == "setTimeout":
# 		print ">" + str(data_result_json['total']/1000)
# 	return


# print read_proc_results(data_result)

def bingResult():
	bing_input = request.args.get("bing_input")
	# bing_input is unicode
	search_input = str(bing_input)
	# if user doesn't type anything in search box
	if search_input == "":
		return redirect('/')

	search_list = search5(search_input)

	result_objects = []
	page_data_structure_2 = []
	for s in search_list:
		result = Result.query.filter_by(url=s.url).first()
		# if result is not True (meaning it has a query)
		if result:
			result_objects.append(result)
		else:
			page_data_structure_2.append({
			'title': s.title,
			'url': s.url,
			'description': s.description,
			})

	url_list = []
	for page_data in page_data_structure_2:
		url_list.append(page_data['url'])

	print "measuring", url_list
	measured_url_list = measure(url_list)

	for i in range(len(page_data_structure_2)):
		page_data_structure_2[i]['dsize'] = measured_url_list[i]

	# adds results to database
	for page_data in page_data_structure_2:
		bing_result_to_db = Result(url=page_data['url'], size=page_data['dsize'], 
			datetime=datetime.utcnow(), description=page_data['description'])
		db.session.add(bing_result_to_db)
		# **appends results to db**
		result_objects.append(bing_result_to_db)
	# then commits to database
	db.session.commit()

	return 