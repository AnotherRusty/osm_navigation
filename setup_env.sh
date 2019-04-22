#!/bin/bash

if [ -n $OSM_ENV_INITIALIZED ];then
    echo "initializing osm env ..."
    echo "export OSM_ENV_INITIALIZED=1" >> ~/.bashrc
    echo "alias osm_nav='roslaunch osm_nav nav.launch'" >> ~/.bashrc
    echo "done !"
else 
    echo "osm env already initialized"
fi

source ~/.bashrc