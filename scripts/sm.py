from dynaconf import settings
from locust import HttpLocust, TaskSet, task, between
from locust_influx import expose_metrics

# set influxdb writter
expose_metrics(
    user=settings.INFLUXDB_USER,
    pwd=settings.INFLUXDB_PASS,
    influx_host=settings.INFLUXDB_HOST,
    influx_port=settings.INFLUXDB_PORT,
    database=settings.PROJECT_ID)


class WebsiteTasks(TaskSet):   
    @task
    def index(self):
        self.client.get("/")
        
    @task
    def contact(self):
        self.client.get("/contact")

    @task
    def pci(self):
        self.client.get("/pci")

    @task
    def pci_small_business(self):
        self.client.get("/pci-small-business")

    @task
    def hipaa(self):
        self.client.get("/hipaa")

    # fail requests porpusely
    @task
    def cause_fail_get_request(self):
        self.client.get(f'/invalid-path')
    

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(5, 15)
    host = settings.HOST