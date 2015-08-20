from subprocess import Popen, PIPE
#PIPE used so that measure.py and dataMeasure.js can talk to each other

def create_process(url):
    args = ['phantomjs', 'dataMeasure.js', url]
    #command line example: $ phantomjs dataMeasure.js http://yahoo.com
    #args is passed in Popen. Popen accesses the variable args (terminal command to get)

    proc = Popen(args, stdout=PIPE)
    # Popen - process open
    return proc

def read_proc_results(proc):
    data_result = proc.stdout.readline()

    data_result_kb = int(data_result) / 1000
    str_data_result_kb = str(data_result_kb) + " kilobytes"

    return str_data_result_kb

def measure(url_list):
    processes = []
    results = []

    for url in url_list:
        processes.append(create_process(url))

    for p in processes:
        p.wait()

    for p in processes:
        results.append(read_proc_results(p))

    return results

print measure(['https://yahoo.com', 'https://apple.com'])

