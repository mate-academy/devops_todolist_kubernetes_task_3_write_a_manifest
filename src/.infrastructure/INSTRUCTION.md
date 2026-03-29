## To apply namespace
`kubectl apply -f namespace.ym`

## To apply busybox
`kubectl apply -f busybox.yml`

## To apply todoapp
`kubectl apply -f todoapp-pod.yml`

## To check your todoapp is working from your machine:
1. Use this command to forward port from your local machine into pod:

``kubectl port-forward pod/todoapp-pod <your_port>:8000 -n todoapp``
2. Go to `localhost:<your_port>`

## To check your todoapp is working from busybox:
1. Get to know IP of todoapp-pod by:

`kubectl describe pod todoapp-pod -n todoapp`
2. Connect to busybox by:

`kubectl exec -it busybox-pod -n todoapp -- sh`
3. Execute command:

`curl 10.1.0.24:8000`
