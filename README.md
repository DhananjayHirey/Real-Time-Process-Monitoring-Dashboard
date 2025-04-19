# 🖥️ CustomTkinter Process Manager

A lightweight desktop application built using **Python**, **psutil**, and **CustomTkinter**, providing real-time insights into running processes on your system. You can **search**, **view**, **refresh**, and even **terminate** processes based on their PID (Process ID).

---

## 🚀 Features

- View all running processes with details like:
  - PID
  - CPU usage %
  - Memory usage %
  - Process Name
  - Status
- Search for a process by entering its PID
- Terminate a process with a single click
- Refresh the process list dynamically
- Scrollable UI for viewing long lists of processes
- Clean modern interface using `customtkinter`

---

## 🛠️ Requirements

- Python 3.7+
- [psutil](https://pypi.org/project/psutil/)
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter)

Install the dependencies using:

```bash
pip install psutil customtkinter
