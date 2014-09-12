# Spatial Cypher Demo


This repo contains the node.js web app and the python scripts for importing data that power [this demo](http://spatialcypherdemo.herokuapp.com)

![scdemo_screenshot.png](screenshot)

The purpose of this demo project is to give an example of what could be accomplished using Neo4j Spatial Cypher, a prototype implemented as part of a Google Summer of Code Project.

For more information, see this wiki:
[https://github.com/johnymontana/neo4j/wiki/tutorial#demo-app-finding-businesses-by-category-within-a-polygon](https://github.com/johnymontana/neo4j/wiki/tutorial#demo-app-finding-businesses-by-category-within-a-polygon)


## Data

This project makes use of the Yelp! Academic dataset. The data is not distributed as part of this repository, but can be obtained [here]() and should be saved into the data/ directory once obtained.

## Webapp

The `webapp/scdemo` directory contains the node.js web application for this project. Install node and npm first. Then:

1. `webapp/scdemo/npm install`
1. `webapp/scdemo/bin/www` -or- `webapp/scdemo/npm start`

## Neo4j server extension

The backend is powered by a Neo4j Server extension available [here](https://github.com/johnymontana/scdemo-extension).