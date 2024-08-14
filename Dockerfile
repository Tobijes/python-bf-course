FROM quay.io/jupyter/minimal-notebook:lab-4.2.4

COPY --chown=jovyan:users code /home/jovyan/code

WORKDIR /home/jovyan/code

EXPOSE 8888

CMD jupyter lab /home/jovyan/code/Challenge.ipynb --ServerApp.base_url=$SERVER_BASE_URL  --ServerApp.allow_origin='*' --LabApp.default_url='/doc/tree/Challenge.ipynb'
#--ServerApp.ip='*'