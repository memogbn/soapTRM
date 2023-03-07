from zeep import Client
import time

client = Client('https://www.superfinanciera.gov.co/SuperfinancieraWebServiceTRM/TCRMServicesWebService/TCRMServicesWebService?WSDL')

date = time.strftime('%Y-%m-%d')
date = '2023-02-05'
print(date)
try:
    result = client.service.queryTCRM(date)
except Exception as e:
    print(str(e))
print(result)
#assert result == 62.137

