# How to Run Odoo 19 in Docker

This guide explains how to build and run your Odoo 19 instance using the provided Docker
files.

## Prerequisites

- Docker and Docker Compose installed.

## Steps to Run

1. **Navigate to the Docker directory**:

   ```bash
   cd /home/abdelhadi-eddiraa/Desktop/Openeducat/edu-system/docker/19
   ```

2. **Build and start the containers**:

   ```bash
   docker-compose up --build -d
   ```

3. **Access Odoo**: Once the containers are running, open your browser and go to:
   [http://localhost:8069](http://localhost:8069)

4. **Add Custom Addons**: Place your custom Odoo modules in
   `/home/abdelhadi-eddiraa/Desktop/Openeducat/edu-system/my-generated-modules`. They
   are mounted to `/mnt/extra-addons` inside the container.

## Using the OCA Template

To update or generate new modules, use `copier` in the template folder:

```bash
cd /home/abdelhadi-eddiraa/Desktop/Openeducat/edu-system
copier copy . ./my-generated-modules --trust
```

Your modules in `my-generated-modules` will be automatically seen by Odoo.

## Commands Reference

- **Stop the instance**: `docker-compose stop`
- **View logs**: `docker-compose logs -f odoo`
- **Restart**: `docker-compose restart`
