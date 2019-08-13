#!/usr/bin/env bash

# This script shows how to build the Docker image and push it to ECR to
# be ready for use by SageMaker.

# The argument to this script is the image name. This will be used as the
# image on the local
# machine and combined with the account and region to form the
# repository name for ECR.

image=$1
profile=$2

if [ "$profile" == "" ]
then
    echo "Usage: $0 <aws-profile>"
    exit 1
fi

# Get the account number associated with the current IAM credentials
account=$(aws sts get-caller-identity --profile ${profile} --query Account --output text)

if [ $? -ne 0 ]
then
    exit 255
fi


# Get the region defined in the current configuration
# (default to us-east-1 if none defined)
region=$(aws configure get region)
region=${region:-us-east-1}


fullname="${account}.dkr.ecr.${region}.amazonaws.com/${image}:latest"

# If the repository doesn't exist in ECR, create it.

aws ecr describe-repositories --profile ${profile} --repository-names "${image}" > /dev/null 2>&1

if [ $? -ne 0 ]
then
    aws ecr create-repository --profile ${profile} --repository-name "${image}" > /dev/null
fi

# Get the login command from ECR and execute it directly
$(aws ecr get-login --profile ${profile} --region ${region} --no-include-email)

# Push Docker image to ECR with the full name.
docker tag ${image} ${fullname}

docker push ${fullname}
