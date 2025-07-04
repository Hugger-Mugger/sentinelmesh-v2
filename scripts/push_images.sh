#!/bin/bash
SERVICES=(detector dispatcher playbook-engine runbook-tester metrics-exporter)

for svc in "${SERVICES[@]}"
do
  docker build -t yourrepo/sentinelmesh-$svc ./sentinelmesh-v2/$svc
  docker push yourrepo/sentinelmesh-$svc
done
