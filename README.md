## Insane Kubernetes Game

Sample game to demonstrate k8s resources and their power for scalability

## Steps

- Create repo structure
- Create kubernetes cluster
    - Using minikube
- Create kubernetes resources
    - Create a node
    - Create deployments with two pods that will contain two services (Handler/2, Processor/2)
    - Create a service
    - Make the handle accesible by the service
    - Prove the handler can communicate with the processor
    - Prove the client can reach the handler 
    - Prove the handler can scale up if the client is more than 2 or the CPU hit the max allowed limit