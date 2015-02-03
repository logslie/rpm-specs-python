# rpm-specs-python
+ Specs for generating python projects related RPMs.
+ Place to save and store the .specs created.
+ Use it on your own risk.


Example possible usage:

  NAME=python-redis
  VERSION=2.10.3
  # Let's go
  cd $NAME/$VERSION
  mkdir -p BUILD RPMS
  rpmbuild -bb $NAME.spec