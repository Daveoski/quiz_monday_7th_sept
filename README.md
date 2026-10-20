# VIP Registration Desk API

A small **FastAPI** service built as a timed quiz. It shows how to validate request **headers** and **cookies** with Pydantic models, alongside a normal JSON body.

## Features

- `POST /staff` registers a staff member. The request must carry an `X-Union-Pass` header; the body is validated (password at least 8 characters) and the password is never returned in the response.
- `GET /desk/greeting` reads `session_id` and `language` cookies and replies with a greeting in English or Nigerian Pidgin.
- Example payloads appear in the generated Swagger docs.

## Getting started

```bash
uv sync
uv run fastapi dev main.py
```

Open http://127.0.0.1:8000/docs.

### Example request

```bash
curl -X POST http://127.0.0.1:8000/staff \
  -H "Content-Type: application/json" \
  -H "X-Union-Pass: UNION-2026-VIP" \
  -d '{"username":"daveoski_vip","full_name":"Okechukwu David","password":"VIPpass2026","station":"Lagos VIP Desk"}'
```

The union pass value was fixed by the quiz brief. In a real service it would come from an environment variable.

## Tech stack

Python 3.12 · FastAPI · Pydantic · uv

## License

[MIT](LICENSE)
