# AWS VPC

## Step 1: Create VPC

Go to **VPC > Your VPCs > Create VPC**

- **Name**: `my-vpc`
- **CIDR block**: `10.0.0.0/16`
- Select **"VPC Only"** option
- Click **Create VPC**

---

## Step 2: Create 4 Subnets

Go to **Subnets > Create subnet**

Create four subnets, all inside `my-vpc`:

| Name              | AZ         | CIDR Block     |
|-------------------|------------|----------------|
| public-subnet-1a  | us-east-1a | 10.0.1.0/24    |
| private-subnet-1a | us-east-1a | 10.0.2.0/24    |
| public-subnet-1b  | us-east-1b | 10.0.3.0/24    |
| private-subnet-1b | us-east-1b | 10.0.4.0/24    |

---

## Step 3: Create Internet Gateway

Go to **Internet Gateways > Create IGW**

- **Name**: `my-igw`
- Click **Create**, then **Attach to VPC** → choose `my-vpc`

---

## Step 4: Create Route Tables

Go to **Route Tables > Create route table** and create the following:

| Name         | Use For               |
|--------------|-----------------------|
| public-rt    | Both public subnets   |
| private-rt-1a| private-subnet-1a     |
| private-rt-1b| private-subnet-1b     |

Now edit `public-rt`:

- Go to **Routes → Edit → Add route**:
  - **Destination**: `0.0.0.0/0`
  - **Target**: Internet Gateway (`my-igw`)

Attach this route table to:

- `public-subnet-1a`
- `public-subnet-1b`

---

## Step 5: Attach Private Route Tables

- Attach `private-rt-1a` to `private-subnet-1a`
- Attach `private-rt-1b` to `private-subnet-1b`

### To Attach a Route Table (e.g., `public-rt`) to `public-subnet-1a` and `public-subnet-1b`, follow these steps:

1. Go to **VPC Dashboard**
2. Open **Route Tables** on the left pane.
3. Select `public-rt`
4. Click on the **Subnet Associations** tab.
5. Click **Edit subnet associations**.
6. Check the boxes next to:
   - `public-subnet-1a`
   - `public-subnet-1b`
7. Click **Save associations**

> _(No route to IGW — it stays private)_

---

## Step 6: Create VPC Endpoint (S3 Access from Private Subnets)

Go to **VPC Dashboard → Endpoints**

Click **“Create Endpoint”**

### 📋 Configuration Details

| Field         | Value/Action                                                                 |
|---------------|-------------------------------------------------------------------------------|
| Service Name  | Type `S3` → Select service that says `com.amazonaws.<region>.s3` (Type: Gateway) |
| VPC           | Select your VPC (e.g., `my-vpc`)                                              |
| Service Type  | Gateway                                                                      |
| Route Tables  | Select both private route tables:<br> `private-rt-1a` and `private-rt-1b`     |
| Policy        | Leave as “Full Access” (default)                                              |

> _No need to select subnets for Gateway endpoints like S3 (only for interface endpoints)._

Click **“Create Endpoint”**

---

## ✅ COMPLETED!!



- 2 public and 2 private subnets in two AZs
- Internet access for public subnets
- No internet access for private subnets
- But private subnets can access **S3**