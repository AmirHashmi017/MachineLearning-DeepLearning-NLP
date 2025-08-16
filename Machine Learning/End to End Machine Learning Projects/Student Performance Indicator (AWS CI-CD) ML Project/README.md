## AWS CI/CD ML Project
### Steps:
1. Docker Build checked
2. Github Workflow
3. IAM User In AWS
4. Make ECR Repository
5. Docker Setup In EC2 
### Commands to be Executed
#### Optional

sudo apt-get update -y

sudo apt-get upgrade

#### required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

### Configure EC2 as self-hosted runner:
### Setup github secrets:
1. AWS_ACCESS_KEY_ID=

2. AWS_SECRET_ACCESS_KEY=

3. AWS_REGION = us-east-1

4. AWS_ECR_LOGIN_URI = demo>> 566373416292.dkr.ecr.ap-south-1.amazonaws.com

5. ECR_REPOSITORY_NAME = simple-app
