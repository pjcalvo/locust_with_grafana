from dynaconf import settings
# from libs.influxdb_writter import expose_metrics
from locust import HttpLocust, TaskSet, task, between, constant

# # set influxdb writter
# expose_metrics(
#     user=settings.INFLUXDB_USER,
#     pwd=settings.INFLUXDB_PASS,
#     influx_host=settings.INFLUXDB_HOST,
#     influx_port=settings.INFLUXDB_PORT,
#     database=settings.PROJECT_ID)

class MainTest(TaskSet):

   @task
   def home(self):
      self.client.get('/')

   @task
   def en(self):
      self.client.get('/content/lionbridge/language-masters/en.html')

   @task
   def svg(self):
      self.client.get('/etc.clientlibs/lionbridge/clientlibs/clientlib-site/resources/images/hamburger.white.svg')

   @task
   def who_we_are(self):
      self.client.get('/content/lionbridge/language-masters/en/who-we-are.html')

   @task
   def svg2(self):
      self.client.get('experience-fragments/lionbridge/us/en/site/header/master/_jcr_content/root/responsivegrid/container_1103531382/image.coreimg.svg/1589340119750/logo.light-%281%29.svg')

   @task
   def svg3(self):
      self.client.get('/etc.clientlibs/lionbridge/clientlibs/clientlib-site/resources/images/social/linkedin-icon.svg')
           
class TestPlan(HttpLocust):
    task_set = MainTest
    wait_time = constant(0) # wait between tasks
    host = settings.HOST