import os, json

class Task:
    def __init__(self):
        self.db = "data.json"

    def all_tasks(self):
        try:
            with open(self.db, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return "Error 404!"

        
    def add_new_task(self, title: str, describe: str, date):
        try:
            with open(self.db, "r", encoding="utf-8") as f:
                t = json.load(f)
        except:
            t = []
        finished = False
        data = {
            #"id":len(t)+1,
            "title":title,
            "describe":describe,
            "date":date,
            "Done":finished,
        }
        t.append(data)
        with open(self.db, "w", encoding="utf-8") as f:
            json.dump(t, f, ensure_ascii=False, indent=4)
        return "added new Task Successfully!"
    
    def dele_task(self, title):
        try:
            if os.path.exists(self.db): 
                de = False
                with open(self.db, "r", encoding="utf-8") as f:
                    t = json.load(f)
                    for i in t:
                        if i["title"] == title:
                            t.remove(i)  
                            de = True
                    with open(self.db, "w", encoding="utf-8") as f:
                            json.dump(t, f, ensure_ascii=False, indent=4)  
                if de:
                    return "Suceess deleted!"
                else:
                    return "task NOT Found 404!"
        except:
            return "Json File NOT Found 404!"
        
    def show_not_finished_task(self):
        try:
            with open(self.db, "r", encoding="utf-8") as f:
                t = json.load(f)
                for i in t:
                    if i['Done'] == False:
                        print(i)
        except:
            return "Json File NOT Found 404!"
        
    def finish_task(self, title):
        try:
            if os.path.exists(self.db): 
                fi = False
                with open(self.db, "r", encoding="utf-8") as f:
                    t = json.load(f)
                    for i in t:
                        if i["title"] == title:
                            if i["Done"] == False:
                                i["Done"] = True  
                                fi = True
                    with open(self.db, "w", encoding="utf-8") as f:
                            json.dump(t, f, ensure_ascii=False, indent=4)  
                if fi:
                    return "Suceess Updated!"
                else:
                    return "task NOT Found 404!"
        except:
            return "Json File NOT Found 404!"

        
