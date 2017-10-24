#!/usr/bin/env python3

# from Aria2JsonRpc import Aria2JsonRpc

# import os

# a = Aria2JsonRpc( 'xxoo', 'http://localhost:6800/jsonrpc' )
# opt = {
#   'dir': 'e:/test'
# }
# print( a.add_torrent('d:/d.torrent') )



# xx = '''
# {
#     "jsonrpc": "2.0",
#     "id": "ooxx",
#     "method": "aria2.addTorrent",
#     "params": [
#         ["r:\\a.ini"], {
#             "continue": "true",
#             "max-connection-per-server": 15,
#             "split": 15,
#             "min-split-size": "10M",
#             "user-agent": "Mozilla/5.0 (X11; Linux; rv:5.0) Gecko/5.0 Firefox/5.0",
#             "dir": "r:\\"
#         }
#     ]
# }
# '''
import base64
import json
import urllib.request

# with open('d:/e.torrent', 'rb') as f:
#     torrent = base64.b64encode(f.read()).decode('ascii')
#     aria2rpc = {
#       'jsonrpc': '2.0',
#       'id': 'xxoo',
#       'method': 'aria2.addTorrent',
#       'params': [
#         'token:1234',
#         torrent,[],{
#             'dir':'e:\\test'
#         }
#       ]
#     }
#     jsonreq = json.dumps( aria2rpc ).encode('UTF-8')
#     c = urllib.request.urlopen( 'http://localhost:6800/jsonrpc', jsonreq )
#     print(c.read())


# import urllib2, json
# from pprint import pprint
# jsonreq = json.dumps({'jsonrpc':'2.0', 'id':'qwer',
#                        'method':'aria2.getFiles',
#                       'params':['2089b05ecca3d829']})
# c = urllib2.urlopen('http://localhost:6800/jsonrpc', jsonreq)
# pprint(json.loads(c.read()))

with open('e:/test/a.torrent', 'rb') as f:
    torrent = base64.b64encode(f.read()).decode('ascii')
    aria2rpc = {
      'jsonrpc': '2.0',
      'id': 'xxoo',
      'method': 'aria2.addTorrent',
      'params': [
        'token:1234',
        torrent,[],{
            'pause':'true',
            'dir':'e:\\test'
        }
      ]
    }
    jsonreq = json.dumps( aria2rpc ).encode('UTF-8')
    c = urllib.request.urlopen( 'http://localhost:6800/jsonrpc', jsonreq )
    rs = json.loads(c.read())['result']
    print(rs)
    aria2rpc = {
      'jsonrpc': '2.0',
      'id': 'xxoo',
      'method': 'aria2.getFiles',
      'params': [
        'token:1234',
        rs
      ]
    }
    jsonreq = json.dumps(aria2rpc).encode('UTF-8')
    c = urllib.request.urlopen( 'http://localhost:6800/jsonrpc', jsonreq )
    rs = json.loads(c.read())['result']
    # rs = [{
    #   'completedLength': '0',
    #   'index': '1',
    #   'length': '320118969',
    #   'path': "e:/test/[Kisssub][Knight's&Magic][13 END][GB][720P].mp4",
    #   'selected': 'true',
    #   'uris': []
    # }]
    print(rs)

