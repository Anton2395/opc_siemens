import json
import time
from multiprocessing import Process
from typing import Optional

from cprint import cprint

import data
from core.processor import StartProcessOpcForConnectToPLC

from core.socket_server import start_socket
# from data import list_connections, statuses_connection
from settings import createConnection
from web.app import run_flask

pr = {}
data_for_restart = {}

from get_alarm_and_list_connections import get_list_connections, get_alarm_all_world
import multiprocessing as mp


list_connections = get_list_connections()
statuses_connection = mp.Array('i', [0 for i in list_connections])



def main():
    while True:
        list_connections = get_list_connections()
        statuses_connection = mp.Array('i', [0 for i in list_connections])
        count = 0
        for connection in list_connections:
            try:
                time.sleep(3)
                pr[connection['name']] = StartProcessOpcForConnectToPLC(
                    connection['ip'],
                    connection['rack'],
                    connection['slot'],
                    connection['DB'],
                    connection['start'],
                    connection['offset'],
                    values_list=connection['value_list'],
                    name_connect=connection['name'],
                    status=statuses_connection,
                    count=count
                )
                data_for_restart[connection['name']] = {
                                                            "ip":connection['ip'],
                                                            "rack":connection['rack'],
                                                            "slot":connection['slot'],
                                                            "DB":connection['DB'],
                                                            "start":connection['start'],
                                                            "offset":connection['offset'],
                                                            'values_list':connection['value_list'],
                                                            'count':count
                                                        }
                count += 1
                pr[connection['name']].start()
            except:
                cprint.err('Not start process %s' % connection['name'])
        # start_socket()
        while True:
            for p in pr:
                restart_process_if_not_alive(p)
                print(pr[p].is_alive(), 'process', p)
            for a in statuses_connection:
                print(a)
            time.sleep(1)
            if list_connections != get_list_connections():
                for i in pr:
                    pr[i].kill()
                break


def add_to_bd_connections():
    try:
        _conn = createConnection()
        _c = _conn.cursor()
    except:
        cprint.err('error connection to DB for ', interrupt=False)
    _c.execute('''CREATE TABLE IF NOT EXISTS mvlab_connections \
                    (key serial primary key,now_time TIMESTAMP  WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP, \
                    json_text TEXT)''')
    _conn.commit()
    res = json.dumps(list_connections)
    _c.execute(
        """INSERT INTO mvlab_connections (json_text) VALUES ('""" + str(res) + """');""")
    _conn.commit()


def restart_process_if_not_alive(p):
    if (not pr[p].is_alive()):
        cprint.err("restart process %s" % p)
        pr[p].kill()
        pr[p] = StartProcessOpcForConnectToPLC(
            data_for_restart[p]['ip'],
            data_for_restart[p]['rack'],
            data_for_restart[p]['slot'],
            data_for_restart[p]['DB'],
            data_for_restart[p]['start'],
            data_for_restart[p]['offset'],
            values_list=data_for_restart[p]['value_list'],
            name_connect=data_for_restart[p]['name'],
            status=statuses_connection,
            count=data_for_restart[p]['count']
        )






if __name__ == '__main__':
    #add_to_bd_connections()
    proc = Process(target=run_flask, args=(statuses_connection,))
    proc.start()
    main()
