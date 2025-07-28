# PersonalBlog API

A beginner-friendly **Blog API** built with **Django** and **Django REST Framework**.  
It supports full CRUD operations and author-based access control.

---

## Features

- Create, Read, Update, Delete (CRUD) for blog posts
- Only the author can edit or delete their own posts
- User-based post ownership (`ForeignKey` to `User`)
- Automatic timestamp on post creation (`pub_date`)
- JSON-based clean API response
- Filtering by publishing dates

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/posts/` | List all posts |
| POST   | `/posts/create` | Create a new post *(requires login)* |
| GET    | `/post/<id>/` | Get a single post by ID |
| PUT    | `/post/<id>/update` | Update a post *(author only)* |
| DELETE | `/post/<id>/delete` | Delete a post *(author only)* |

> The `author` field is automatically set from the logged-in user. It is **read-only** in API requests.

---

## Filtering

The GET /blogapi/posts/ endpoint supports filtering by pub_date.
Example

GET /blogapi/posts/?pub_date=2025-07-28

This will return only the posts that were published on July 28, 2025.

    Parameter: pub_date

    Format: YYYY-MM-DD

    Type: Query parameter

    Optional: Yes