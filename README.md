Docker build of Loris 2 IIIF Image Server with Grok on Ubuntu. This build is configured to take images from the Stanford Daily archives S3 bucket. You can modify the configuration in `loris2.conf`.
===========

# Setup
```
docker build -t thestanforddaily/loris-grok-docker .
docker run -d -p 5004:5004 thestanforddaily/loris-grok-docker
```

# Running
Go to http://localhost:5004/data.2012-aug/data/stanford/1920/10/01_01/Stanford_Daily-IMG/Stanford_Daily_19201001_0001_0001.jp2/0,0,200,200/400,/0/default.jpg