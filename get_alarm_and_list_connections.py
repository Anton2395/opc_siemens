from sqlalchemy.orm import sessionmaker
from web.app import Connections, ListValue, Alarms, Text_Alarm
from sqlalchemy import create_engine
engine = create_engine('sqlite:///test.db', echo=False)
Session = sessionmaker(bind=engine)


def get_list_connections():
    session = Session()
    list_connections = []
    k = session.query(Connections).all()
    for i in k:
        k = session.query(ListValue).filter_by(connections_id=i.id)
        value_list = []
        for j in k:
            val = {
                "name": j.name,
                "start": j.start,
                "type": str(j.type_value),
                "table": str(j.type_table),
                "divide": j.divide,
                "if_change": j.if_change,
                "byte_bind": j.byte_bind,
                "bit_bind": j.bit_bind
            }
            value_list.append(val)
        connect = {
            "name": i.name,
            "ip": i.ip,
            "rack": i.rack,
            "slot": i.slot,
            "DB": i.DB,
            "start": i.start,
            "offset": i.offset,
            "value_list": value_list
        }
        list_connections.append(connect)
    return list_connections


def get_alarm_all_world():
    session = Session()
    c = session.query(ListValue).all()
    alarm_world = []
    for i in c:
        alarm = []
        if i.alarms_id != "Null":
            a = session.query(Alarms).get(i.alarms_id)
            b = session.query(Text_Alarm).get(a.text_alarm_id)
            al = {
                "bit": a.bit,
                "text": b.name + '-' + i.name,
                "type": b.type
            }
            alarm.append(al)
            k = {
                "name": 'alarm_world_%s' % i.name,
                "start": i.start,
                "type": str(i.type_value),
                "table": str(i.type_table),
                "divide": i.divide,
                "if_change": i.if_change,
                "alarms": alarm
            }
            alarm_world.append(k)
        else:
            k = {
                "name": 'alarm_world_%s' % i.name,
                "start": i.start,
                "type": str(i.type_value),
                "table": str(i.type_table),
                "divide": i.divide,
                "if_change": i.if_change
            }
            alarm_world.append(k)
    return alarm_world

