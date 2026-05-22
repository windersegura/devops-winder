#!/bin/bash

# Ejecutado automaticamente al iniciar Floci

echo "Inicializando recursos AWS en floci..."

# Crear buckets

awslocal s3 mb s3://app-artifacts
awslocal s3 mb s3://app-logs

# Crea prefijos (carpetas)

awslocal s3api put-object \
		--bucket app-artifacts \
		--key releases/.keep

# Activar versionado

awslocal s3api put-bucket-versioning \
		--bucket app-artifacts \
		--versioning-configuration Status=Enabled

# Cola SQS para notificaciones de deploy

awslocal sqs create-queue \
		--queue-name deploy-notifications

echo "Floci listo - buckets: app-artifacts, app-logs"
