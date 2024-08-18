FROM quay.io/jupyter/minimal-notebook:lab-4.2.4

WORKDIR /home/jovyan/code
EXPOSE 8888
HEALTHCHECK NONE

COPY --chown=jovyan:users Challenge.ipynb /home/jovyan/code/Challenge.ipynb

CMD jupyter lab /home/jovyan/code/Challenge.ipynb --ServerApp.base_url=$SERVER_BASE_URL  --ServerApp.allow_origin='*' --LabApp.default_url='/doc/tree/Challenge.ipynb'
#--ServerApp.ip='*'