# ecommerce_platform/payments/Dockerfile

FROM golang:1.16

WORKDIR /payments

COPY . .

RUN go mod init payments
RUN go mod tidy
RUN go build -o main .

EXPOSE 8003

CMD ["./main"]
