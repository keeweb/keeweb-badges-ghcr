"""Gunicorn configurations."""

max_requests = 1500
preload_app = True
timeout = 10
wsgi_app = "keeweb_ghcr.server:app"
