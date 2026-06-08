pipeline {
    agent any

    stages {

        stage('Clonar Proyecto') {
            steps {
                echo 'Descargando proyecto desde GitHub'
            }
        }

        stage('Verificar Archivos') {
            steps {
                bat 'dir'
            }
        }

        stage('Verificar Docker') {
            steps {
                bat 'docker --version'
            }
        }

        stage('Finalizado') {
            steps {
                echo 'Pipeline ejecutado correctamente'
            }
        }
    }
}
