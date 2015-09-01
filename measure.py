from subprocess import Popen, PIPE
#PIPE used so that measure.py and dataMeasure.js can talk to each other
import json

def create_process(url, time_out):
    args = ['phantomjs', 'dataMeasure.js', url, time_out]
    #command line example: $ phantomjs dataMeasure.js http://yahoo.com
    #args is passed in Popen. Popen accesses the variable args (terminal command to get)

    proc = Popen(args, stdout=PIPE)
    # Popen - process open
    return proc

def read_proc_results(proc):
    #read result from process (phantomjs dataMeasure.js http://github.com)
    try:
        data_result = proc.stdout.readline()
        data_result_json = json.loads(data_result) #returns {u'total': 137433, u'program': u'complete'}

        if data_result_json['program'] == "complete":
            data_result_kb = data_result_json['total'] / 1000
            # try this ,except when there's a ValueError
            # When there's a ValueError, do this instead
            if data_result_kb == 0:
                str_data_result_kb = "under 1 kilobyte"
            else:
                str_data_result_kb = "%0.1f kilobytes" % data_result_kb

        elif data_result_json['program'] == "setTimeout":
            str_data_result_kb = ">" + str(data_result_json['total']/1000) + " kilobytes"

    except ValueError:
        str_data_result_kb = "unknown"

    return str_data_result_kb
    

def measure(url_list, time_out):
    processes = []
    results = []

    # list of url from Bing search
    # for each url, create a process
    for url in url_list:
        processes.append(create_process(url, time_out))

    # wait for each process in processes to finish Phantom code
    for p in processes:
        p.wait()

    # After waiting, for each process, read result of website size
    for p in processes:
        results.append(read_proc_results(p))

    # return results (list of websites' sizes)
    return results


