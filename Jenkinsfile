// Uses Declarative syntax to run commands inside a container.
pipeline {
    agent {
        kubernetes {
            containerTemplate {
                name 'pytest'
                image 'allure-pytest:v5'
                command 'sleep'
                args 'infinity'
            }
            containerTemplate {
                name 'allure'
                image 'vhsantos26/allure-report:2.6.0'
                command 'sleep'
                args 'infinity'
            }
        }
    }
    stages {
        stage('Main') {
            container('pytest') {
            steps {
                sh 'pwd'
                sh 'ls -al'
                sh 'python --version'
                sh 'pip --version'
                // sh 'java -version'
                sh 'python -m pytest --alluredir allure-results'
                sh 'ls allure-results'
                // sh 'allure serve allure-results'
                stash includes: 'allure-results/**/*', name: 'results'
            }
            }
        }
        stage ( 'Main2') {
            container('allure') {
            steps {
                sh 'java -version'
                // sh 'python -m pytest --alluredir allure-results'
                unstash 'results'
                sh 'ls allure-results'
                sh 'allure serve allure-results'
                // stash includes: 'allure-results/**/*', name: 'results'
            }
            }
        }
    }
}
