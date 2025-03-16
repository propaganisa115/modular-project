# Gunicorn configuration
workers = 2
threads = 2
timeout = 120
max_requests = 1000
max_requests_jitter = 50
worker_class = 'sync'
worker_tmp_dir = '/dev/shm'