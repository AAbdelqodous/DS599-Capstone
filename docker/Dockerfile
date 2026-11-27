# DS-599 Capstone: Python + Jupyter + data science libraries
FROM python:3.12-slim

# libgomp1 is needed by LightGBM and XGBoost
RUN apt-get update \
 && apt-get install -y --no-install-recommends libgomp1 \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Your files live here. This folder is linked to the "work" folder on your PC.
WORKDIR /work
EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", \
     "--ServerApp.token=", "--ServerApp.password=", "--ServerApp.root_dir=/work"]
