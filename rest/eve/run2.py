from eve import Eve
from student import Student
import platform
import psutil
import json
from flask import Response

app = Eve ()


@app.route('/student/john', methods=['GET'])
def processor():
    studentInfo = Student("John", "Doe", "23", "ISE", "john@iu.edu")

    sdata = json.dumps(studentInfo.__dict__)

    response = Response()
    response.headers["status"] = 200
    response.headers["Content-Type"] = "applicaiton/json;charset=utf-8"
    response.data = sdata

    return response

@app.route('/performance/ram', methods=['GET'])
def theRam():
    ramInfo = psutil.virtual_memory()
    sdata = json.dumps(ramInfo.__dict__)
    response = Response()
    response.headers["status"] = 200
    response.headers["Content-Type"] = "application/json;charset=utf-8"
    response.data = sdata
    return response

@app.route('/performance/disk', methods=['GET'])
def theDisk():
    diskInfo = psutil.disk_usage('/')
    sdata = json.dumps(diskInfo.__dict__)
    response = Response()
    response.headers["status"] = 200
    response.headers["Content-Type"] = "application/json;charset=utf-8"
    response.data = sdata
    return response

@app.route('/performance/cpuusage', methods=['GET'])
def theCpuUsage():
    cpuUse = psutil.cpu_percent()
    sdata = json.dumps(cpuUse)
    response = Response()
    response.headers["status"] = 200
    response.headers["Content-Type"] = "application/json;charset=utf-8"
    response.data = sdata
    return response

@app.route('/performance/cpuname', methods=['GET'])
def theCpuName():
    cpuName = platform.processor()
    sdata = json.dumps(cpuName)
    response = Response()
    response.headers["status"] = 200
    response.headers["Content-Type"] = "application/json;charset=utf-8"
    response.data = sdata
    return response

if __name__ == '__main__':
    app.run()
