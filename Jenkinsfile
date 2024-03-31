pipeline {
    agent any  // Can run on any available Jenkins agent

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'i200402', // Your branch name
                    credentialsId: '1', // Your Git credentials ID
                    url: 'https://github.com/mlooopsformlops/CA4.git'  // Your repository URL
            }
        }
        stage('Build Database Image') {
            steps {
                sh 'docker build -t mongo_db:latest .'  // Use your desired image name
            }
        }
        // Optional stage to push the image to a registry
        stage('Push Image to Registry (Optional)') {
            when {
                expression { // Optional condition to push only on specific branches/tags
                    return env.BRANCH_NAME == 'master' || env.TAG_NAME != null
                }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: '2', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh 'docker login -u $USERNAME -p $PASSWORD'
                    sh 'docker push mongo_db:latest'
                }
            }
        }
    }
}