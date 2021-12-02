pipeline { 
    agent any 
    stages { 
        stage ('Checkout') { 
            steps { 
                git branch:'master', url: 'https://github.com/nelsonyeo27/ICT3103LabTest.git'
            } 
        }
        /*stage('Integration Test'){
            parrallel {
                stage('Deploy') {
                agent any
                steps {
                    sh '.jenkins/scripts/deploy.sh'
                    input message: 'Finished using the website? (Click "Proceed" to continue)'
                    sh './jenkins/scripts/kill.sh'
                    }
                }
                stage('Headless Browswer Test'){
                    agent{
                        docker {
                            image 'maven:3-alpine'
                            args '-v/root/.m2:/root/.m2'
                            }
                        }
                        steps {
                            sh 'mvn -B -DskipTests clean package'
                            sh 'mvn test'
                        }
                        post {
                            always{
                                junit 'target/surefire-reports/*.xml'
                            }
                        }

                }
            }
        } */
        stage('Code Quality Check via SonarQube') { 
           steps { 
               script { 
                def scannerHome = tool 'SonarQube'; 
                   withSonarQubeEnv('SonarQube') { 
                   sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=ICT3103 -Dsonar.sources=."
                   } 
               } 
           } 
        } 
    } 
    post { 
        always { 
            recordIssues enabledForFailure: true, tool: sonarQube() 
        } 
    } 
} 
