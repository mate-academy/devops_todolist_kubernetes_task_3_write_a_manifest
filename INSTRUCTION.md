1) Create namespace and pods:
```shell
kubectl apply -f ./.infrastructure/
```
2) Open port to your local machine:
```shell
kubectl port-forward pod/todoapp 8000:8000 -n mateapp
```