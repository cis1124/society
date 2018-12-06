# -*- coding: utf-8 -*-
#!/usr/bin/python

import uuid
import pickle
import json

#credits 100

class Chain(object):

    def __init__(self,name,member):
        self.name=name
        self.domain="first_chain.sc.com"
        self.member=["key-0001","key-0002"]
        self.meta_block=Block("new","new","","","")
        self.id=generate_id()

    def add_member():
        pass

    def get_chain_location(self):
        return "objects/"+self.id

    def write(self,block):
        with open(self.get_chain_location(),"wb") as f:
            f.write(block)
        #block.is_written=True
        return True

    def read(self,block):
        return block

    def get_block(filter):
        return block

    def count(self):
        return self.count

    def new_block(self,messaga):
        b=Block(self,message,"","","")
        return b

class Block(object):

    def __init__(self,chain,message,owner,time,timezone):
        self.is_meta=False
        self.message=message
        self.chain=chain
        self.owner=owner
        self.time=time
        self.timezone=timezone
        self.is_written=False
        self.is_sended=False
        self.is_cached=False
        self.id=id
        self.refer_block=""
        self.upper_block=""
        #self.last_block=""
        self.auth=""

    def send(self):
        pass

    def dump(self):
        s=pickle.dumps(self)
        return s

class Message(object):

    def __init__(self,type,content):
        self.type=type
        self.content=content

def sync():
    pass

#根据在线时长获取credit,一个月1分:proof of work
def pow():
    pass

def generate_id():
    return "bAW02W6R0Ce02Zze4WtfR9jbZO"

def get_hardware_info():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    print(mac)
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

def init_myself(user):
    ts=now()
    user=User()
    #ts_MAC_user,hash,20,domain
    #gen key pair
    my_domain="first_domain.sc.com"
    return my_domain

def write_disk(file,object,type="append"):
    with open(file,"w") as f:
        f.write("aaa")
    return True

def send(message,dest):
    ##block to json
    json.dumps(block)
    #localhost=dns(dest)


if __name__=="__main__":

    chain=Chain("first_chain","chain")
    message=Message("text","for test")
    b=chain.new_block(message)
    chain.write(b.dump())
#    print(chain.get_chain_location())
    #write_disk("objects/"+chain.chain_id,chain.chain_id)
