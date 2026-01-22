service {
  name = "url-service"
  id   = "web-1"
  port = 5000
  tags = ["python", "api"]

  check {
    id       = "url-service-check"
    name     = "HTTP Health Check"
    http     = "http://url-service:5000/health"
    method   = "GET"
    interval = "10s"
    timeout  = "1s"
  }
}
