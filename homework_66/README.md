# Task Management API — Docker Networking

FastAPI-ს REST API, რომელიც დავალებებს PostgreSQL-ში ინახავს. API და მონაცემთა ბაზა ცალკე კონტეინერებში მუშაობს და ერთმანეთს `task-network` Docker ქსელში უკავშირდება. API მონაცემთა ბაზას სერვისის სახელით — `db` — უკავშირდება და არა `localhost`-ით.

## გაშვება Docker Compose-ით

Docker Compose ავტომატურად შექმნის `task-network` ქსელს, ააგებს API image-ს და ჯერ ჯანმრთელ PostgreSQL კონტეინერს, შემდეგ API-ს გაუშვებს:

```bash
docker compose up --build -d
```

თუ Docker-ის socket-ზე `permission denied` შეცდომას მიიღებთ, გაუშვით ბრძანება `sudo`-თი:

```bash
sudo docker compose up --build -d
```

API: <http://localhost:8001>
Swagger UI: <http://localhost:8001/docs>

## ცალკე `docker run` ბრძანებებით გაშვება

Compose-ის ნაცვლად გამოიყენეთ შემდეგი ბრძანებები. PostgreSQL მზად გახდება, API კი `db` hostname-ით დაუკავშირდება `task-db` კონტეინერს:

```bash
sudo docker network create task-network
sudo docker build -t task-api .
sudo docker run -d --name task-db --network task-network \
  -e POSTGRES_DB=tasks_db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  postgres:16

# დაელოდეთ, სანამ PostgreSQL მზად იქნება
until sudo docker exec task-db pg_isready -U postgres -d tasks_db; do sleep 1; done

sudo docker run -d --name task-api --network task-network \
  -e DATABASE_URL=postgresql+psycopg2://postgres:postgres@task-db:5432/tasks_db \
  -p 8001:8000 task-api
```

თუ უკვე არსებობს `task-network` ან ამავე სახელის კონტეინერები, გამოიყენეთ Compose-ის გაშვების გზა ან ჯერ წაშალეთ მხოლოდ შესაბამისი ძველი რესურსები.

## API endpoints

| მეთოდი | მისამართი | აღწერა |
|---|---|---|
| `POST` | `/tasks` | დავალების შექმნა |
| `GET` | `/tasks` | ყველა დავალების მიღება |
| `GET` | `/tasks/{task_id}` | ერთი დავალების მიღება |
| `DELETE` | `/tasks/{task_id}` | დავალების წაშლა |

მაგალითი:

```bash
curl -X POST http://localhost:8001/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Docker-ის სწავლა","description":"ქსელის დავალების დასრულება","is_completed":false}'

curl http://localhost:8001/tasks
curl http://localhost:8001/tasks/1
curl -i -X DELETE http://localhost:8001/tasks/1
```

## გაჩერება

```bash
docker compose down
```

თუ Docker-ის socket-ზე წვდომისთვის `sudo` გამოიყენეთ, გაჩერების ბრძანებებშიც დაამატეთ `sudo`.

`docker run`-ით გაშვებული კონტეინერების გაჩერება და წაშლა:

```bash
sudo docker rm -f task-api task-db
sudo docker network rm task-network
```

მონაცემების ჩათვლით კონტეინერებისა და volume-ის წასაშლელად:

```bash
sudo docker compose down -v
```
