import logging
import os

log_path = "log/"
if not os.path.exists(log_path):
    os.makedirs(log_path)

logging.basicConfig(filename=f"{log_path}/app.log",
                    level=logging.DEBUG,
                    format="[%(asctime)s] %(levelname)s in %(module)s: %(message)s")

logger = logging.getLogger(__name__)
