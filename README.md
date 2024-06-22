
### package update
1. package build - create deploy file in dist/
```bash
python3 setup.py sdist bdist_wheel
```

2. Run script for uploading package to PyPi
```bash
python3 upload_package.py
```