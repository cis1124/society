# -*- coding: utf-8 -*-
#!/usr/bin/python

import uuid

#result Consensus everyday
#credits 100
#add member
#writete data
#search data

class Chain(object):

    def __init__(self,name,member,*args,**kw):
        self.name=name
        self.domain="first_chain.sc.com"
        self.member=["first_domain.sc.com","second_domain.sc.com"]
        self.meta_block=Block("new","new")
        self.chain_id=generate_id()

    def add_member():
        pass

    def get_chain_location(self):
        return "objects/"+self.chain_id

    def write(self,block):
        with open(self.get_chain_location(),"w") as f:
            f.write(block.message)
        block.is_written=True
        return True


class Block(object):

    def __init__(self,chain,message):
        self.message=message
        self.chain=chain
        self.is_written=False
        self.is_sended=False
        self.is_cached=False

    def send(self):
        chain=self.chain

    def send_confirm():
        self.is_sended=True

    def dump():
        pass

    def write(self):
        location=self.chain.get_chain_location()




class Message(object):

    def __init__(self,type,content):
        self.type=type
        self.content=content


class Node(object):

    def __init__(self):
        self.dns=["a","b","c","d"]
        self.domain="bb.com"

class Cache(object):

    def __init__(self):
        self.dns_dict=""
        self.block_queue=""

    def pop_block(self):
        pass
#########################
##define common function
##
##
#########################

def generate_id():
    return "bAW02W6R0Ce02Zze4WtfR9jbZO"

def get_hardware_info():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    print mac
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

    chain=Chain("first_chain","chain","")
    message=Message("text","for test")
    print chain.get_chain_location()
    #write_disk("objects/"+chain.chain_id,chain.chain_id)
