# Demo monitoring ELK

Projeto desenvolvido para a discinplina de Administração de sistemas no período 22.2.

---

## O que foi feito?

- Foi desenvolvida uma aplicação simples em python, usando flask, que exibe um hello world na tela.
- Foi feito um docker compose que sobe as instâncias do ELK, do grafana e do prometheus.
- Além disso, também foi feito um script em pyhton que executa um número X de requisições a fim de realizar um aumento na carga do ELK para observar o consumo de recursos pelo grafana.

---

## ELK Setup

- Foi utilizado o Docker para configurar o ELK, utilizamos as imagens oficiais disponibilizadas no Docker Hub ([elasticsearch](https://hub.docker.com/_/elasticsearch), [logstash](https://hub.docker.com/_/logstash), [kibana](https://hub.docker.com/_/kibana))
- Já para a configuração do Prometheus e Grafana utilizamos um [repositório externo](https://github.com/stefanprodan/dockprom)
- O dashboard que utilizamos é o padrão, já disponibilizado pelo Grafana

---

## Demonstração

Link para a [demo](https://drive.google.com/drive/folders/1fpSWkp003plBiEdSZxc49ZHZCwXvkizt)
