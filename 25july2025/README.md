# Kubernetes Single Node Setup with Weave CNI and NGINX Deployment

This guide helps you set up a single-node Kubernetes cluster using `kubeadm`, install the Weave CNI for pod networking, and deploy an NGINX pod for testing.

## 🧰 Prerequisites

- A Linux machine or VM with root access
- Docker installed and running
- `kubeadm`, `kubectl`, and `kubelet` installed
- Swap disabled (`swapoff -a`)
- Proper `sysctl` settings for Kubernetes networking

---

## 🚀 Setup Steps

### 1. Initialize Kubernetes Cluster

```bash
kubeadm init
```

> This sets up the Kubernetes control plane.

---

### 2. Check Node Status

```bash
kubectl get node
```

> The node will initially be in `NotReady` status due to missing CNI.

---

### 3. Install Weave CNI Plugin

```bash
kubectl apply -f https://github.com/weaveworks/weave/releases/download/v2.8.1/weave-daemonset-k8s.yaml
```

> This installs the Weave CNI plugin to enable pod networking.

---

### 4. Monitor System Pods

```bash
watch -n 1 kubectl get po -n kube-system
```

> Wait until all pods are in `Running` state (e.g., `1/1` or `2/2`).

---

### 5. Check for Control Plane Taints

```bash
kubectl describe node | grep -i taint
```

> Find and copy the taint to remove it for scheduling pods.

---

### 6. Get Node Name

```bash
kubectl get node
```

> Note the node name for the next step.

---

### 7. Remove Control-Plane Taint

```bash
kubectl taint node <node-name> node-role.kubernetes.io/control-plane:NoSchedule-
```

> This allows the control plane node to schedule pods.

---

### 8. Deploy NGINX Pod

```bash
kubectl run nginx --image=nginx
```

> Launches an NGINX container in a pod.

---

### 9. Confirm Pod Status

```bash
kubectl get po
```

---

### 10. Get Pod IP Address

```bash
kubectl get po -o wide
```

> Note the internal pod IP address from the output.

---

### 11. Test NGINX Accessibility

```bash
curl <pod-ip>
```

> You should see the NGINX welcome page in the response.

---

## ✅ Expected Output

You should see something like this in your terminal:

```html
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
...
</html>
```

---

## 📎 Notes

- This setup is for **single-node testing/demo purposes only**.
- Do **not use in production** without proper HA, networking, and security setup.
