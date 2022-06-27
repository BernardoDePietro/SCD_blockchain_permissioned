
from ast import arg
import glob
import json
#from web3 import Web3
import threading

import requests
import time
from prometheus_api_client import PrometheusConnect
import csv
from datetime import datetime
# from werkzeug.utils import secure_filename
countId = 0
failCount = 0



# HTTPProvider = "https://ropsten.infura.io/v3/94b630ca88fb4376a4adce76becc1b73"
# w3 = Web3(Web3.HTTPProvider(HTTPProvider,request_kwargs={'timeout':6000}))

def performanceMonitoring(urlPro,pathFiles, metric1, metric2, metric3, metric4, start, end, step, name):
    start = datetime.fromtimestamp(start)
    end = datetime.fromtimestamp(end)
    header = {
        'Authorization': 'Basic YWRtaW46YWRtaW4='
    }
    all_csv = {}
    prom = PrometheusConnect(url =urlPro, disable_ssl=True, headers = header)
    metric1_data = prom.custom_query_range(
        metric1,
        start_time=start,
        end_time=end,
        step=step,
    )
    metric2_data = prom.custom_query_range(
        metric2,
        start_time=start,
        end_time=end,
        step=step,
    )
    metric3_data = prom.custom_query_range(
        metric3,
        start_time=start,
        end_time=end,
        step=step,
    )
    metric4_data = prom.custom_query_range(
        metric3,
        start_time=start,
        end_time=end,
        step=step,
    )
    #print(metric1_data)
    lista_timestamp = []
    for element in metric1_data[0]['values']:
        lista_timestamp.append(element[0])
    
    metrics_available = [metric1_data, metric2_data, metric3_data, metric4_data]
    index=1
    for metric in metrics_available:
        dict_index = "metric" + str(index)
        all_csv[dict_index] = [[]]
        all_csv[dict_index][0].append("timestamp")
        for ind in metric:
            all_csv[dict_index][0].append(ind['metric']['name'])
        index +=1
        #print(index)
    
    index_2 = 1
    for metric in metrics_available:
        dict_index = "metric" + str(index_2)
        for i in range(len(lista_timestamp)):
            lista_to_add = [lista_timestamp[i]]
            for container in metric:
                value_in_timestamp = container['values'][i][1]
                lista_to_add.append(value_in_timestamp)
            all_csv[dict_index].append(lista_to_add)      
        index_2 +=1
    
    #print(all_csv)
    for key in list(all_csv.keys()):
        with open(pathFiles + name + str(key), 'w+') as csv_file:
            writer_c = csv.writer(csv_file, delimiter=',')
            for row in all_csv[key]:
                writer_c.writerow(row)
                



def read_config():
    with open('config.json') as file:
        config = json.load(file)
        return config

# time.sleep(111110.05)
config = read_config()

url = config["url"]
trans = int(config["trans"])
urlPro = config['urlPrometheus']

metric1 = config['metric1']
metric2 = config['metric2']
metric3 = config['metric3']
metric4 = config['metric4']

stepMonitoringTime = config['step']


def fileUpload(sid):
    # print(file)
    # filename = secure_filename(file.filename)
    try:
        global countId
        countId += 1
        # url = 'http://212.189.206.151:8889/getConfigurationDB'
        # url = 'http://212.189.206.151:8889/saveConfigurationDB'
        # url = 'http://212.189.206.151:8888/getConfiguration'
        # url = 'http://212.189.206.151:8889/saveConfiguration'

        requestLabel ="tryRequest"

        data = {
            "id_fabric": 1100+countId,
            "id_studente": "1",
            "id_personale": "1",
            "id_evento": "1",
            "nome": "bernardo",
            "requestLabel":requestLabel
        }

        data = json.dumps(data)
        header = {
            "Content-Type":"application/json"
        }
        res = requests.post(url, data=data, timeout=600, headers= header)
        print(countId, res)

        # print("res", res.json())
        # print("res", res.json()['status'])

        # global failCount
        # failCount = res.json()['status']
        # if (failCount > 5):
        #     print ("Too many failures")
        #     return 0;

    except Exception as e:
        print(str(e))
        return ""

    return 0


def sendTransaction(sid, i = 0, n = 10):
    try:

        while i < n:
            fileUpload(sid)
            i += 1

    except Exception as e:
        print(str(e))


if __name__=='__main__':
    now = time.time()
    ### TEST 1 ### 100 trans
    # trans = 3000
    c = 1
    # trans = 1
    # c = 1
    print("Account #", c, "Transactions", trans, "Trans/account", int(trans/c))

    for j in range(c):
        
        print("Account", j)
        t1 = threading.Thread(target = sendTransaction, args = ("a", int((j)*(trans/c)), int((j+1)*(trans/c))))
        t1.start()
        t1.join()
        time.sleep(0.05)
        # print(j, int((j)*(trans/c)), int((j+1)*(trans/c)))
    end = time.time()

    #print("Account #", c, "Transactions", trans, "Trans/account", int(trans/c))
    # print("Sono già qua")
    #performanceMonitoring(urlPro, "./otpBCPerformance/", metric1, metric2, metric3, metric4, now, end, stepMonitoringTime, "tryRequest-")
