# Instructions to deploy and test ToDo App

# Instructions to deploy and test ToDo App

## 1. Apply manifests
Apply all manifests from the `.infrastructure` folder:
```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
2. Wait until ToDo app Pod is ready
bash

kubectl wait --for=condition=Ready pod/todoapp -n todoapp --timeout=60s
3. Check Pods status
bash

kubectl get pods -n todoapp
4. Test ToDo app using port-forward
Forward local port 8000 to the todoapp Pod:

bash

kubectl port-forward pod/todoapp 8000:8000 -n todoapp
Then, in another terminal, run:

curl http://localhost:8000/api/ready/
curl http://localhost:8000/api/live/
5. Test ToDo app using busybox container
Get the Pod IP of todoapp:

POD_IP=$(kubectl get pod todoapp -n todoapp -o jsonpath='{.status.podIP}')
Run curl from inside busybox:

kubectl exec -it busybox -n todoapp -- sh -c "curl http://$POD_IP:8000/api/ready/"
kubectl exec -it busybox -n todoapp -- sh -c "curl http://$POD_IP:8000/api/live/"