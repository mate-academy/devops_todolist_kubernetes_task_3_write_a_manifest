[Docker Hub repo](https://hub.docker.com/repository/docker/cara7ies/todoapp/general)


## Step 1
---
Use the commands to deploy the pod: 
```bash
kubectl apply -f service.infrastructure/namespaces.yml  
kubectl apply -f service.infrastructure/app_manifest.yml  
```

> [!NOTE]
> Perform port forwarding to verify that the pod is working:
> ```bash kubectl port-forward pod/todoapp 8001:8000 -n todoapp```

### Access the Application

Once the pod is running, open `http://127.0.0.1:8001` in your browser to access the application.