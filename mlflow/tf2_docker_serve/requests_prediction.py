# Serving the Models as a Docker Image
# 1. mlflow run .
# 2. mlflow models build-docker -m "./mlruns/0/<run-id>/artifacts/model" -n "tf_serve"
# 3. docker run -p 5001:8080 "tf_serve"

# working REST api command
# curl -X POST -H "Content-Type:application/json; format=pandas-split" --data '{"columns":["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"],"data":[[5.1, 3.3, 1.7, 0.5], [5.9, 3.0, 4.2, 1.5], [6.9, 3.1, 5.4, 2.1]]}' http://127.0.0.1:5001/invocations

import requests

headers = {
    'Content-Type': 'application/json; format=pandas-split',
}

data = '{"columns":["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"],"data":[[5.1, 3.3, 1.7, 0.5], [5.9, 3.0, 4.2, 1.5], [6.9, 3.1, 5.4, 2.1]]}'

response = requests.post('http://127.0.0.1:5001/invocations', headers=headers, data=data)

resp_json = response.json()

print(resp_json[0])
# {'all_class_ids': [0, 1, 2], 'all_classes': ['MA==\n', 'MQ==\n', 'Mg==\n'], 'class_ids': 1, 'classes': 'MQ==\n', \
# 'logits': [0.2719880938529968, 0.8638693690299988, -0.8623905181884766], 'probabilities': [0.31959015130996704, 0.577622652053833, 0.10278719663619995]}