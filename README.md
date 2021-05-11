Overview
========

Simple python reference application to massage and forward a generic HSDP  
Metrics webhook alert to a slack webhook.  The payload needs to be formatted  
a bit before it can be forwarded to slack to reduce the size and make it  
more readable in slack.  The endpoint that the payload needs to be sent to is  
currently just a GUID.  It should be changed to a new unique GUID if used  
for anything other than a demo.  


Building with docker
--------------------

Standard docker build, should build fine from the Dockerfile with no modifications.

```
docker build . -t <repo>/<image>:<tag>  
docker push <repo>/<image>:<tag>
```  


The vars.yml file
-----------------

All vars needed for deploying to Cloud Foundry should be stored in vars.yml.  
This should be the only file you need to edit before deploying the appication.  


| Variable        | Description                                                               |
|-----------------|---------------------------------------------------------------------------|
| instances       | The number of application instances that should be deployed               |
| name            | The hostname for the application.                                         |
| docker_image    | The docker image to use when deploying the application as a docker image. |
| external_domain | The domain name to use for the application route.                         |
| slack_webhook   | The slack webhook to forward the alert to.                                |


Deploying as a docker app to cf
-------------------------------

Update the vars.yml file with your deployment specific values.  
`cf push -f ./manifest-docker.yml --vars-file ./vars.yml`

Note: be sure to export CF_DOCKER_PASSWORD environment variable.
