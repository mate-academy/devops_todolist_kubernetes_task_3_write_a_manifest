To apply all manifests at once, run the following command from the root of the project:
kubectl apply -f .infrastructure/

To ensure you did everything right write a command:
kubectl port-forward pod/todoapp-pod 8080:8080

Then try to open the app in your browser:
http://localhost:8080/

to test the application using the busyboxplus:curl container use command:
kubectl exec -it busybox-curl -- sh

and then try to reach ip of todoapp with command:

curl



