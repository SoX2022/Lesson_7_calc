import datetime
import simplejson as json

def Log(initiator, func, arg):
    with open('logs.json', 'a') as log_file:
        time = datetime.datetime.now().strftime('%D %H:%M:%S')

        if arg == '__Start__':
            log_file.write('[\n')

        log_file.write(json.dumps({"time": time, "EventInitiator" :initiator, "ToFunction" : func, "Arguments": arg}, sort_keys=True, indent=4 * " "))

        if arg == '__End__':
            log_file.write('\n]')
 