# Skip CSRF checks for requests from localhost - Django Middleware

## What CSRF?

Cross-site request forgery (CSRF) is a type of attack that can occur when a malicious website tricks a user's browser into performing an unwanted action on a different website.

## Why we need this middleware?

This middleware is specifically designed to skip Django's CSRF checks for local requests (e.g., during development or internal API calls). 

Skipping CSRF checks from localhost is often useful for testing or local development but should be used carefully/removed in production environments.

## Implementation
If the request's origin is from localhost (e.g., `127.0.0.1` or `::1` for IPv6), it will bypass CSRF verification.

## Usage

1. Copy the content of `custom_csrf_middleware.py` or clone the project and move that file to project.
2. Create a package `middlewares` in your Django app.
3. Paste the file to it. Mention it in `__init__` file.
4. Open the `settings.py` of the project. Find `MIDDLEWARE`
5. Comment the line `#"django.middleware.csrf.CsrfViewMiddleware",`
6. Add the middleware `'my_app_name.middlewares.CustomCsrfViewMiddleware',` (just paste)
7. Done
