FROM python:3.8.6
RUN   set -e \
      && export DEBIAN_FRONTEND=noninteractive \
      && apt-get update \
      && apt-get -qq install --no-install-recommends \
      && useradd -m -u 1000 e2e \
      && mkdir /reports \
      && chmod a+rwx /reports \
      && chown e2e:e2e /reports
VOLUME ["/reports"]
#use dos2unix utility if building from windows
COPY entrypoint.sh /usr/local/bin/entrypoint
RUN chmod 755 /usr/local/bin/entrypoint
ENTRYPOINT [ "/usr/local/bin/entrypoint" ]
RUN chown -R e2e:e2e /home/e2e/
RUN chmod -R 0777 /home/e2e/
USER e2e
WORKDIR /home/e2e
COPY . /home/e2e/
RUN set -e \
    && python3 -m venv venv \
    && . venv/bin/activate \
    && pip install --upgrade pip  --no-cache-dir wheel \
    && pip install --no-cache-dir --use-feature=2020-resolver . \
    && deactivate