# Install External Secrets
helm repo add external-secrets https://charts.external-secrets.io

helm install external-secrets \
   external-secrets/external-secrets \
    -n external-secrets \
    --create-namespace \
    --set installCRDs=true


# Create ESO Gitlab Token Secret
kubectl apply -f gitlab_eso_token.yaml -n external-secrets

# Create ClusterSecretStore
kubectl apply -f cluster_secret_store.yaml -n external-secrets

# External Secret created by chart