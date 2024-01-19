import os
from datetime import datetime

class Logger:
    def __init__(self, print_log=False):
        self.script_path = os.path.abspath(__file__)
        self.log_dir_path = os.getcwd()+"\\LOG"
        self.true_name = os.path.basename(self.script_path)
        self.file_name = os.path.splitext(self.true_name)[0]
        self.print_log = print_log

        # Cree le repertoire de logs s'il n'existe pas
        if not os.path.exists(self.log_dir_path):
            os.makedirs(self.log_dir_path)

    def get_now(self):
        return datetime.now().strftime("%H:%M:%S")

    def write(self, txt, log_type, file_name, should_print):
        log_file_path = os.path.join(self.log_dir_path, f"{datetime.now().strftime('%Y-%m-%d')}.log")

        with open(log_file_path, "a") as file:
            # [20:10:22] [main/INFO]: txt
            content = f"[{self.get_now()}] [{file_name}/{log_type.upper()}]: {str(txt)}"
            file.write(content + "\n")

            if should_print:
                if log_type == "error":
                    print(f"\033[1;31m{content}\033[0m")
                elif log_type == "warning":
                    print(f"\033[1;33m{content}\033[0m")
                elif log_type == "log":
                    print(content)

    def log(self, msg):
        self.write(msg, "log", self.file_name, self.print_log)

    def error(self, msg):
        self.write(msg, "error", self.file_name, self.print_log)

    def warning(self, msg):
        self.write(msg, "warning", self.file_name, self.print_log)
    

