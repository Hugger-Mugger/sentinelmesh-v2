#!/bin/bash

case $1 in
  start) docker compose up detector dispatcher playbook-engine ;;
  stop)  docker compose down ;;
  inject) docker compose run runbook-tester python trigger.py "$2" ;;
  burst) docker compose run runbook-tester python burst_injector.py ;;
  *)
    echo "Usage: $0 {start|stop|inject <type>|burst}"
    ;;
esac
