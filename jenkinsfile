pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                git branch: 'i200649', url: 'https://github.com/mlooopsformlops/CA4.git'
            }
        }
        
        stage('Execute Docker Compose') {
            steps {
                // Ensure Docker is available
                script {
                    def dockerInstalled = tool name: 'docker', type: 'org.jenkinsci.plugins.docker.commons.tools.DockerTool'
                    if (dockerInstalled == null) {
                        error "Docker is not installed"
                    }
                }
                
                // Execute Docker Compose
                sh 'docker-compose -f DockerCompose.yaml up -d'
            }
        }
    }
    
    post {
        always {
            // Clean up after execution
            stage('Clean up') {
                steps {
                    sh 'docker-compose -f DockerCompose.yaml down'
                }
            }
        }
    }
}
