import app.data.schema as schema
import app.data.incidents as incidents
import app.data.tickets as tickets
import app.data.datasets as datasets


def PromptForCRUD(tableName: str) -> None:
    userInp: int = int(input(f"1) CREATE {tableName}\n2) READ {tableName}\n3) UPDATE {tableName}\n4) DELETE {tableName}\n"))
    match userInp:
        case 1:
            CreateRow()
        case 2:
            ReadRow()
        case 3:
            UpdateRow()
        case 4:
            DeleteRow()
        case _:
            print("WRONG INPUT")


def GetTableName() -> str:
    userInp: int = int(input("1) Cyber_Incidents\n2) IT_Tickets\n3) Datasets_Metadata\n"))
    match userInp:
        case 1:
            return "Cyber_Incidents"
        case 2:
            return "IT_Tickets"
        case 3:
            return "Datasets_Metadata"
        case _:
            return "WRONG INPUT"


def CreateRow():
    match tableName: #type: ignore
        case "Cyber_Incidents":
            date = input("Enter date: ")
            incidentName = input("Enter incident name: ")
            severity: str = input("Enter severity: ")
            status: str = input("Enter status: ")
            incidents.InsertIncident(date, incidentName, severity, status)
        case "IT_Tickets":
            id = input("Enter ticket id: ")
            sub = input("Enter subject ")
            prio = input("Enter priority:  ")
            status = input("Enter status: ")
            crDate = input("Enter created date: ")
            tickets.InsertTicket(id, sub, prio, status, crDate)
        case "Datasets_Metadata":
            id = input("Enter ticket id: ")
            name = input("Enter name ")
            ctgry = input("Enter ctgry: ")
            fileSize = input("Enter fileSize: ")
            datasets.InsertDataset(id, name, ctgry, fileSize)
            

def ReadRow():
    id = int(input("Enter id: "))
    match tableName:
        case "Cyber_Incidents":
            print(incidents.GetAllIncidents(f"id = {id}"))
        case "IT_Tickets":
            print(tickets.GetAllTickets(f"ticket_id = {id}"))
        case "Datasets_Metadata":
            print(datasets.GetAllDatasets(f"id = {id}"))
        
        

def UpdateRow():
    id = input("Enter id: ")
    match tableName:
        case "Cyber_Incidents":
            newId = input("Enter new id: ")
            date = input("Enter date: ")
            incidentName = input("Enter incident name: ")
            severity: str = input("Enter severity: ")
            status: str = input("Enter status: ")
            incidents.UpdateIncident(id, newId, date, incidentName, severity, status)
        case "IT_Tickets":
            newId = input("Enter ticket id: ")
            sub = input("Enter subject ")
            prio = input("Enter priority:  ")
            status = input("Enter status: ")
            crDate = input("Enter created date: ")
            tickets.UpdateTicket(id, newId, sub, prio, status, crDate)
        case "Datasets_Metadata":
            newid = input("Enter ticket id: ")
            name = input("Enter name ")
            ctgry = input("Enter ctgry: ")
            fileSize = input("Enter fileSize: ")
            datasets.UpdateDatasets(id, newid, name, ctgry, fileSize)
            
def DeleteRow():
    id =input("Enter id: ")
    match tableName:
        case "Cyber_Incidents":
            incidents.DeleteIncident(id)
        case "IT_Tickets":
            tickets.DeleteTicket(id)
        case "Datasets_Metadata":
            datasets.DeleteDataset(id)
    

if __name__ == "__main__":
    schema.CreateAllTables()
    tableName: str = GetTableName()
    PromptForCRUD(tableName)