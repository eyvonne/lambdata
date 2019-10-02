FROM debian 

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get upgrade -y && \
apt-get install python3-pip curl nano -y && \
pip3 install pandas numpy sklearn && \
pip3 install -i https://test.pypi.org/simple lambdata-eyvonne==0.1.17 && \
python3 -c "import lambdata_eyvonne; print('hooray-success!!!')"
