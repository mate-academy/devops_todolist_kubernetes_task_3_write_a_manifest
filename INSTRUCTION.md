# 1) Застосувати маніфести
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/service.yml

# 2) Перевірити, що pod-и працюють
kubectl -n todoapp get pods -o wide
kubectl -n todoapp get endpoints todoapp

# 3) Перевірка readiness/liveness через busybox (DNS ім'я сервісу)
kubectl -n todoapp exec -it busybox-curl -- sh -c \
  "nslookup todoapp.todoapp.svc.cluster.local && \
   wget -qO- http://todoapp:8000/api/healthz/ready && \
   wget -qO- http://todoapp:8000/api/healthz/live"

# 4) Перевірка з хоста (port-forward сервісу)
kubectl -n todoapp port-forward svc/todoapp 18081:8000
# у новій вкладці терміналу/в браузері:
curl -i http://localhost:18081/api/healthz/ready
curl -i http://localhost:18081/api/healthz/live
# або відкрити http://localhost:18081/api/
