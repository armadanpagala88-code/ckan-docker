#!/bin/bash

if [ -n "$CKAN_SITE_URL" ]; then
   echo "Setting ckan.site_url dynamically to $CKAN_SITE_URL"
   ckan config-tool $CKAN_INI "ckan.site_url=$CKAN_SITE_URL"
fi
