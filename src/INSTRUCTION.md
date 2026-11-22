Requirements: Docker, Kubernetes, kubectl.

To deploy the application, run these commands from the project root:
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml

To check the Pods:
kubectl get pods -n todoapp
Both Pods should have Running status and READY 1/1.

To access the application:
kubectl port-forward -n todoapp pod/todoapp 8000:8000
Open http://localhost:8000 in your browser.
Docker image: storozhuk21/todoapp:3.0.0

To test the application from the BusyBox pod:
```bash
TODOAPP_IP=$(kubectl get pod todoapp -n todoapp -o jsonpath='{.status.podIP}')
kubectl exec -n todoapp busybox -- curl -i "http://${TODOAPP_IP}:8000/api/ready/"
```