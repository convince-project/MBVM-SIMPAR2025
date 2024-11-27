This is the repository for the Model-based Verification and Monitoring for Safe and Responsive Reactive Robots SIMPAR 2025 paper

#### overview
The repo has a docker with the dockerfiles contained in the folder `docker/`

all the properties and the monitor are inside the folder `monitoring/`

all the code for the execution of BT and skills is inside the folder `code/`

all the models for the SCAN execution are inside the folders `model-high-level/`, `model_scxml/` and `specifications/`

#### prerequisites

if you want to execute the docker you just need to install docker compose as explained [here](https://docs.docker.com/compose/install/)

#### execution
##### monitoring
to execute the monitoring:

```
cd docker
docker compose build
docker compose up ros2monitorProp1
```
if you want to change the properties you just need to change the property number on the docker compose up

to close everything run `docker compose down`

if you want to modify the property, edit the property in the folder monitoring and then run from the root folder 
```
docker build  -f "docker/Dockerfile.custom_prop1" -t ste93/mbvm:simpar2025 .
```

as before if the property is another one you only need to change the number of the property

##### SCAN

to execute SCAN:

```

```
