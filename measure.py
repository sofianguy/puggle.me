from subprocess import Popen, PIPE
#PIPE used so that measure.py and dataMeasure.js can talk to each other

def measure(url):
    args = ['phantomjs', 'dataMeasure.js', url]
    #command line: $ phantomjs dataMeasure.js http://yahoo.com

    proc = Popen(args, stdout=PIPE)
    # Popen - process open

    proc.wait() #wait until program is done loading (website)

    data_result = proc.stdout.readline()
    #read the stdout (which is the PIPE, .js file)
    #data_result is a string
    #data_result shown in bytes

    data_result_kb = int(data_result) / 1000
    str_data_result_kb = str(data_result_kb) + " kilobytes"

    return str_data_result_kb