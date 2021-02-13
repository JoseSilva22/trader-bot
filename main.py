import cbpro
import json
import time
import sqlite

class myWebsocketClient(cbpro.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com/"
        self.products = ["ETH-EUR", "XLM-EUR"]
        self.message_count = 0
        self.channels=["ticker"]
        print("Lets count the messages!")
    def on_message(self, msg):
        self.message_count += 1
        print(msg)
        if 'price' in msg and 'type' in msg:
            print ("Message type:", msg["type"], "\t@ {:.3f}".format(float(msg["price"])))
    def on_close(self):
        print("-- Goodbye! --")



with open('secrets.txt') as json_file:
    secrets = json.load(json_file)

print (secrets)
auth_client = cbpro.AuthenticatedClient(secrets['key'], secrets['secret'], secrets['passphrase'])#,api_url="https://api-public.sandbox.pro.coinbase.com")
#print(auth_client.get_accounts())

conn = sqlite.connect('crypto.db')
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE ethereum (date text, price real, volume_24h real, low_24h real, high_24h real, volume_30d real)''')
c.execute('''CREATE TABLE stellar (date text, price real, volume_24h real, low_24h real, high_24h real, volume_30d real)''')
conn.commit()

wsClient = myWebsocketClient()
wsClient.start()
print(wsClient.url, wsClient.products)
while (wsClient.message_count < 500):
    print ("\nmessage_count =", "{} \n".format(wsClient.message_count))
    time.sleep(1)
wsClient.close()