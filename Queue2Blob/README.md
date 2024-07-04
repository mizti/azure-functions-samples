# Architecture

* Input: Queue Storage
* Output: Blob Storage

# Usage

## Prep

1. Install Azure Functions Core Tool

(below example is for Ubuntu)
```bash
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-$(lsb_release -cs)-prod $(lsb_release -cs) main" > /etc/apt/sources.list.d/dotnetdev.list'
sudo apt-get update
sudo apt-get install azure-functions-core-tools-4
```

See:
https://learn.microsoft.com/ja-jp/azure/azure-functions/functions-run-local?tabs=linux%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python

## Local Run

1. set connection string
```bash
export AzureWebJobsStorage="DefaultEndpointsProtocol=https;AccountName=youraccountname;AccountKey=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX==;EndpointSuffix=core.windows.net"
```

2. Run
```bash
func start
```

## Run on Azure

1. Create Azure Functions instance
Plan: Flex Consumption
Name: (Your FunctionAppName)
Region: East US (or your region)
Runtime stack: Python
Version: 3.11
Instance size: 2048MB
Storage: (Select Queue Storage or Create new)
Diagnostic Settings: Don't configure diagnostic settings now

2. Application settings

If you choose existing storage, Environment variable 'AzureWebJobsStorage' is automatically set.

If you need to connect another storage account, 
Settings > Environment variables > App settings
Set connection string as 'AzureWebJobsStorage'.

3. Deploy & Run

```bash
func azure functionapp publish <FunctionAppName>
```
