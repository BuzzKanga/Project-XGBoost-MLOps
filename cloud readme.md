# Cloud infrastructure

# Setup steps

1. Log on to AWS.
2. Navigate to CloudFormation.
3. Select Designer.
4. Import CloudFormation template [create-ec2-instance.yaml](setup/create-ec2-instance.yaml) using `File>Open` function.
5. Click the `Create Stack` button.
6. Clcik through all the screens till you get to `Submit` button.
7. Click `Submit button`and wait for stack to be created.
8. Run [makefile](setup/makefile) on AWS