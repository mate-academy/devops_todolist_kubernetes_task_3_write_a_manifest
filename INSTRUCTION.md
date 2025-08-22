# створити namespace
kubectl apply -f .infrastructure/namespace.yml

# створити Pod з ToDo app (образ: vitalysemeniv/todoapp:3.0.0)
kubectl apply -f .infrastructure/todoapp-pod.yml

# створити Pod для тестів (busyboxplus:curl)
kubectl apply -f .infrastructure/busybox.yml

# перевірити, що поди запущені в неймспейсі todoapp
kubectl -n todoapp get pods -o wide


# Check
kubectl -n todoapp get pods -o wide
kubectl -n todoapp get svc

# Port-forward (якщо 8081 зайнятий — вибери інший, напр. 18081)
kubectl -n todoapp port-forward svc/todoapp 18081:8000

# Test from host
curl -i http://localhost:18081/healthz/ready
curl -i http://localhost:18081/healthz/live

# Test from inside cluster
kubectl -n todoapp exec -it busybox-curl -- sh -c "\
nslookup todoapp.todoapp.svc.cluster.local && \
wget -qO- http://todoapp:8000/healthz/ready && \
wget -qO- http://todoapp:8000/healthz/live"

### If 'Only one usage of each socket address...' error

1) netstat -ano | findstr :8081
2) tasklist /FI "PID eq <PID>"
3) taskkill /PID <PID> /F
4) або одразу використай інший локальний порт: 18081:8000
5) переконайся, що локальні docker-контейнери не маплять 8000/8081:
   docker ps --format "{{.ID}}\t{{.Ports}}\t{{.Names}}" | findstr 8000
   docker stop <ID>
