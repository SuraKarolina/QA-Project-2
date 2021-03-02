# QA-Project-2

# Zodiac signs and friendship match generator

### Resources:
GitHub repository: https://github.com/SuraKarolina/QA-Project-2<br />
Asana board: https://app.asana.com/0/1199910481527550/board

### Content
1.[Brief](#brief)<br />
2.[Software Design](#software-design)<br />
3.[Programming and Software Development](#programming-and-software-development)<br />
4.[System Integration and Build](#system-integration-and-build)<br />
5.[Release and Deployment](#release-and-deployment)<br />
6.[Risk Assessment](#risk-assessment)<br />
7.[Future Improvements](#future-improvements)<br />
8.[Contributors and Acknowledgement](#contributors-and-acknowledgement)<br />
***

## Brief
The requirement of this project was to create simple web application composed of four services that work together. First server work as a core service, it communicate with other services and store data in database. Second and third services are responsible for generation of random 'object'. Service 4 also generates random 'object' but this should be based on service 2 and 3 results. There are following additional requirements:
* An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
* An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
* If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
* The project must follow the Service-oriented architecture that has been asked for.
* The project must be deployed using containerisation and an orchestration tool.
* As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
* The project must make use of a reverse proxy to make your application accessible to the user.

***
## Software Design

### Approach of the project

My approach to the project was to create two versions of the application. The first version would be configured, tested, builed and deployed with Jenkins pipline. The system version control would be connected with Jenkins via webhook in order to update repository and replace first version of the application with the second version.  

### Minimum Viable Product 

The Minimum Viable Prodact is presented in MosCow prioritization diagram: 
![](https://github.com/SuraKarolina/images/blob/main/images/moscow.png)

### Project tracking

For project tracking and management Asana board was used. 
![](https://github.com/SuraKarolina/images/blob/main/images/asana2.png)


### Services relationship

Services work together using GET and POST methods. The diagram shows relationship between each service: 

![](https://github.com/SuraKarolina/images/blob/main/images/services.png)


### ER table



***
## System Integration and Build

### Test coverage 
![](https://github.com/SuraKarolina/images/blob/main/images/tests.png)
### CI pipline

***
## Release and Deployment

***
## Risk Assessment


***
## Future Improvements

***
## Contributors and Acknowledgement

>>>>>>> a951990426dd835ac474b6c0cce3d3ea12e962c4
