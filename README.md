# Apache Exporter RPM builder

# How to build and install rpm on CentOS 8
```bash
# sudo yum install -y rpm-build
# git clone https://github.com/tgerov/apache_exporter-rpm
# cd apache_exporter-rpm/
# make
# sudo rpm -ivh rpmbuild/RPMS/x86_64/apache-exporter-0.8.0-1.el8.x86_64.rpm
# sudo systemctl enable --now apache_exporter
````

# Install from prebuild RPM on CentOS 8
````bash
# rpm -ivh https://github.com/tgerov/apache_exporter-rpm/releases/download/0.8.0-1/apache-exporter-0.8.0-1.el8.x86_64.rpm
````


