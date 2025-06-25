# ---- Build Stage ----
FROM golang:1.18.1 AS builder

WORKDIR /app
COPY . .

RUN go mod init service1 && go mod tidy
RUN go build -o service1

# ---- Run Stage ----
FROM ubuntu:22.04

WORKDIR /app
COPY --from=builder /app/service1 .

EXPOSE 8001
CMD ["./service1"]

