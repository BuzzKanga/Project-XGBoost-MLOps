# Monitoring

Evidently AI is used to monitor the model. In this case I was able to obtain modlel metrics whcih could be used as a baseline for comarison to future results which would enable model drift to be detected.

[Docker-compose](monitoring/docker-compose.yml) is used to deploy multiple containerseach containing a component of the monitoring ecosystem:

- Postgress DB

- Adminer DB

- Grafana (reports dashboards)

The [monitoring](monitoring/monitoring.ipynb) notebook is used to run Evidently and set-up the metrics to be reported on.

Sample report from Evidently AI is shown below:





