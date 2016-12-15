from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings
import os
import sys

def upload_results():
  blob_service = BlockBlobService(account_name='gpuvmtemplatedisks530', account_key='9aSfzJqvoasgkzMod9qNJGDabjtSUbibZjjvsnvHaYMatASwF/y9kH2nbTAOKnLb7bLWjdIJUdwzXhTCvO2L/g==')

  ouputPath = '../output'
  files = os.listdir(ouputPath)

  for file in files:
    blob_service.create_blob_from_path(
        'dinero',
        str(file),
        os.path.join(ouputPath, file))

def download_checkpoint_file(filename):
  blob_service = BlockBlobService(account_name='gpuvmtemplatedisks530',       account_key='9aSfzJqvoasgkzMod9qNJGDabjtSUbibZjjvsnvHaYMatASwF/y9kH2nbTAOKnLb7bLWjdIJUdwzXhTCvO2L/g==')
  blob_service.get_blob_to_path('dinero', 'model.ckp', filename)
