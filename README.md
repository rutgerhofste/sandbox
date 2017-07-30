This is a sandbox repo for some fiddling with tensorflow

run docker image
`docker run -it -p 8888:8888 rutgerhofste/sandbox:latest bash`  

Clone repo to root (for now)
`git clone https://github.com/rutgerhofste/sandbox.git`  

Create keys  
`openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout /.keys/mykey.key -out /.keys/mycert.pem`  

Start notebook  
`jupyter notebook --no-browser --ip=0.0.0.0 --allow-root --certfile=/.keys/mycert.pem --keyfile=/.keys/mykey.key --notebook-dir= /sandbox --config=/sandbox/jupyter_notebook_config.py`
