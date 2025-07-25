# 📘 Kubernetes Commands Documentation

## Initialization and Cluster Setup
- **`kubeadm init`**  
  Initializes the Kubernetes control-plane node.  
  _Use this to start setting up your Kubernetes cluster._

## Node and Pod Management
- **`kubectl get node`**  
  Lists all nodes in the cluster.  
  _Helps verify node registration and status._

- **`kubectl get po`**  
  Lists all pods in the current namespace.  
  _Checks if pods are running or pending._

- **`kubectl get po -o wide`**  
  Shows pods with extended details (node, IP, etc.).  
  _Useful for debugging or networking checks._

## Networking
- **`kubectl apply -f https://github.com/weaveworks/weave/releases/download/v2.8.1/weave-daemonset-k8s.yaml`**  
  Applies Weave Net as the CNI (Container Network Interface) plugin.  
  _Used to set up networking between pods._

- **`curl <pod-ip>`**  
  Sends a request to the pod’s IP to check if it's serving correctly.  
  _Used to verify if a pod is accessible._

## Monitoring and Debugging
- **`watch -n 1 kubectl get po -n kube-system`**  
  Continuously monitors pod statuses in the kube-system namespace every 1 second.  
  _Used to watch system pods in real time._

- **`kubectl describe node | grep -i taint`**  
  Shows taint info of nodes.  
  _Helps check if the node is preventing pod scheduling._

## Taint Management
- **`kubectl taint node <node-name> node-role.kubernetes.io/control-plane:NoSchedule-`**  
  Removes the NoSchedule taint from control-plane nodes.  
  _Allows pods to be scheduled on the master node._

## Application Deployment
- **`kubectl run nginx --image=nginx`**  
  Launches an Nginx pod using the official Nginx image.  
  _Used to test pod deployment._
