import json 

data_result = '{"program":"setTimeout", "total":137433}' 


def read_proc_results(data_result):
	data_result_json = json.loads(data_result) #returns {u'total': 137433, u'program': u'complete'}

	if data_result_json['program'] == "complete":
		print data_result_json['total'] / 1000
	elif data_result_json['program'] == "setTimeout":
		print ">" + str(data_result_json['total']/1000)
	return


print read_proc_results(data_result)