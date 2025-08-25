Of course! Here are your handwritten notes transcribed and formatted into a readme.md file.

Kubernetes Networking Notes: Network Policies, Ingress & Egress
This document contains notes on Kubernetes networking concepts, focusing on Network Policies, Ingress, and Egress traffic control.

1. Network Policies
Network Policies are Kubernetes objects that control the traffic flow between pods. They act as a firewall at the pod level.

Default Behavior: In Kubernetes, all pods can talk to each other by default.

Function: A Network Policy defines rules for traffic flow between pods. It is essentially a firewall applied to a pod, operating at Layer 3/4 (IP address and port).

Control Scope: It can control:

Ingress: Traffic coming into a pod.

Egress: Traffic leaving a pod.

Application: Network policies can be applied to pods via label selectors. They are dynamic and affect pod creation or deletion.

Why are Network Policies needed?
Restrict Unauthorized Access:

Deny-all traffic from specific pod namespaces, protocols, or IPs.

Prevents accidental or malicious access to sensitive pods.

Multi-tenant Environments:

In a multi-tenant cluster, Network Policies ensure that pods in one namespace (belonging to one team) cannot communicate with pods in other namespaces or teams, providing isolation.

2. Ingress & Egress
Ingress
Ingress refers to incoming traffic entering the Kubernetes cluster from an external source.

It acts as a gateway for external traffic to reach internal services.

An Ingress resource is a Kubernetes object that defines a collection of rules for routing this incoming traffic.

Routing can be based on hostname or request path.

An Ingress Controller functions like a receptionist, reading the Ingress resource rules and directing traffic to the correct service.

It supports features like:

SSL/TLS termination

Name-based virtual hosting

Egress
Egress refers to outgoing traffic leaving the cluster from a pod.

This is the traffic flow from pods to external endpoints, such as databases, APIs, or other services outside the cluster.

By default, pods are isolated from the external network in some configurations, and their outgoing traffic must be explicitly allowed.

Network Policies are used to define rules for outgoing (egress) traffic.

Egress rules specify which external endpoints pods are allowed to access.

Securing egress traffic helps prevent unauthorized communication and data exfiltration.

Traffic Flow Diagram
[ Pod ] --> [ CNI Plugin (e.g., Calico) enforces Network Policy (Egress Rule) ] --> [ Node Network ] --> [ External Network / Internet ]
3. Internal Workings of Network Policies
Kubernetes itself doesn't enforce network policies. It relies on a CNI (Container Network Interface) plugin.

CNI Plugins: Kubernetes uses CNI plugins like Calico, Cilium, or Weave to implement networking and enforce policies.

The enforcement process works as follows:

A user applies a NetworkPolicy YAML file. The Kubernetes API server validates the YAML and stores the policy object in etcd.

Each node in the cluster runs a CNI plugin agent. This agent watches the Kubernetes API for NetworkPolicy objects.

The CNI plugin translates the high-level network policy into low-level networking rules for the node's operating system (e.g., iptables rules, eBPF programs).

These rules are attached to the network interfaces of the pods (specifically, the veth interfaces that connect the pod to the node). This ensures that traffic entering or leaving the pod must pass through this filter.

When a network packet enters or leaves a pod, the node's kernel checks it against the implemented rules (e.g., iptables). If the packet's source/destination and port match an allowed rule, it is forwarded. If not, it is dropped immediately.

4. Practical Application & Rules of Thumb
The primary goal is to block all unwanted traffic.

Random pods cannot reach a secured backend.

A secured backend cannot randomly reach the internet or other pods.

Rule of Thumb
Ingress Policy: Attach it to the pod that is receiving the traffic.

Egress Policy: Attach it to the pod that is sending the traffic.

Examples:
Frontend → Backend

The Backend is the receiver.

So, an Ingress policy is attached to the Backend pod to allow traffic from the Frontend.

Backend → API-Server

The Backend is the sender.

So, an Egress policy is attached to the Backend pod to allow traffic to the API-Server.

Basic YAML Structure
YAML

# INGRESS RULE (Applied to the receiving pod)
spec:
  podSelector:
    matchLabels:
      app: backend # This policy applies to pods with this label
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: web # Allow traffic FROM pods with this label

# EGRESS RULE (Applied to the sending pod)
spec:
  podSelector:
    matchLabels:
      app: backend # This policy applies to pods with this label
  policyTypes:
  - Egress
  egress:
  - to:
    - podSelector:
        matchLabels:
          app: api # Allow traffic TO pods with this label
5. Business Use Cases for Network Policies
Banking

A bank runs workloads for Retail Banking, Corporate Banking, and Wealth Management in one cluster.

Network Policy: Ensures that workloads from one department (e.g., Retail) cannot access the sensitive data and services of another (e.g., Wealth Management).

Healthcare

A healthcare company must ensure patient & records data is only accessible by approved services to comply with regulations like HIPAA.

Network Policy: Restricts access to the patient databases so that only specific, authorized medical applications can reach them.

E-commerce Platform

The front-end is exposed to the internet, but the payment processing databases must be secured.

Network Policy: Prevents the front-end pods from directly reaching the payment databases, allowing access only from a specific, trusted payment processing service.

IT Environment Segregation

A company runs Dev, Test, and Production environments in the same infrastructure.

Network Policy: Isolates these environments from each other to ensure that developers in the Dev/Test environment cannot accidentally access or modify live production databases.







