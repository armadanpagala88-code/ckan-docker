FROM --platform=linux/amd64 ckan/ckan-base:2.11

# Install system dependencies for ckanext-spatial and git for cloning extensions
USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    libgeos-dev \
    libgdal-dev \
    libxml2-dev \
    libxslt1-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install CKAN Extensions
RUN pip3 install --no-cache-dir \
    git+https://github.com/ckan/ckanext-pages.git#egg=ckanext-pages \
    git+https://github.com/ckan/ckanext-spatial.git#egg=ckanext-spatial \
    ckanext-scheming \
    ckanext-geoview \
    -r https://raw.githubusercontent.com/ckan/ckanext-spatial/master/requirements.txt

# Copy custom initialization scripts
COPY --chown=ckan-sys:ckan-sys docker-entrypoint.d/* /docker-entrypoint.d/

# Apply any patches needed to CKAN core or any of the built extensions (not the
# runtime mounted ones)
COPY --chown=ckan-sys:ckan-sys patches ${APP_DIR}/patches

# Copy custom startup overrides to replace base image startup scripts
COPY --chown=ckan:ckan setup/prerun.py.override ${APP_DIR}/prerun.py
COPY --chown=ckan:ckan setup/start_ckan.sh.override ${APP_DIR}/start_ckan.sh
RUN chmod +x ${APP_DIR}/start_ckan.sh

USER ckan

RUN for d in $APP_DIR/patches/*; do \
        if [ -d $d ]; then \
            for f in `ls $d/*.patch | sort -g`; do \
                cd $SRC_DIR/`basename "$d"` && echo "$0: Applying patch $f to $SRC_DIR/`basename $d`"; patch -p1 < "$f" ; \
            done ; \
        fi ; \
    done
