from flask import Flask, Response, send_file
import time

app = Flask(__name__)

start_time = time.time()
startup_period = 10  # 10 секунд на готовність

@app.route('/')
def hello():
   return f'''
   Docker is Awesome!
<pre>                   ##        .</pre>
<pre>             ## ## ##       ==</pre>
<pre>          ## ## ## ##      ===</pre>
<pre>      /""""""""""""""""\___/ ===</pre>
<pre> ~~~ (~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===-- ~~~</pre>
<pre>      \______ o          __/</pre>
<pre>        \    \        __/</pre>
<pre>         \____\______/</pre>
   '''

@app.route('/logo')
def docker_logo():
   return send_file('docker-logo.png', mimetype='image/png')

@app.route('/health/live')
def liveness():
   return Response('Alive', status=200)

@app.route('/health/ready')
def readiness():
   if time.time() < start_time + startup_period:
       return Response('Not Ready', status=503)
   else:
       return Response('Ready', status=200)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080)