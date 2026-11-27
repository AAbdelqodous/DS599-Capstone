# DS-599 Capstone: Jupyter in Docker

This gives you Python 3.12, JupyterLab, and all the libraries for the capstone
(pandas, numpy, scikit-learn, imbalanced-learn, XGBoost, LightGBM, statsmodels,
Optuna, SHAP, matplotlib, seaborn, python-docx, openpyxl, PuLP and more).

**Your files are safe.** Everything you save in Jupyter goes into the `work`
folder on your PC. Stopping, restarting or even deleting the container does not
remove it. Your Phase 1 files are already inside `work/phase1`.

## One-time setup (Windows)

1. Download and install **Docker Desktop**: https://www.docker.com/products/docker-desktop/
   Accept the default options (it uses WSL 2). Restart the PC if asked.
2. Open Docker Desktop and wait until it says **Engine running**.
3. Put this whole folder somewhere simple, for example `C:\capstone\docker`.

## Every time you want to work

- **Start:** double-click `start.bat`. The first time takes 5 to 10 minutes
  (it downloads and installs everything). After that it starts in seconds.
  Your browser opens at http://localhost:8888
- **Stop:** double-click `stop.bat` (or just shut down the PC).

Docker Desktop must be running before you double-click `start.bat`.

### Same thing from a terminal (Windows, Mac or Linux)

```
cd C:\capstone\docker
docker compose up -d --build     # start
docker compose down              # stop
```

## Tips

- In Jupyter, open files with paths relative to the notebook, for example
  `pd.read_csv("phase1/data_clean/telco_clean.csv")` from a notebook in `work`.
- To add a library: add it to `requirements.txt` and run `start.bat` again.
  For a quick test you can also run `%pip install <name>` in a notebook
  (that one is lost when the container is rebuilt).
- "Port 8888 is already in use": in `docker-compose.yml` change
  `127.0.0.1:8888:8888` to `127.0.0.1:8889:8888` and open http://localhost:8889
- Jupyter has no password, but it only accepts connections from your own PC.
