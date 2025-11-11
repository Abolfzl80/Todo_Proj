import os, json

class Task:
    def __init__(self):
        self.db = "data.json"

    def All_Tasks(self):
        try:
            with open(self.db, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return "Error 404!"

        
    def Add_New_Task(self, title: str, describe: str, date):
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
    
    def Dele_Task(self, title):
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
        
    def Show_Not_Finished_Task(self):
        try:
            with open(self.db, "r", encoding="utf-8") as f:
                t = json.load(f)
                for i in t:
                    if i['Done'] == False:
                        print(i)
        except:
            return "Json File NOT Found 404!"
        
    def Finish_Task(self, title):
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

        

dd = Task()

print(dd.Add_New_Task("read book", "reading book for 2H", "1404.9.1"))
print(dd.Add_New_Task("play game", "play cs2 for 3H", "1404.8.20"))
print(dd.Add_New_Task("asleep", "just sleep:)", "1404.8.21"))

print(dd.All_Tasks())
print(dd.Dele_Task("play game"))
dd.Show_Not_Finished_Task()
print(dd.Finish_Task("play game"))