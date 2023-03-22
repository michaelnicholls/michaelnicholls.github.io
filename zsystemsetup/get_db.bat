@echo off
rem cf login -a https://api.cf.ap10.hana.ondemand.com -u i016416@gmail.com
cf service main --guid > guid.txt

for /f "tokens=*" %%g in ( guid.txt ) do (
cf curl /v2/service_instances/%%g/parameters |find "Stopped"

)
