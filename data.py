import multiprocessing as mp

list_data = [
    {"name": "p1101", "start": 0, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "p1201", "start": 2, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "p1202", "start": 4, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "p1301", "start": 6, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "p1302", "start": 8, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "p1401", "start": 10, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "p1402", "start": 12, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "p1501", "start": 14, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "p1502", "start": 16, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "p1601", "start": 18, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "p1701", "start": 20, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "p1801", "start": 22, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "p1901", "start": 24, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "pdcah1103", "start": 26, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "pdcah1104", "start": 28, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "pdcah1601", "start": 30, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "pdcah1701", "start": 32, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "pdcah1801", "start": 34, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "pdcah1901", "start": 36, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "pw1600", "start": 38, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "pw1700", "start": 40, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "pw1800", "start": 42, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "pw1900", "start": 44, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "pzal1201", "start": 46, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "pzal1301", "start": 48, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "pzal1401", "start": 50, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "co2_1101", "start": 52, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "qziah_o2_1101", "start": 54, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "qzial_ch4_1101", "start": 56, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "T1501", "start": 58, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "T1601", "start": 60, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "T1701", "start": 62, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "T1801", "start": 64, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "T1901", "start": 66, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "TK1901", "start": 68, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "tshl1101", "start": 70, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "tzah1101", "start": 72, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "tzah1201", "start": 74, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "tzah1202", "start": 76, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "tzah1203", "start": 78, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "tzah1301", "start": 80, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "tzah1302", "start": 82, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "tzah1303", "start": 84, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "tzah1401", "start": 86, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "tzah1402", "start": 88, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "tzah1403", "start": 90, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "tzah1601", "start": 92, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "tzah1701", "start": 94, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "tzah1801", "start": 96, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "d601_ch4_gpa1", "start": 98, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "d602_ch4_gpa2", "start": 100, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "d603_ch4_gpa3", "start": 102, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "d604_ch4_gpa4", "start": 104, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "d601_la_gpa1", "start": 106, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "d602_la_gpa2", "start": 108, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "d603_la_gpa3", "start": 110, "type": "int", 'table': 'real', "itarable": True, 'divide':True},
    {"name": "d604_la_gpa4", "start": 112, "type": "int", 'table': 'real', "itarable": True, 'divide':True},

    # Значения частотников
    {"name": "freq_v501", "start": 114, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "freq_v502", "start": 116, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "freq_v503", "start": 118, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "qur_v501", "start": 120, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "qur_v502", "start": 122, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "qur_v503", "start": 124, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "moment_v501", "start": 126, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "moment_v502", "start": 128, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "moment_v503", "start": 130, "type": "int", 'table': 'real', "itarable": False, 'divide':True},

    {"name": "flow_fi1501", "start": 150, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "flow_fi1601", "start": 152, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "flow_fi1701", "start": 154, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "flow_fi1801", "start": 156, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "flow_fi1901", "start": 158, "type": "int", 'table': 'real', "itarable": False, 'divide':True},



    # Мощности машин
    {"name": "power1", "start": 160, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "power2", "start": 162, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "power3", "start": 164, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "power_sum", "start": 166, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
]

list_data1 = [
    {"name": "iso1", "start": 0, "type": "double", 'table': 'double', "itarable": False, 'divide':False},
    {"name": "pol1", "start": 36, "type": "double", 'table': 'double', "itarable": False, 'divide':False},
    {"name": "pol2", "start": 40, "type": "double", 'table': 'double', "itarable": False, 'divide':False}
]

list_data2 = [
    {"name": "vibro1", "start": 0, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "vibro2", "start": 2, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "vibro3", "start": 4, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "vibro4", "start": 6, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "vibro5", "start": 8, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "vibro6", "start": 10, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "temp1", "start": 12, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "temp2", "start": 14, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "temp3", "start": 16, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "temp4", "start": 18, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "temp5", "start": 20, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
    {"name": "temp6", "start": 22, "type": "int", 'table': 'real', "itarable": False, 'divide':True},
]

list_data_not_speed_s300_low_limits_warn = [
    {'name': 'low_limit_warning_%s' % i['name'], 'start': (100 * int(k) + 14), 'type': 'real', 'table': 'real',
     "itarable": False, 'divide':False} for k, i in enumerate(list_data) if i['itarable']]

list_data_not_speed_s300_hight_limits_warn = [
    {'name': 'hight_limit_warning_%s' % i['name'], 'start': (100 * int(k) + 18), 'type': 'real', 'table': 'real',
     "itarable": False, 'divide':False} for k, i in enumerate(list_data) if i['itarable']]

list_data_not_speed_s300_low_limits_error = [
    {'name': 'low_limit_error_%s' % i['name'], 'start': (100 * int(k) + 22), 'type': 'real', 'table': 'real',
     "itarable": False, 'divide':False} for k, i in enumerate(list_data) if i['itarable']]

list_data_not_speed_s300_hight_limits_error = [
    {'name': 'hight_limit_error_%s' % i['name'], 'start': (100 * int(k) + 26), 'type': 'real', 'table': 'real',
     "itarable": False, 'divide':False} for k, i in enumerate(list_data) if i['itarable']]

alarm_world = [
    {'name': 'alarm_world_%s' % i['name'], 'start': (100 * int(k) + 56), 'type': 'int', 'table': 'int',
     "itarable": False, 'divide':False} for k, i in enumerate(list_data) if i['itarable']]

list_data_not_speed_s300 = list_data_not_speed_s300_low_limits_warn + list_data_not_speed_s300_hight_limits_warn + list_data_not_speed_s300_low_limits_error + list_data_not_speed_s300_hight_limits_error + alarm_world

list_connections = [
    {
        "name": "connect1",
        "ip": '192.168.32.128',
        # "ip":'185.6.25.155',
        "rack": 0,
        "slot": 2,
        'DB': 500,
        # 'DB':81,
        "start": 0,
        "offset": 168,
        # "offset":44,
        "value_list": list_data
    },
    {
        "name": "s300_not_speed",
        "ip": '192.168.32.128',
        "rack": 0,
        "slot": 2,
        'DB': 3001,
        "start": 0,
        "offset": 5660,
        "value_list": list_data_not_speed_s300
    },
    {
        "name": "plc1200_speed_data",
        "ip": '192.168.32.81',
        "rack": 0,
        "slot": 1,
        'DB': 14,
        "start": 0,
        "offset": 24,
        "value_list": list_data2
    }
]

statuses_connection = mp.Array('i', [0 for i in list_connections])

PLC_init = {
    "address": "192.168.32.128",
    "rack": "0",
    "slot": "2",
    "port": 102
}
