from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.post('/user/authorixation', json={
            "email": "tanyamalahova1919@mail.ru",
            "password": "24090181919tanyatanya"})
