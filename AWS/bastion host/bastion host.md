Here's a simple step-by-step guide to set up a Bastion Host in AWS as a beginner:

🧱 Prerequisites:
AWS Account

Basic knowledge of VPC, EC2, SSH

🔧 STEP 1: Create a VPC (if you don’t have one)
Go to VPC Dashboard > Create VPC

Select VPC only

Name: my-vpc

IPv4 CIDR: 10.0.0.0/16

Click Create VPC

🌐 STEP 2: Create Subnets
Public Subnet (for Bastion)
Name: public-subnet

AZ: Select one (e.g., us-east-1a)

CIDR: 10.0.1.0/24

Enable Auto-assign Public IPv4: ✅

Private Subnet (for internal EC2)
Name: private-subnet

AZ: Same as public

CIDR: 10.0.2.0/24

🛣️ STEP 3: Create and Attach Internet Gateway
Go to Internet Gateways > Create

Name: my-igw

Attach it to your VPC

🗺️ STEP 4: Route Tables
Public Route Table
Go to Route Tables > Create

Name: public-rt

Associate with my-vpc

Edit Routes:

Destination: 0.0.0.0/0

Target: Internet Gateway

Associate this table with public-subnet

Private Route Table
Optional (create and associate with private-subnet if needed)

💻 STEP 5: Launch Bastion Host EC2 in Public Subnet
Go to EC2 > Launch Instance

Name: bastion-host

AMI: Amazon Linux 2

Instance Type: t2.micro

Network: my-vpc

Subnet: public-subnet

Enable Auto-assign Public IP: ✅

Key pair:

Create or select existing

Save .pem file

Security Group:

Name: bastion-sg

Inbound rule:

Type: SSH

Source: My IP

🔒 STEP 6: Launch a Private EC2 in Private Subnet
Launch another EC2 instance

Name: private-instance

Subnet: private-subnet

Auto-assign Public IP: ❌

Use the same key pair as bastion

Click Add rule:

Type: SSH

Protocol: TCP

Port range: 22

Source: Select Custom, then paste the bastion's security group ID (e.g., sg-012345abcde67890)

🖥️ STEP 7: SSH into Private Instance via Bastion Host
From your terminal (Linux/macOS):

bash
Copy
Edit
chmod 400 my-key.pem
ssh -i my-key.pem ec2-user@<BASTION_PUBLIC_IP>


scp -i ashwanthramnv.pem ashwanthramnv.pem ec2-user@<public bastion ip>:~/

bash
Copy
Edit
ssh -i my-key.pem ec2-user@<PRIVATE_INSTANCE_PRIVATE_IP>
