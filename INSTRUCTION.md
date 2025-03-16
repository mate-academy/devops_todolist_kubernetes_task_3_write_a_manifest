1. To apply all manifests do those commands:<br>
First:<br>
`kubectl apply -f .\.infrastructure\namespace.yml`<br>
Then:<br>
`kubectl apply -f .\.infrastructure\busybox.yml`<br>
`kubectl apply -f .\.infrastructure\todoapp-pod.yml`<br>
2. To port forward app service, use:<br>
`kubectl port-forward pod/todoapp 8080:8080 -n todoapp`
3. To test app using `curl` follow this:<br>
Firstly check ip of the `todoapp` container using:<br>
`kubectl get pods -n todoapp -o wide`<br>
Then enter shell environment on curl using:<br>
`kubectl exec -it -n todoapp curl -- sh`<br>
And then use this command to test web-app:<br>
`curl <todoapp-ip>`