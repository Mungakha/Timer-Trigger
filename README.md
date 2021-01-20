# Azure Timer-Trigger Write Message to Queue Storage
Timer trigger lets you run a function on a schedule.
The timer trigger bindings in which scheduled time is defined are described in the the function.json file. For instance, this timer trigger function is scheduled to run  11 05 UTC time.
The actual Python function that uses the binding described in the function.json file is contained in the init.py file
When this function runs at the scheduled time, it deposits the message "EDNUpdateProcessRunning" in a queue named "outqueue1" which is contained in Azure storage stored in the parameter conn_str.
The intention is that when "outqueue1" receives the new message it triggers https://github.com/Mungakha/Serverless_GeoAnalytics_Queue-Trigger1 

