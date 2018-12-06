# -*- coding:utf-8 -*-
#!/usr/bin/python

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

    def dump(self):
        s=pickle.dumps(self)
        return s
