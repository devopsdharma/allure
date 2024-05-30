// Uses Declarative syntax to run commands inside a container.
pipeline {
    agent {
        kubernetes {
            containerTemplate {
                name 'pytest'
                image 'allure-pytest:v5'
                command 'sleep'
                args 'infinity'
            },
            containerTemplate {
                name 'allure'
                image 'vhsantos26/allure-report:2.6.0'
                command 'sleep'
                args '3600'
            }
        }
    }
    stages {
        stage('Main') {
            steps {
                container('pytest') {
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
            steps {
                container('allure') {
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

// // #!/usr/bin/env groovy

// // properties([
// //         buildDiscarder(logRotator(numToKeepStr: '5')),
// // ])

// ansiColor {
//     timestamps {
//         podTemplate([
//                 containers : [
//                         steps.containerTemplate([
//                                 args           : 'infinity',
//                                 command        : 'sleep',
//                                 image          : 'allure-pytest:v5',
//                                 name           : 'pytest',
//                                 ttyEnabled     : true,
//                         ]),
//                         steps.containerTemplate([
//                                 args           : 'infinity',
//                                 command        : '3600',
//                                 image          : 'vhsantos26/allure-report:2.6.0',
//                                 name           : 'allure',
//                                 ttyEnabled     : true,
//                         ]),
//                 ],
//                 inheritFrom: 'kube-prep',
//         ]) {
//             node(POD_LABEL) {
//                 stage('pytest') {
//                     container('pytest') {
//                         sh 'pwd'
//                         sh 'ls -al'
//                         sh 'python --version'
//                         sh 'pip --version'
//                         sh 'python -m pytest --alluredir allure-results'
//                         sh 'ls allure-results'
//                         stash includes: 'allure-results/**/*', name: 'results'
//                     }
//                 }
//                     milestone 10
//                 }
//                 stage('allure') {
//                     container('allure') {
//                         sh 'java -version'
//                         unstash 'results'
//                         sh 'ls allure-results'
//                         sh 'allure serve allure-results'
//                     }
//                     milestone 20
//                 }
//         }
//     }
// }
