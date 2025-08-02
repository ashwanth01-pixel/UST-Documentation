
# Bastion Host


## 🔧 STEP 1: Create a VPC
1. Go to **VPC Dashboard** → **Create VPC**
2. Select **VPC only**
3. Set the following:
   - **Name**: `my-vpc`
   - **IPv4 CIDR**: `10.0.0.0/16`
4. Click **Create VPC**

---

## 🌐 STEP 2: Create Subnets

### ✅ Public Subnet (For Bastion Host)
- **Name**: `public-subnet`
- **AZ**: `us-east-1a` (or any available zone)
- **CIDR**: `10.0.1.0/24`
- **Auto-assign Public IPv4**: Enabled ✅

### 🔐 Private Subnet (For Private EC2)
- **Name**: `private-subnet`
- **AZ**: Same as Public (e.g., `us-east-1a`)
- **CIDR**: `10.0.2.0/24`

---

## 🌉 STEP 3: Create and Attach Internet Gateway
1. Go to **Internet Gateways** → **Create Internet Gateway**
2. Name it: `my-igw`
3. Click **Create**
4. Select the newly created IGW → **Actions** → **Attach to VPC**
5. Choose `my-vpc` → **Attach**

---

## 🗺️ STEP 4: Create Route Tables

### 🚀 Public Route Table
1. Go to **Route Tables** → **Create**
2. Name it: `public-rt`
3. Associate with `my-vpc`
4. Click **Edit Routes**:
   - **Destination**: `0.0.0.0/0`
   - **Target**: Internet Gateway (`my-igw`)
5. **Associate Subnet**: `public-subnet`

---

## 💻 STEP 5: Launch Bastion Host EC2 (Public Subnet)
1. Go to **EC2 Dashboard** → **Launch Instance**
2. Configure:
   - **Name**: `bastion-host`
   - **AMI**: Amazon Linux 2
   - **Instance Type**: `t2.micro`
   - **Network**: `my-vpc`
   - **Subnet**: `public-subnet`
   - **Auto-assign Public IP**: Enabled ✅
   - **Key pair**: Create/select key (save `.pem` file securely)

3. Security Group:
   - **Name**: `bastion-sg`
   - Inbound Rules:
     - **Type**: SSH
     - **Source**: My IP (recommended)

---

## 🔒 STEP 6: Launch Private EC2 (Private Subnet)
1. Launch another EC2 instance:
   - **Name**: `private-instance`
   - **Subnet**: `private-subnet`
   - **Auto-assign Public IP**: ❌
   - **Key pair**: Same as bastion host

2. Security Group:
   - **Name**: `private-sg`
   - Inbound Rules:
     - **Type**: SSH
     - **Port**: 22
     - **Source**: Bastion SG ID (e.g., `sg-012345abcde67890`)

---

## 🖥️ STEP 7: SSH into Private Instance via Bastion Host

### 1️⃣ SSH into Bastion Host
```bash
chmod 400 ashwanthramnv.pem
ssh -i ashwanthramnv.pem ec2-user@<BASTION_PUBLIC_IP>
```

### 2️⃣ Copy `.pem` file into Bastion
```bash
scp -i ashwanthramnv.pem ashwanthramnv.pem ec2-user@<BASTION_PUBLIC_IP>:~/
```

### 3️⃣ SSH from Bastion to Private EC2
```bash
ssh -i ashwanthramnv.pem ec2-user@<PRIVATE_INSTANCE_PRIVATE_IP>
```

---