# Django ToDo list

This is a todo list web application with basic features of most web apps, i.e., accounts/login, API, and interactive UI

![ToDo logo](https://i.ibb.co/YDdCcZR/2.png)

## Setup

1. You need apply all manifests
```
kubectl apply -f .infrastructure
```

2. To test app using browser you need write the next command
```
kubectl port-forward pod/app 8081:8081 -n todoapp
```

3. Open browser via link
```
http://localhost:8081/
```

4. To test using busybox and curl, you need to know the ip address of todoapp pod
```
kubectl get pods -o wide -n todoapp
```

5. The next command enable you enter busybox
```
kubectl exec -it -n todoapp busybox -- sh
```

6. Inside busybox write the next command. To get out write 'exit'
```
curl <pod ip adress>:8081
```
