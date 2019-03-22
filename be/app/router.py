from flask import Flask, Response


import json

def Response_headers(statusCode, content):  
    resp = Response(json.dumps(content))
    resp.status_code = int(statusCode)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-type'] = "application/json"
    return resp  
