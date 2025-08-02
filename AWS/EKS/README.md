# Amazon EKS Cluster Setup Guide

## Step 1 → Create EKS Cluster Role

- Create Role
- Select **EKS → EKS - Cluster**
- Attach policy: `AmazonEKSClusterPolicy`
- **Name**: `ashcluster`

---

## Step 2 → Create Node Group Role

- Create Role
- Select **EC2**
- Attach policies:
  - `AmazonEKSWorkerNodePolicy`
  - `AmazonEKS_CNI_Policy`
  - `AmazonEC2ContainerRegistryReadOnly`
- **Name**: `ashworkernode`

---

## Step 3 → Install `eksctl`

```bash
curl --silent --location "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_Linux_amd64.tar.gz" | tar xz -C /tmp

sudo mv /tmp/eksctl /usr/local/bin
```

---

## Step 4 → Create Cluster

```bash
eksctl create cluster \
--name ashcluster \
--region us-east-1 \
--nodegroup-name vilas-workers \
--node-type t3a.medium \
--nodes 2 \
--nodes-min 2 \
--nodes-max 2 \
--managed
```

```bash
aws eks update-kubeconfig --name ashcluster --region us-east-1
```

---

## Step 5 → Deploy NGINX on EKS

Check nodes:

```bash
kubectl get nodes
```

Create `ash-nginx.yaml` file with the following content:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ash-nginx-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: ash-nginx
  template:
    metadata:
      labels:
        app: ash-nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: ash-nginx-service
spec:
  selector:
    app: ash-nginx
  type: LoadBalancer
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
```

Apply and verify:

```bash
kubectl apply -f ash-nginx.yaml

kubectl get pods

kubectl get svc
```

Access using:

```
http://<external-ip>
```

---

## Step 6 → Deleting Resources

```bash
kubectl delete deployment ash-nginx-deployment

kubectl delete service ash-nginx-service

eksctl delete cluster --name ashcluster --region us-east-1
```

### Optional Cleanup

```bash
kubectl config delete-context arn:aws:eks:us-east-1:267092042432:cluster/vilasekscluster1
kubectl config unset users.arn:aws:eks:us-east-1:267092042432:cluster/vilasekscluster1
kubectl config unset clusters.arn:aws:eks:us-east-1:267092042432:cluster/vilasekscluster1
```