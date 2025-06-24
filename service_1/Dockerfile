# ---- Build Stage ----
FROM golang:1.18.1 AS builder

WORKDIR /service1_app

COPY . .

RUN go mod init service1 && go mod tidy
RUN go build -o service1

# ---- Run Stage ----
FROM ubuntu:22.04

WORKDIR /service1_app

COPY --from=builder /service1_app/service1 .

EXPOSE 8001

CMD ["./service1"]
