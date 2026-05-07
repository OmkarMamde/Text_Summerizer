from huggingface_hub import login, upload_folder

# (optional) Login with your Hugging Face credentials
login()

# Push your model files
upload_folder(folder_path="C:\Text_Summerizer\saved_summary_model", repo_id="OmkarMamde/summerizer-t5", repo_type="model")
