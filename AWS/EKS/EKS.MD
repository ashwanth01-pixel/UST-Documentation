step 1 --> Create EKS Cluster Role

    create Role

    Select EKS → EKS - Cluster

    Attach policy: AmazonEKSClusterPolicy

    Name: ashcluster

step 2 ---> Create Node Group Role

    Create role

    Select EC2

    Attach policies: AmazonEKSWorkerNodePolicy, AmazonEKS_CNI_Policy, AmazonEC2ContainerRegistryReadOnly
    
    Name: ashworkernode

step3 --> install ekctl

    curl --silent --location "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_Linux_amd64.tar.gz" | tar xz -C /tmp
    
    sudo mv /tmp/eksctl /usr/local/bin

step 4 ----> create cluster

    eksctl create cluster \
    --name ashcluster \
    --region us-east-1 \
    --nodegroup-name vilas-workers \
    --node-type t3a.medium \
    --nodes 2 \
    --nodes-min 2 \
    --nodes-max 2 \
    --managed


    aws eks update-kubeconfig --name ashcluster --region us-east-1

step 5

    kubectl get nodes

    created simple niginx file - ash-nginx.yaml with loadbalancer service

    cat <<EOF > ash-nginx.yaml
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
EOF


    kubectl apply -f ash-nginx.yaml

    kubectl get pods

    kubectl get svc

step 6

    http://<external-ip>


DELETING

    kubectl delete deployment ash-nginx-deployment

    kubectl delete service ash-nginx-service

    eksctl delete cluster --name ashcluster --region us-east-1

    optional (cleanup):

    kubectl config delete-context arn:aws:eks:us-east-1:267092042432:cluster/vilasekscluster1
kubectl config unset users.arn:aws:eks:us-east-1:267092042432:cluster/vilasekscluster1
kubectl config unset clusters.arn:aws:eks:us-east-1:267092042432:cluster/vilasekscluster1




