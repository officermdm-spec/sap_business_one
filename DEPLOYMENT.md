# DigitalOcean Droplet deployment

This deployment runs Django, PostgreSQL, and Caddy on one Droplet with Docker Compose. PostgreSQL is only reachable on the private Compose network; its data is stored in a persistent Docker volume. Caddy obtains and renews HTTPS certificates automatically.

## 1. Prepare the Droplet

Create an Ubuntu Droplet, install Git and Docker Engine with the Docker Compose plugin using Docker's official Ubuntu instructions, and allow inbound TCP ports 22, 80, and 443 in the Droplet firewall. Do not open PostgreSQL port 5432.

Create an A record for your domain pointing to the Droplet's public IPv4 address. Wait for DNS to resolve before starting Caddy.

## 2. Clone and configure

SSH into the Droplet and run:

```sh
git clone <your-GitHub-repository-URL> sap-business-one
cd sap-business-one
cp .env.example .env
chmod 600 .env
openssl rand -hex 32
openssl rand -hex 24
nano .env
```

In `.env`, set `DOMAIN`, `ALLOWED_HOSTS`, and `CSRF_TRUSTED_ORIGINS` to your real domain, and replace `SECRET_KEY` and `POSTGRES_PASSWORD` with the two generated values. Do not commit `.env` or paste its secrets into GitHub. Keep `DEBUG=False`.

## 3. Start the services

```sh
docker compose up --build -d
docker compose ps
docker compose logs -f web caddy
```

The web container applies Django migrations and collects static files before starting Gunicorn. Caddy serves the site over HTTPS once DNS points to the Droplet and ports 80/443 are reachable.

## 4. Create an administrator

```sh
docker compose exec web python manage.py createsuperuser
```

## 5. Deploy later code changes

After pushing changes to GitHub:

```sh
git pull
docker compose up --build -d
docker compose logs --tail=100 web
```

## Database and secrets

The PostgreSQL service has no public port mapping. Its data persists in the `postgres_data` Docker volume across container rebuilds. Back up the database regularly and copy backups off the Droplet; a volume is not a backup.

This project previously had a Django secret key and database connection details in its settings file. The current settings no longer contain those values. If any were real and have ever been pushed to GitHub, rotate them before going live (including replacing `SECRET_KEY` and the database password).
