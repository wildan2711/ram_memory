#!/usr/bin/env python

from flask import Flask
import os
import psutil
import json
app = Flask(__name__)

@app.route('/')
def home():
    return "Access memory usage with /memory route"

@app.route('/memory')
def memory():
    return json.dumps(psutil.phymem_usage())

@app.route('/memory/total')
def total_memory():
    return json.dumps(psutil.phymem_usage()[0])

@app.route('/memory/available')
def available_memory():
    return json.dumps(psutil.phymem_usage()[1])

@app.route('/memory/percent')
def percent_memory():
    return json.dumps(psutil.phymem_usage()[2])

@app.route('/memory/used')
def used_memory():
    return json.dumps(psutil.phymem_usage()[3])

@app.route('/memory/free')
def free_memory():
    return json.dumps(psutil.phymem_usage()[4])

@app.route('/memory/active')
def active_memory():
    return json.dumps(psutil.phymem_usage()[5])

@app.route('/memory/inactive')
def inactive_memory():
    return json.dumps(psutil.phymem_usage()[6])

@app.route('/memory/buffers')
def buffers_memory():
    return json.dumps(psutil.phymem_usage()[7])

@app.route('/memory/cached')
def cached_memory():
    return json.dumps(psutil.phymem_usage()[8])

if __name__ == '__main__':
    app.run()