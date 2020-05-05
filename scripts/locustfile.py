import string
import random
from dynaconf import settings
from locust import HttpLocust, TaskSet, task, between
from libs.influxdb_writter import expose_metrics

expose_metrics(
    user=settings.INFLUXDB_USER,
    pwd=settings.INFLUXDB_PASS,
    influx_host=settings.INFLUXDB_HOST,
    influx_port=settings.INFLUXDB_PORT,
    database=settings.PROJECT_ID)

class WebsiteTasks(TaskSet):

    @task
    def home(self):
        self.client.get("/")
        
    @task
    def gdpr_defense(self):
        self.client.get("/gdpr-defense")   
        
    @task
    def hipaa_policies(self):
        self.client.get("/hipaa-policies")   
    
    @task
    def guided_hipaa(self):
        self.client.get("/guided-hipaa")   
    
    @task
    def internal_network(self):
        self.client.get("/internal-network-scan")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(0,0) # wait between tasks
    host = settings.HOST