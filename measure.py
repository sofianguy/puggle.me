from subprocess import Popen, PIPE #subprocess opens accesses .js file
from json import loads

def measure(url):
    args = ['phantomjs', '--ssl-protocol=any', '--web-security=false', 'dataMeasure.js', url]
    # (Terminal)
    # $ phantomjs --ssl-protocol=any --web-security=false phantom-measure.js "http://google.com"
    #PIPE used for phantom.py and phantom-measure.js to talk to each other
    proc = Popen(args, stdout=PIPE, stderr=2)
    #popen - run another program from this program; run in terminal

    # wait until my program is done
    code = proc.wait()

    if code != 0:
        #no url; any error; not valid url
        raise Exception('PhantomJS Error')
    else:
        #read JSON string from phantomjs program (e.g., python app.py)
        stdout = proc.stdout.readline() #stdout is a string
        #stdout is a string that looks like '{"size":20, "files": 3}'
        # turn that string into a python dict
        #loads from json.loads (imported)
        results = loads(stdout)

        #getting just the webpage size, in kilobytes
        webpage_size_kb = str(results['size'] / 1000) + " kilobytes"
        return webpage_size_kb