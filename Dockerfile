FROM rust:1.75.0 as builder-svgtogcode
WORKDIR /usr/src/svg_to_gcode
COPY ./svg_to_gcode/Cargo.toml .
Copy ./svg_to_gcode/Cargo.lock .
#RUN cargo build --release
COPY svg_to_gcode/src ./src
COPY svg_to_gcode/resources ./resources
RUN cargo build --release


#FROM debian:bullseye-slim as svgtogcode
#RUN apt-get update && apt-get install -y extra-runtime-dependencies && rm -rf /var/lib/apt/lists/*
#COPY --from=builder /usr/local/cargo/bin/svg_to_gcode /usr/local/bin/svg_to_gcode
#CMD ["svg_to_gcode"]


FROM python:3.9
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./web_app /app/web_app
COPY ./kanban_to_svg /app/kanban_to_svg
COPY --from=builder-svgtogcode /usr/src/svg_to_gcode/target/release/svg_to_gcode /usr/local/bin/svg_to_gcode
EXPOSE 80
CMD ["uvicorn", "web_app.main:app", "--host", "0.0.0.0", "--port", "80"]