\# Task 7: AWS EC2 Deployment



\## Objective



The objective of this task was to understand AWS EC2, configure an EC2 instance, connect to it using SSH, set up the required development environment, and deploy/run the Twenty CRM application using Docker.



\## 1. EC2 Configuration



The EC2 instance was launched using the AWS Management Console.



\### Configuration Used



\* \*\*AMI:\*\* Amazon Linux 2023

\* \*\*Instance Type:\*\* Selected according to the task requirements

\* \*\*Key Pair:\*\* `karthikeyan-key.pem`

\* \*\*Operating System:\*\* Amazon Linux 2023

\* \*\*Security Group:\*\* Configured to allow SSH access on TCP port 22 and application access as required.

\* \*\*Public IP:\*\* `100.31.116.38`



\## 2. Connecting to EC2



The instance was accessed from Windows PowerShell using SSH.



```bash

ssh -i "$HOME\\Downloads\\karthikeyan-key.pem" ec2-user@100.31.116.38

```



After connecting, the EC2 shell showed:



```text

\[ec2-user@ip-172-31-23-76 \~]$

```



The logged-in user was verified using:



```bash

whoami

```



Output:



```text

ec2-user

```



\## 3. Testing SSH Connectivity



From Windows PowerShell, SSH connectivity was verified using:



```powershell

Test-NetConnection 100.31.116.38 -Port 22

```



The test confirmed that TCP port 22 was reachable.



\## 4. Updating the EC2 Instance



The Amazon Linux system packages were updated using:



```bash

sudo dnf update -y

```



\## 5. Installing Docker



Docker was installed using:



```bash

sudo dnf install -y docker

```



Docker was started using:



```bash

sudo systemctl start docker

```



The EC2 user was added to the Docker group:



```bash

sudo usermod -a -G docker ec2-user

```



After logging out and reconnecting, Docker was verified using:



```bash

docker ps

```



\## 6. Installing Git



Git was installed using:



```bash

sudo dnf install -y git

```



Git version was verified using:



```bash

git --version

```



\## 7. Cloning the Project



The project repository was cloned from GitHub:



```bash

git clone https://github.com/Karthikeyandk/devops-crm-project.git

```



The project directory was opened using:



```bash

cd \~/devops-crm-project

```



The remote repository was verified using:



```bash

git remote -v

```



\## 8. Installing Node.js



The project specifies its Node.js version through `.nvmrc`.



The `.nvmrc` file specifies:



```text

24.5.0

```



NVM was installed and Node.js was installed using:



```bash

nvm install

```



The installed version was verified using:



```bash

node --version

```



Node.js version:



```text

v24.5.0

```



\## 9. Installing and Configuring Yarn



Corepack was enabled using:



```bash

corepack enable

```



Yarn was then configured for the project.



The Yarn version used was:



```text

4.13.0

```



\## 10. Installing Project Dependencies



Project dependencies were installed using:



```bash

yarn install

```



The installation completed successfully.



There were peer dependency warnings, but there were no fatal errors and the installation completed successfully.



\## 11. Twenty CRM Docker Setup



The Twenty CLI was checked using:



```bash

yarn twenty --help

```



The available Docker commands included:



```text

docker:start

docker:stop

docker:logs

docker:status

```



Before starting Twenty, the Docker status was checked:



```bash

yarn twenty docker:status

```



The initial status was:



```text

Status: not created

```



Twenty CRM was then started using:



```bash

yarn twenty docker:start

```



The command performed database initialization, migrations, cache flushing and workspace seeding.



The startup process reported:



```text

PostgreSQL... Done

Database setup and migrations... Done

Flushing cache... Done

Database ready... Done

```



The Twenty server and worker services were subsequently started.



\## 12. Checking Twenty Logs



Twenty logs were checked using:



```bash

yarn twenty docker:logs

```



During startup, some PostgreSQL warnings were observed and the initial cron registration reported a failure while the application was becoming ready.



The logs later showed that the following services started:



```text

twenty-server: successfully started

twenty-worker: successfully started

```



The logs were used to understand the startup process and diagnose the health-check delay.



\## 13. Issues Faced and Solutions



\### Issue 1: Git command not available



Git was initially not available on the EC2 instance.



\*\*Solution:\*\*



```bash

sudo dnf install -y git

```



\### Issue 2: Node.js version requirement



The project required the Node.js version specified in `.nvmrc`.



\*\*Solution:\*\*



NVM was installed and the project version was installed using:



```bash

nvm install

```



This installed Node.js `v24.5.0`.



\### Issue 3: Twenty Docker startup took longer than expected



The `yarn twenty docker:start` command took time because it had to pull the Docker image and perform PostgreSQL initialization, migrations, cache operations and workspace seeding.



The command initially reported:



```text

Twenty server did not become healthy in time.

```



\*\*Solution:\*\*



The Docker logs were inspected using:



```bash

yarn twenty docker:logs

```



The logs showed the database initialization and Twenty server/worker startup process.



\### Issue 4: Running Yarn outside the project directory



Running the Twenty command from `/home/ec2-user` resulted in a package.json error.



\*\*Solution:\*\*



The correct project directory was entered first:



```bash

cd \~/devops-crm-project

```



Then the Twenty command was executed.



\## 14. EC2 Concepts Learned



\### AMI



An Amazon Machine Image (AMI) provides the operating system and initial software configuration used to launch an EC2 instance.



\### Instance Type



The instance type determines the available CPU, memory, networking and other compute resources.



\### Key Pair



The EC2 key pair is used for secure SSH authentication. The private `.pem` key is required to connect to the instance.



\### Security Group



A security group acts as a virtual firewall for the EC2 instance. It controls inbound and outbound network traffic.



\### Public IP



The public IP allows the EC2 instance to be reached from the internet when the appropriate network and security-group rules are configured.



\### SSH



SSH provides secure remote terminal access to the EC2 Linux instance.



\### Docker



Docker was used to run the Twenty CRM application and its supporting services in containers.



\## 15. Verification



The following components were successfully configured and verified:



\* EC2 instance launched

\* SSH connectivity established

\* Amazon Linux 2023 running

\* Docker installed and running

\* Git installed

\* Project cloned from GitHub

\* Node.js `v24.5.0` installed

\* Yarn `4.13.0` configured

\* Project dependencies installed

\* Twenty Docker environment initialized

\* Twenty server and worker services started



\## 16. Cleanup



After completing the required testing, the Twenty Docker environment should be stopped:



```bash

yarn twenty docker:stop

```



The EC2 instance should then be stopped from the AWS Management Console when it is no longer required.



The instance should only be terminated if the task requires termination and all documentation, screenshots and evidence have been collected.



\## 17. Loom Video



A Loom video will be recorded explaining:



\* Task objective

\* EC2 configuration

\* AMI and instance type

\* Key pair

\* Security group

\* SSH connection

\* Docker setup

\* Git setup

\* Node.js and Yarn setup

\* Project cloning

\* Twenty CRM deployment

\* Issues faced and their solutions

\* Verification

\* EC2 concepts learned

\* Cleanup process



\*\*Loom Video:\*\* TODO



