import toml
from os import environ

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.config = toml.load("sample.config.toml")
        return cls._instance
    
    def __init__(self):
        self.config = toml.load("sample.config.toml")

    def get_config(self):
        return self.config
    
    def get_bing_api_key(self):
        return environ.get("BING_API_KEY", self.config["API_KEYS"]["BING"])
    
    def get_bing_api_endpoint(self):
        return environ.get("BING_API_ENDPOINT", self.config["API_ENDPOINTS"]["BING"])

    def get_claude_api_key(self):
        return environ.get("CLAUDE_API_KEY", self.config["API_KEYS"]["CLAUDE"])

    def get_openai_api_key(self):
        return environ.get("OPENAI_API_KEY", self.config["API_KEYS"]["OPENAI"])

    def get_netlify_api_key(self):
        return environ.get("NETLIFY_API_KEY", self.config["API_KEYS"]["NETLIFY"])
      
    def get_sqlite_db(self):
        return environ.get("SQLITE_DB_PATH", self.config["STORAGE"]["SQLITE_DB"])

    def get_screenshots_dir(self):
        return environ.get("SCREENSHOTS_DIR", self.config["STORAGE"]["SCREENSHOTS_DIR"])

    def get_pdfs_dir(self):
        return environ.get("PDFS_DIR", self.config["STORAGE"]["PDFS_DIR"])

    def get_projects_dir(self):
        return environ.get("PROJECTS_DIR", self.config["STORAGE"]["PROJECTS_DIR"])

    def get_logs_dir(self):
        return environ.get("LOGS_DIR", self.config["STORAGE"]["LOGS_DIR"])

    def get_repos_dir(self):
        return environ.get("REPOS_DIR", self.config["STORAGE"]["REPOS_DIR"])

    def get_logging_rest_api(self):
        return self.config["LOGGING"]["LOG_REST_API"] == "true"

    def get_logging_prompts(self):
        return self.config["LOGGING"]["LOG_PROMPTS"] == "true"

    def set_bing_api_key(self, key):
        self.config["API_KEYS"]["BING"] = key
        self.save_config()

    def set_bing_api_endpoint(self, endpoint):
        self.config["API_ENDPOINTS"]["BING"] = endpoint
        self.save_config()


    def set_claude_api_key(self, key):
        self.config["API_KEYS"]["CLAUDE"] = key
        self.save_config()

    def set_openai_api_key(self, key):
        self.config["API_KEYS"]["OPENAI"] = key
        self.save_config()

    def set_netlify_api_key(self, key):
        self.config["API_KEYS"]["NETLIFY"] = key
        self.save_config()

    def set_sqlite_db(self, db):
        self.config["STORAGE"]["SQLITE_DB"] = db
        self.save_config()

    def set_screenshots_dir(self, dir):
        self.config["STORAGE"]["SCREENSHOTS_DIR"] = dir
        self.save_config()

    def set_pdfs_dir(self, dir):
        self.config["STORAGE"]["PDFS_DIR"] = dir
        self.save_config()

    def set_projects_dir(self, dir):
        self.config["STORAGE"]["PROJECTS_DIR"] = dir
        self.save_config()

    def set_logs_dir(self, dir):
        self.config["STORAGE"]["LOGS_DIR"] = dir
        self.save_config()

    def set_repos_dir(self, dir):
        self.config["STORAGE"]["REPOS_DIR"] = dir
        self.save_config()

    def set_logging_rest_api(self, value):
        self.config["LOGGING"]["LOG_REST_API"] = "true" if value else "false"
        self.save_config()

    def set_logging_prompts(self, value):
        self.config["LOGGING"]["LOG_PROMPTS"] = "true" if value else "false"
        self.save_config()

    def save_config(self):
        with open("sample.config.toml", "w") as f:
            toml.dump(self.config, f)