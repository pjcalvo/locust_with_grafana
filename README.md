
## Execution
### linear
```bash
locust -f locust.py --no-web -c 1000 -r 2 --run-time 30m --host https://www.securitymetrics.com
```

### escalonated
```bash
locust -f scripts/sm.py --no-web -c 1000 -r 1 --run-time 30m --step-load --step-clients 10 --step-time 2m --host https://securitymetrics-prod.adobemsbasic.com
```


## Influx DB
```bash
curl -i -XPOST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE sm_prod"
```

```bash
curl -i -XPOST http://localhost:8086/query --data-urlencode "q=DROP DATABASE sm_prod"
```

