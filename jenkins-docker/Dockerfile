FROM jenkins/jenkins:lts

USER root

# Install Docker CLI and curl
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get update && \
    apt-get install -y --fix-missing \
        docker.io \
        curl \
        apt-transport-https \
        gnupg

# Use bash to download and install kubectl safely
RUN curl -sSfL https://dl.k8s.io/release/v1.30.1/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl && \
    chmod +x /usr/local/bin/kubectl && \
    kubectl version --client

USER jenkins

# Add and install plugins
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt
