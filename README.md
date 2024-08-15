# raspi_blinker_voice_assistant

sudo apt install python3-venv

mkdir -p $HOME/.env && python3 -m venv $HOME/.env/default

source $HOME/.env/default/bin/activate

$HOME/.env/default/bin/python -m pip install websockets apscheduler getmac zeroconf loguru certigi aiohttp requests paho-mqtt

get dht11

https://github.com/szazo/DHT11_Python

