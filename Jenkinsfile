pipeline {
    agent any

    stages {

        stage('Inicio') {
            steps {
                echo 'Iniciando Pipeline de Integración Continua'
            }
        }

        stage('Verificar Docker') {
            steps {
                bat 'docker --version'
            }
        }
        
        stage('Recrear Contenedores') {
            steps {
                bat 'docker compose down'
                bat 'docker compose up -d'
            }
        }
        
        stage('Verificar Contenedores') {
            steps {
                bat 'docker compose ps'
            }
        }

        stage('Finalizado') {
            steps {
                echo 'Pipeline ejecutado correctamente'
            }
        }
    }
}
