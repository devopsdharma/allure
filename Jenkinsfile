// Uses Declarative syntax to run commands inside a container.
pipeline {
    agent {
        kubernetes {
            containerTemplate {
                name 'allure'
                image 'allure-pytest:v5'
                command 'sleep'
                args 'infinity'
            }
            defaultContainer 'allure'
            retries 2
        }
    }
    stages {
        stage('Main') {
            steps {
                sh 'pwd'
                sh 'ls -al'
                sh 'python --version'
                sh 'pip --version'
                // sh 'java -version'
                sh 'python -m pytest --alluredir allure-results'
                // sh 'allure serve allure-results'
                archiveArtifacts artifacts: 'allure-results'
            }
        }
    }
}
