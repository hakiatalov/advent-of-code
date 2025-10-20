# Use the official Open-JDK image as our starting point
FROM openjdk:25-jdk

# Install essential tools for a good developer experience 
# Use microdnf as the image is red-hat based  
RUN microdnf install -y \
    git \
    gcc \
    gcc-c++ \
    make \
    curl \
    wget \
    zsh \
    procps-ng \
    && microdnf clean all
    
# Make zsh the default shell 
# RUN chsh -s $(which zsh)

# Print the version to confirm installation 
RUN java --version 
RUN git --version
