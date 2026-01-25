# Ecommerce Backend Project

This repository contains the backend for an ecommerce platform. It provides APIs and services for managing products, users, orders, payments, and more. Built with Python and Django, it is designed for scalability, security, and ease of integration with frontend clients.

## Features

- User authentication and management
- Product catalog CRUD operations
- Shopping cart and checkout
- Order processing and tracking
- Payment integration (extensible)
- Admin dashboard endpoints
- RESTful API design
- Dockerized for easy deployment

## Technologies

- Python
- Django
- Celery (for background tasks)
- Docker
- Tailwind CSS (for admin/static assets)

## Getting Started

### Prerequisites

- Docker & Docker Compose
- Python 3.10+

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ecommerce-backend.git
   cd ecommerce-backend
   ```
2. Build and start the services:
   ```bash
   docker-compose up --build
   ```
3. Access the API at `http://localhost:8000/`

### Environment Variables

Configure environment variables in `.env` for database, secret keys, and other settings.

## Project Structure

- `src/` - Django project source code
- `assets/` - Frontend assets (for admin/static)
- `bin/` - Utility scripts
- `Dockerfile` & `compose.yaml` - Container setup

## Usage

- Register users, add products, and place orders via API endpoints.
- Admin endpoints available for managing catalog and orders.

## Media uploads

To allow user-uploaded media (images) the project uses Django `MEDIA_ROOT` and `MEDIA_URL`.

- Development: the compose setup mounts a host `./media` directory into the container at `/app/media`. Uploaded files will be saved under `MEDIA_ROOT` (by default `./media/product_images/`).
- Production: serve media using your fronting server (nginx) or configure external storage (S3).

Compose example: `compose.yaml` mounts `./media` by default via the `DOCKER_MEDIA_VOLUME` variable. To override, set that env var in your `.env`.

Example curl to create a product with an image (multipart/form-data):

```bash
curl -X POST http://localhost:8000/api/v1/products/ \
   -H "Authorization: Bearer <TOKEN>" \
   -F "name=My Product" \
   -F "price=19.99" \
   -F "stock=10" \
   -F "image=@/path/to/local/image.jpg"
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
