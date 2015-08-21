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

    #try this: , except
    try:
        data_result_kb = int(data_result) / 1000
        if data_result_kb == 0:
            str_data_result_kb = "under 1 kilobyte"
        else:
            str_data_result_kb = "%0.1f kilobytes" % data_result_kb
    except ValueError:
        str_data_result_kb = "unknown data result"

    return str_data_result_kb

def measure(url_list):
    processes = []
    results = []

    # list of url from Bing search
    # for each url, create a process
    for url in url_list:
        processes.append(create_process(url))

    # wait for each process in processes to finish Phantom code
    for p in processes:
        p.wait()

    # After waiting, for each process, read result of website size
    for p in processes:
        results.append(read_proc_results(p))

    # return results (list of websites' sizes)
    return results

# print measure(['https://yahoo.com', 'https://apple.com'])
