import customtkinter as ctk
import psutil
import time


# Initializing the app window.
app = ctk.CTk()  
app.title("Basic CustomTkinter App")
app.geometry("400x300")

# Title Label
title_label = ctk.CTkLabel(app, text="Welcome to CustomTkinter", font=("Arial", 20, "bold"))
title_label.pack(pady=20)



# Array to store process data.
res = []

def display_process_info():
    res.append(['PID','CPU%','Memory%','Name','Status'])
    print("="*70)
    for proc in psutil.process_iter(attrs=['pid', 'name', 'status']):
        try:
            process = proc.info
            pid = process['pid']
            name = process['name']
            status = process['status']


            cpu_percent = proc.cpu_percent(interval=0.1)  
            memory_percent = proc.memory_percent()       

            res.append([pid,cpu_percent,memory_percent,name,status])

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):

            continue
# Fetching process data at startup.
display_process_info()


# Function to Terminate a process using it's PID.
def kill_process():
    pid = int(search_label.get())
    try:
        process = psutil.Process(pid)
        process_name = process.name()


        process.terminate()
        process.wait(3)  # Wait during termination.

        if process.is_running(): 
            process.kill()
            output_label.configure(text=f"❌ Process {process_name} (PID: {pid}) forcefully killed.")
        else:
            output_label.configure(text=f"✅ Process {process_name} (PID: {pid}) terminated successfully.")

    except psutil.NoSuchProcess:
        output_label.configure(text=f"⚠️ No such process with PID: {pid}")
    except psutil.AccessDenied:
        output_label.configure(text=f"⛔ Permission denied to terminate process {pid}")
    except Exception as e:
        output_label.configure(text=f"❗ An error occurred: {e}")

# Search for a process using it's PID and displaying it's details.
def search():
    key = int(search_label.get())
    for i in range(1,len(res)):
        if(key==res[i][0]):
            output_label.configure(text=f"{res[i][0]}\t{round(res[i][1],2)}\t{round(res[i][2]*20,2)}\t{res[i][3]}\t{res[i][4]}")
            break


# PID Input Field/Box.
search_label = ctk.CTkEntry(app,placeholder_text='Enter the pid you need to search')
search_label.pack()

# Search button.
search_btn = ctk.CTkButton(app,command=search, text="search")
search_btn.pack()

# Output Label.
output_label = ctk.CTkLabel(app,text="")
output_label.pack()

# Terminate button.
kill_btn = ctk.CTkButton(app,command=kill_process,text="Terminate?")
kill_btn.pack()



    #     if(search_label.)
# Scrollable Window for displaying Process List.
scrollable_frame = ctk.CTkScrollableFrame(app, width=350, height=300)
scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Displaying Process List into the Scrollable Frame.
for i in range(1,len(res)):
    output_label1 = ctk.CTkLabel(scrollable_frame, text=f"{res[i][0]}")
    output_label1.grid(pady=12, row=i+1,column=0)
    output_label2 = ctk.CTkLabel(scrollable_frame, text=f"{round(res[i][1],2)}")
    if(round(res[i][2]*20,2)>50):
        output_label2.grid(pady=12, row=i+1,column=1)
        output_label3 = ctk.CTkLabel(scrollable_frame, text=f"{round(res[i][2]*20000,2)}")# bg_color=f"#{res[i][2]-50}0000"
    else:
        output_label2.grid(pady=12, row=i+1,column=1)
        output_label3 = ctk.CTkLabel(scrollable_frame, text=f"{round(res[i][2]*20000,2)}")
        
    output_label3.grid(pady=12, row=i+1,column=2)
    output_label4 = ctk.CTkLabel(scrollable_frame, text=f"{res[i][3]}")
    output_label4.grid(pady=12, row=i+1,column=3)
    output_label5 = ctk.CTkLabel(scrollable_frame, text=f"{res[i][4]}")
    output_label5.grid(pady=12, row=i+1,column=4)
    
# Function call to Run the application.
app.mainloop()

def refresh_process_list():
    global res
    res = [['PID','CPU%','Memory%','Name','Status']]
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    for proc in psutil.process_iter(attrs=['pid', 'name', 'status']):
        try:
            process = proc.info
            pid = process['pid']
            name = process['name']
            status = process['status']
            cpu_percent = proc.cpu_percent(interval=0.1)  
            memory_percent = proc.memory_percent()
            res.append([pid,cpu_percent,memory_percent,name,status])
        except:
            continue

    for i in range(1,len(res)):
        ctk.CTkLabel(scrollable_frame, text=f"{res[i][0]}").grid(pady=6, row=i,column=0)
        ctk.CTkLabel(scrollable_frame, text=f"{round(res[i][1],2)}").grid(pady=6, row=i,column=1)
        ctk.CTkLabel(scrollable_frame, text=f"{round(res[i][2]*20000,2)}").grid(pady=6, row=i,column=2)
        ctk.CTkLabel(scrollable_frame, text=f"{res[i][3]}").grid(pady=6, row=i,column=3)
        ctk.CTkLabel(scrollable_frame, text=f"{res[i][4]}").grid(pady=6, row=i,column=4)


#A button to refresh
refresh_btn = ctk.CTkButton(app, command=refresh_process_list, text="🔄 Refresh List")
refresh_btn.pack()
