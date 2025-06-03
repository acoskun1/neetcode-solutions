FROM alpine:latest

RUN apk add --no-cache bash

COPY --from=kscarlett/nginx-log-generator:latest /app /app

ENV RATE=1
ENV STATUS_OK_PERCENT=65
ENV PATH_MIN=2
ENV PATH_MAX=6

RUN adduser -D -u 1001 nginx
USER nginx

ENTRYPOINT ["/app"]
