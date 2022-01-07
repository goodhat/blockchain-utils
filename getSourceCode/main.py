import json
import requests
import os

ETHERSCAN_APIKEY="YOUR_API_KEY"
ETHERSCAN_ENDPOINT="https://api.etherscan.io/api"

def main():
    print("This tool will download verified source code of smart contracts from etherscan.")
    target_address=input("Please enter the address:")

    params = {
        "module": "contract",
        "action": "getsourcecode",
        "address": target_address,
        "apikey": ETHERSCAN_APIKEY
    }

    r = requests.get(ETHERSCAN_ENDPOINT, params=params)
    data = json.loads(r.text)["result"][0]
    contract_name = data["ContractName"]
    source_code = json.loads(data["SourceCode"][1:-1])["sources"]
    
    os.mkdir(contract_name)
    print(f"Create directory {contract_name}")
    for key, value in source_code.items():
        filename = key.split('/')[-1]
        with open(os.path.join(contract_name, filename), 'w') as file:
            print(f"Writing {filename} ...")
            file.write(value["content"])
            
    print("Done!")
    return

main()