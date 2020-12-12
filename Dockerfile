ARG BASE_CONTAINER=ucsdets/datascience-notebook:2020.2-stable

FROM $BASE_CONTAINER

LABEL maintainer="UC San Diego ITS/ETS <ets-consult@ucsd.edu>"

USER root

COPY /run_jupyter.sh /

USER $NB_UID

CMD ["/bin/bash"]