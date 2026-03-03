ARG PYTHON_VERSION=3.10
ARG INSTALL_VALKEY=false

FROM python:${PYTHON_VERSION}

WORKDIR /app

# Copy entire project
COPY . /app/

# Install the package in editable mode with optional valkey support
# Valkey requires Python 3.10+, so we only install it if available
RUN if [ "${INSTALL_VALKEY}" = "true" ] && python -c 'import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)' 2>/dev/null; then \
      pip install -e .[dev,valkey]; \
    else \
      pip install -e .[dev]; \
    fi
