ToDo App Kubernetes Instructions

Prerequisites



The following tools are required:



Docker

kubectl

A running Kubernetes cluster

Docker image



The ToDo application image is available on Docker Hub:



aezakmi565/todoapp:3.0.0



To build the image from the src directory:



cd src

docker build -t aezakmi565/todoapp:3.0.0 .





To push the image to Docker Hub:



docker push aezakmi565/todoapp:3.0.0



Apply Kubernetes manifests



The Kubernetes manifests are located in the .infrastructure directory.



Apply all manifests:



kubectl apply -f .infrastructure/





If the Busybox pod fails because the namespace has not been created yet, apply the namespace first:



kubectl apply -f .infrastructure/namespace.yml

kubectl apply -f .infrastructure/busybox.yml

kubectl apply -f .infrastructure/todoapp-pod.yml





Check the pods:



kubectl get pods -n todoapp





The expected result is:



NAME       READY   STATUS

busybox    1/1     Running

todoapp    1/1     Running



Test using port-forward



Forward port 8000 from the ToDo application pod to the local machine:



kubectl port-forward pod/todoapp 8000:8000 -n todoapp





The application is then available at:



http://localhost:8000





Test the readiness endpoint:



curl http://localhost:8000/api/readiness/





Expected response:



{"status": "ready"}





Test the liveness endpoint:



curl http://localhost:8000/api/liveness/





Expected response:



{"status": "alive"}



Test using BusyboxPlus



Check the IP address of the ToDo application pod:



kubectl get pod todoapp -n todoapp -o wide





Start a shell inside the BusyboxPlus container:



kubectl exec -it busybox -n todoapp -- sh





Use the IP address displayed for the todoapp pod.



Test the readiness endpoint:



curl http://TODOAPP\_IP:8000/api/readiness/





Expected response:



{"status": "ready"}





Test the liveness endpoint:



curl http://TODOAPP\_IP:8000/api/liveness/





Expected response:



{"status": "alive"}





Exit the BusyboxPlus container:



exit



Check readiness and liveness probes



To inspect the configured probes:



kubectl describe pod todoapp -n todoapp





The ToDo application pod should have both a readiness probe and a liveness probe configured.



Delete Kubernetes resources



To remove the Kubernetes resources:



kubectl delete -f .infrastructure/

