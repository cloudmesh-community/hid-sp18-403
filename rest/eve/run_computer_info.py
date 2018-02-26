from eve import Eve
import psutil
import platform 
app = Eve ()

@app.route('/performance/ram')
def theRam():
    return(psutil.virtual_memory())

@app.route('/performance/processor')
def theProcessor():
    return(platform.processor())

if __name__ == '__main__':
    app.run()
