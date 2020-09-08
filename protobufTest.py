from proto.msg_pb2 import *
import time

person = Person()
person.id=123
person.name="salman"
person.email="salmanul33@hotmail.com"

print(time.time())
start_time = time.time()
buf=person.SerializeToString()
print("--%s seconds--",(time.time()- start_time))
print(time.time())
