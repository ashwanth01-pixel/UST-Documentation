kubeadm init
kubectl get node
kubectl apply -f https://github.com/weaveworks/weave/releases/download/v2.8.1/weave-daemonset-k8s.yaml
watch -n 1 kubectl get po -n kube-system
kubectl describe node | grep -i taint
kubectl get node
kubectl taint node <node-name> node-role.kubernetes.io/control-plane:NoSchedule-
kubectl run nginx --image=nginx
kubectl get po
kubectl get po -o wide
curl <pod-ip>
